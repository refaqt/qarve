# Top-level bill of materials

`bom.csv` at this path is **generated** by `aggregate_bom.py` from every `**/bom/bom.csv` under the repo (typically under `modules/` when sub-assemblies exist). Do not edit it by hand.

```powershell
python bom/aggregate_bom.py
```

Module-level `bom/bom.csv` files are source data and are committed.
