# Usage graph

`usage-graph.json` is **generated** by `doqs/scripts/resolve_graph.py` and committed as a snapshot of which parents and builds reference each module.

```powershell
python doqs/doqs.py generate
```

To check that the committed file is still current, without writing it:

```powershell
python doqs/scripts/resolve_graph.py --check
```
