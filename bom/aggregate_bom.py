"""Aggregate all module bom/bom.csv files into the root bom/bom.csv (generated)."""
from pathlib import Path
import csv


def aggregate(root: Path, out_path: Path) -> None:
    rows: list[dict] = []
    for bom_file in sorted(root.rglob("bom/bom.csv")):
        if bom_file.resolve() == out_path.resolve():
            continue
        rel = bom_file.parent.parent.relative_to(root)
        with open(bom_file, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["module"] = str(rel)
                rows.append(row)
    if not rows:
        print("No module BOM files found.")
        return
    fieldnames = ["module"] + [k for k in rows[0] if k != "module"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    aggregate(root, root / "bom" / "bom.csv")
