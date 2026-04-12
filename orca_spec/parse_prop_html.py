# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "beautifulsoup4>=4.14.3",
# ]
# ///


from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

file = Path("9.4. Property File - ORCA 6.1 Manual.html").read_text()
soup = BeautifulSoup(file, features="html.parser")

# orca_dtypes = {
#     "D": "Double",
#     "C": "Complex",
#     "S": "String",
#     "I": "Integer",
#     "B": "Boolean",
#     "AD": "ArrayOfDoubles",
#     "AC": "ArrayOfComplex",
#     "AI": "ArrayOfIntegers",
#     "AB": "ArrayOfBooleans",
#     "CC": "Coordinates",
# }

orca_dtypes = {
    "D": "float",
    "C": "complex",
    "S": "str",
    "I": "int",
    "B": "bool",
    "AD": "list[float]",
    "AC": "list[complex]",
    "AI": "list[int]",
    "AB": "list[bool]",
    "CC": "list[str, float, float, float]",
}

table_data = [[cell.text for cell in row("td")] for row in soup("tr")]
table_dict = {}
for item in table_data[1:]:
    if item[0].startswith(" ") or item[1] not in orca_dtypes.keys():
        parent = item[0]
        table_dict[parent] = {}
        multiple_allowed = item[1].strip().lower() == "y"
        table_dict[parent]["multiple_allowed"] = multiple_allowed
        table_dict[parent]["components"] = {}
        item = item[2:]

    comp_type = orca_dtypes[item[1]]

    table_dict[parent]["components"][item[0]] = {
        "type": comp_type,
        "optional": item[2].strip().lower() == "y",
        "list": item[3].strip().lower() == "y",
        "description": item[4] if item[4] != "" else None,
    }

    if item[5] != "":
        table_dict[parent]["components"][item[0]]["units"] = item[5]
# print(json.dumps(tab_dict, indent=4))

nested_prop_map = {}

tiered_dict = {}
for key, val in table_dict.items():
    if "]" in key:
        super_type = re.search(r'\[([\w]+)\]', key).group(1)
        if super_type not in tiered_dict.keys():
            tiered_dict[super_type] = {}

        key_name = key.strip().split()[0]
        if super_type in key_name:
            key_name = key_name.replace(f"_{super_type}", "").replace(f"{super_type}_", "")
        elif super_type == "Energy":
            key_name = key_name.replace("_Energies", "").replace("Energies_", "")
        elif super_type == "Nuclear_Gradient":
            key_name = key_name.replace("_Nuc_Gradient", "").replace("Nuc_Gradient_", "")
        
        nested_prop_map[key.strip().split()[0]] = {"super_type": super_type, "key_name": key_name}
        tiered_dict[super_type][key_name] = val
    else:
        key_name = key.strip().split()[0]

        if key_name in tiered_dict.keys():
            # This essentially just creates a "base" list of components.
            # Other methods may have additional items.
            tiered_dict[key_name]["multiple_allowed"] = val["multiple_allowed"]
            tiered_dict[key_name]["components"] = val["components"]
        else:
            tiered_dict[key_name] = val

# tiered_dict = {"Energy": tiered_dict["Energy"]}
final_dict = {}
for parent, child in tiered_dict.items():
    final_dict[parent] = {
        "multiple_allowed": tiered_dict[parent]["multiple_allowed"],
        "components": tiered_dict[parent]["components"],
    }
    for item in child:
        if item in ["multiple_allowed", "components"]:
            continue
        else:
            final_dict[parent][item] = {}

        if tiered_dict[parent][item]["components"] == child["components"]:
            final_dict[parent][item]["additional_components"] = None
        else:
            final_dict[parent][item]["additional_components"] = {}
            for comp_key, comp_val in tiered_dict[parent][item]["components"].items():
                if comp_key not in child["components"].keys() or comp_val != child["components"][comp_key]:
                    final_dict[parent][item]["additional_components"][comp_key] = comp_val

        if tiered_dict[parent][item]["multiple_allowed"] != child["multiple_allowed"]:
            final_dict[parent][item]["multiple_allowed"] = tiered_dict[parent][item]["multiple_allowed"]

Path("orca_prop_spec_py.json").write_text(json.dumps(final_dict, indent=4))
#print("nested_prop_map = {")
#for key, val in nested_prop_map.items():
#    print(f"    {key}: {val}")
#print("}")
