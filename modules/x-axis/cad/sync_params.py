"""
Sync params.csv into the FreeCAD Spreadsheet named 'Params'.

Usage (FreeCAD Python console):
    exec(open("cad/sync_params.py").read())

Usage (headless, from the module root):
    FreeCADCmd cad/assemblies/x-axis.FCStd cad/sync_params.py
"""
import csv
from pathlib import Path


def sync_params(doc=None, csv_path=None):
    import FreeCAD  # only available inside FreeCAD runtime

    if doc is None:
        doc = FreeCAD.ActiveDocument
    if doc is None:
        raise RuntimeError("No active FreeCAD document.")

    sheet = doc.getObjectsByLabel("Params")
    if not sheet:
        raise RuntimeError("No Spreadsheet named 'Params' in document.")
    sheet = sheet[0]

    here = Path(__file__).parent
    csv_path = csv_path or (here / "params.csv")

    updated = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            alias = row["alias"].strip()
            value = row["value"].strip()
            unit = row.get("unit", "").strip()
            cell_value = f"{value} {unit}".strip() if unit else value
            sheet.set(alias, cell_value)
            updated.append(alias)

    doc.recompute()
    doc.save()
    print(f"Synced {len(updated)} parameters: {', '.join(updated)}")


if __name__ == "__main__":
    sync_params()
