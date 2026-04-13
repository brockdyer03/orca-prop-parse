from pathlib import Path
import sys
from .prop_parse import prop_to_json, prop_to_toml


def prop2json() -> None:
    inp = Path(sys.argv[1]).resolve()
    if len(sys.argv) > 2:
        out = Path(sys.argv[2])
    else:
        out = inp.parent / inp.name.replace(".txt", ".json")

    print(f"Writing output to {out.name}...")
    prop_to_json(inp, out)
    print("Done!")


def prop2toml() -> None:
    inp = Path(sys.argv[1]).resolve()
    if len(sys.argv) > 2:
        out = Path(sys.argv[2])
    else:
        out = inp.parent / inp.name.replace(".txt", ".toml")

    print(f"Writing output to {out.name}...")
    prop_to_toml(inp, out)
    print("Done!")
