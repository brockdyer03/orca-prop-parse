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

tab_data = [[cell.text for cell in row("td")] for row in soup("tr")]
tab_dict = {}
for item in tab_data[1:]:
    if item[0].startswith(" "):
        parent = item[0]
        tab_dict[parent] = {}
        multiple_allowed = item[1].strip().lower() == "y"
        tab_dict[parent]["multiple_allowed"] = multiple_allowed
        tab_dict[parent]["components"] = {}
        item = item[2:]
    elif item[1] not in ["D", "C", "S", "I", "B", "AD", "AC", "AI", "AB", "CC"]:
        parent = item[0]
        tab_dict[parent] = {}
        multiple_allowed = item[1].strip().lower() == "y"
        tab_dict[parent]["multiple_allowed"] = multiple_allowed
        tab_dict[parent]["components"] = {}
        item = item[2:]

    match item[1]:
        case "D":
            comp_type = "Double"
        case "C":
            comp_type = "Complex"
        case "S":
            comp_type = "String"
        case "I":
            comp_type = "Integer"
        case "B":
            comp_type = "Boolean"
        case "AD":
            comp_type = "ArrayOfDoubles"
        case "AC":
            comp_type = "ArrayOfComplex"
        case "AI":
            comp_type = "ArrayOfIntegers"
        case "AB":
            comp_type = "ArrayOfBooleans"
        case "CC":
            comp_type = "Coordinates"
        case _:
            print(item)
            raise ValueError(f"Unrecognized type: {item[1]}")

    tab_dict[parent]["components"][item[0]] = {
        "type": comp_type,
        "optional": item[2].strip().lower() == "y",
        "list": item[3].strip().lower() == "y",
    }

    if item[5] != "":
        tab_dict[parent]["components"][item[0]]["units"] = item[5]
# print(json.dumps(tab_dict, indent=4))

final_dict = {}
for key, val in tab_dict.items():
    if "]" in key:
        super_type = re.search(r'\[([\w]+)\]', key).group(1)
        if super_type not in final_dict.keys():
            final_dict[super_type] = {}

        key_name = key.strip().split()[0]
        if super_type in key_name:
            key_name = key_name.replace(f"_{super_type}", "")
        elif super_type == "Energy":
            key_name = key_name.replace("_Energies", "")
        elif super_type == "Nuclear_Gradient":
            key_name = key_name.replace("_Nuc_Gradient", "")

        final_dict[super_type][key_name] = val

Path("orca_prop_spec.json").write_text(json.dumps(final_dict, indent=4))
