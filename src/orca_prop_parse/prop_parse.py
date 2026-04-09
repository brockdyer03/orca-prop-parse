from io import StringIO
from typing import Any
import re
import json
import rtoml


class OrcaPropFile:
    """Parsing and conversion for ORCA's ``.property.txt`` files"""

    @classmethod
    def _parse_props(cls, prop_io: StringIO, num_geoms: int) -> dict[str, Any]:
        prop_dict = {"Geometries": [None]*num_geoms}
        while True:
            line = prop_io.readline()
            if line == "":
                break
            elif line.startswith("$Calculation_"):
                prop = line[1:].strip()
                geom_number, prop_info = cls._parse_prop(prop_io)
                prop_dict[prop] = prop_info
            elif line.startswith("$"):
                geom_number, prop_info = cls._parse_prop(prop_io)
                prop_dict["Geometries"][geom_number] = prop_info

    @classmethod
    def loads(cls, prop_str: str) -> dict[str, Any]:
        num_geoms = max(map(int, re.findall(r"&GeometryIndex ([0-9]+)", prop_str)))
        prop_io = StringIO(prop_str)
        return cls._process_props(prop_io, num_geoms)

    @classmethod
    def _parse_prop(cls, prop_io: StringIO) -> dict[str, Any]:
        prop_dict = {}
        geom_number = int(prop_io.readline().split()[-1]) # &GeometryIndex N
        line = prop_io.readline().strip()
        while line != "$End":
            # &NAtoms [&Type "Integer"] 10
            comp_name = line.split(maxsplit=1)[0].replace("&", "")
            dtype, dimensions, units = re.search(
                r'\[&Type "(\w+)"(?:, &Dim(\([0-9]+,[0-9]+\)))?(?:, &Units "(\w+)")?\]',
                line,
            )
            match dtype:
                case "Double":
                    prop_dict[comp_name] = float(re.search(r' ([-\+]?[\.0-9]+(?:[e][-\+]?[\.0-9]+)?) ', line).group(1))
                case "Integer":
                    prop_dict[comp_name] = int(re.search(r' ([0-9]+) ', line).group(1))
                case "Boolean":
                    prop_dict[comp_name] = "true" in line
                case "Complex":
                    real, imag = re.search(
                        r' ([-\+]?[\.0-9]+(?:[e][-\+]?[\.0-9]+)?) ([-\+]?[\.0-9]+(?:[e][-\+]?[\.0-9]+)?) ',
                        line,
                    ).groups()
                    prop_dict[comp_name] = complex(float(real), float(imag))
                case "String":
                    prop_dict[comp_name] = line.split('] "', maxsplit=1)[-1].split('"', maxsplit=1)[0]
                case "ArrayOfDoubles" | "ArrayOfIntegers" | "ArrayOfBooleans" | "ArrayOfComplex":
                    prop_dict[comp_name] = cls._parse_array(prop_io)
                case "Coordinates":
                    prop_dict[comp_name] = []
                    for _ in range(dimensions[0]):
                        atom = prop_io.readline().strip().split()
                        prop_dict[comp_name].append([
                            atom[0],        # Symbol
                            float(atom[1]), # x
                            float(atom[2]), # y
                            float(atom[3]), # z
                        ])
            
            return prop_dict, geom_number

    @staticmethod
    def _parse_array(prop_io: StringIO) -> list[Any]:
        raise NotImplementedError("Array types have not been implemented yet!")
