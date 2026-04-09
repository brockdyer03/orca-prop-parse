from warnings import warn
from io import StringIO
from typing import Any
import re
import json
import rtoml


class OrcaPropParse:
    """Parsing and conversion for ORCA's ``.property.txt`` files"""

    @classmethod
    def _parse_props(cls, prop_io: StringIO, num_geoms: int) -> dict[str, Any]:
        prop_dict = {"Geometries": [{} for _ in range(num_geoms)]}
        while True:
            line = prop_io.readline()
            if line == "":
                break
            elif line.startswith("$Calculation_"):
                prop = line[1:].strip()
                prop_info, geom_number = cls._parse_prop(prop_io)
                prop_dict[prop] = prop_info
            elif line.startswith("$"):
                prop = line[1:].strip()
                prop_info, geom_number = cls._parse_prop(prop_io)
                prop_dict["Geometries"][geom_number][prop] = prop_info
        return prop_dict

    @classmethod
    def loads(cls, prop_str: str) -> dict[str, Any]:
        num_geoms = max(map(int, re.findall(r"&GeometryIndex ([0-9]+)", prop_str)))
        prop_io = StringIO(prop_str)
        return cls._parse_props(prop_io, num_geoms)

    @classmethod
    def _parse_prop(cls, prop_io: StringIO) -> tuple[dict[str, Any], int]:
        prop_dict = {}
        geom_number = int(prop_io.readline().split()[-1]) - 1 # &GeometryIndex N
        line = prop_io.readline()
        while line.strip() != "$End":
            comp_name = line.split(maxsplit=1)[0].replace("&", "")
            dtype, dimensions, units = re.search(
                r'\[&Type "(\w+)"(?:, &Dim ?\(([0-9]+,[0-9]+)\)|, &Units "([-\.\w^]+)"){0,2}\]',
                line,
            ).groups()
            if dimensions is not None:
                dimensions = tuple(map(int, dimensions.split(",")))

            match dtype:
                case "Double":
                    prop_dict[comp_name] = float(re.search(r'\b([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?)\b', line).group(1))
                case "Integer":
                    prop_dict[comp_name] = int(re.search(r'\b([0-9]+)\b', line).group(1))
                case "Boolean":
                    prop_dict[comp_name] = "true" in line
                case "Complex":
                    warn("Complex number parsing has not been tested!")
                    real, imag = re.search(
                        r'\b([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?) ([-\+]?[0-9]\.[0-9]+(?:[e][-\+]?[\.0-9]+)?)\b',
                        line,
                    ).groups()
                    prop_dict[comp_name] = complex(float(real), float(imag))
                case "String":
                    prop_dict[comp_name] = line.split('] "', maxsplit=1)[-1].split('"', maxsplit=1)[0]
                case "ArrayOfDoubles" | "ArrayOfIntegers" | "ArrayOfBooleans":
                    prop_dict[comp_name] = cls._parse_array(prop_io, dtype, dimensions)
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
                case "ArrayOfComplex":
                    raise NotImplementedError(
                        "ArrayOfComplex parsing not yet implemented!\n"
                       f"ArrayOfComplex found at position {prop_io.tell()}!"
                    )
            line = prop_io.readline()

        return prop_dict, geom_number

    @staticmethod
    def _parse_array(
        prop_io: StringIO,
        array_type: str,
        dim: tuple[int, int],
    ) -> list[Any | list[Any]]:

        array = []
        if dim[1] == 1:
            for _ in range(2):
                prop_io.readline() # Skip over 2nd dimension index and comment line

            for _ in range(dim[0]):
                array.append(
                    prop_io.readline().strip().split()[-1]
                )

            match array_type:
                case "ArrayOfDoubles":
                    return list(map(float, array))
                case "ArrayOfIntegers":
                    return list(map(int, array))
                case "ArrayOfBooleans":
                    return list(map(lambda x: x.lower() == "true", array))
                case _:
                    raise ValueError(
                        f"Array type {array_type} not recognized!"
                    )
        else:
            for _ in range(dim[0]):
                array.append([])

            num_blocks = ((dim[1] - (dim[1] % 8)) / 8) + 1 if dim[1] > 8 else 1
            for b in range(num_blocks):
                for _ in range(2):
                    prop_io.readline() # Skip over 2nd dimension index and comment line

                for i in range(dim[0]):
                    line = prop_io.readline().strip().split()
                    arr_index = int(line[0])
                    array[arr_index].extend(line[1:])
            
            match array_type:
                case "ArrayOfDoubles":
                    return [list(map(float, row)) for row in array]
                case "ArrayOfIntegers":
                    return [list(map(int, row)) for row in array]
                case "ArrayOfBooleans":
                    return [list(map(lambda x: x.lower() == "true", row)) for row in array]
                case _:
                    raise ValueError(
                        f"Array type {array_type} not recognized!"
                    )
