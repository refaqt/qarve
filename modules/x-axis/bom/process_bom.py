"""Render module bom.csv to bom_output.md (generated, gitignored)."""
import csv
from pathlib import Path


def load_bom(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render_markdown(bom: list[dict], out_path: Path) -> None:
    header = "| ID | Name | Qty | Unit Cost (€) | Total (€) | Primary Supplier |"
    sep = "|----|------|-----|--------------|-----------|-----------------|"
    lines = ["# Bill of Materials\n", header, sep]
    for r in bom:
        total = float(r.get("unit_cost_eur") or 0) * int(r.get("qty") or 0)
        lines.append(
            f"| {r['id']} | {r['name']} | {r['qty']} | "
            f"{r.get('unit_cost_eur', '')} | {total:.2f} | {r.get('supplier_1', '')} |"
        )
    grand = sum(
        float(r.get("unit_cost_eur") or 0) * int(r.get("qty") or 0) for r in bom
    )
    lines.append(f"\n**Grand Total: €{grand:.2f}**")
    out_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    here = Path(__file__).parent
    bom = load_bom(here / "bom.csv")
    render_markdown(bom, here / "bom_output.md")
    print(f"Wrote {here / 'bom_output.md'}")
