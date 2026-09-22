# Top-level bill of materials

`bom.csv` at this path is **generated** by `doqs/scripts/aggregate_bom.py` from every `**/bom/bom.csv` under the repo (typically under `modules/` when sub-assemblies exist). Do not edit it by hand.

```powershell
python doqs/doqs.py generate
```

Module-level `bom/bom.csv` files are source data and are committed.

The aggregating tool lives in the `doqs/` submodule and updates with it. A copy of it in this folder would go out of date without anybody noticing, so there is none.
