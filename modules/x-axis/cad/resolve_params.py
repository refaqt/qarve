"""Merge default + model override → active params.csv."""
import csv
import sys
from pathlib import Path


def resolve(here: Path, model: str) -> None:
    default_path = here / "params" / "default.csv"
    default = {
        r["alias"]: r
        for r in csv.DictReader(open(default_path, newline="", encoding="utf-8"))
    }
    if model != "default":
        override_path = here / "params" / f"{model}.csv"
        for row in csv.DictReader(open(override_path, newline="", encoding="utf-8")):
            default[row["alias"]] = row
    rows = sorted(default.values(), key=lambda r: r["alias"])
    out = here / "params.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["alias", "value", "unit", "description"])
        w.writeheader()
        w.writerows(rows)
    print(f"Resolved model '{model}' -> {out} ({len(rows)} params)")


if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else "default"
    resolve(Path(__file__).parent, model)
