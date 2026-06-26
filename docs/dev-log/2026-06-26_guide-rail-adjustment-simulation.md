# 2026-06-26 — Guide-rail adjustment simulation

## Goal

Evaluate whether a small bend in the linear guide rail can be corrected by
adjusting the preload of the screws that fix the rail, using a compliant layer
underneath the rail as the adjustment medium.

## Work Done

- Set up an FEM study in `simulation/guide-rail-adjustment/guide-rail-adjustment.FCStd`.
- Modelled a 5 mm POM layer underneath the guide rail that is compressed by the
  preloading of the rail-fixing screws.
- Used the screw preload to locally compress the POM layer so the rail can be
  straightened, simulating correction of a bend in the guide.

## Results

- Results captured in `simulation/guide-rail-adjustment/guide-rail-adjustment.FCStd`.
- The compliant POM layer allows the rail position to be adjusted via differential
  screw preload, supporting the concept of bend correction through preload tuning.

## Notes

- CalculiX solver scratch/output files (`FEMMeshGmsh.*`) are regenerable from the
  `.FCStd` and are excluded from version control via `.gitignore`.

## Next Steps

- [ ] Quantify achievable rail-straightness correction vs. screw preload range.
- [ ] Confirm POM creep/long-term compression does not relax the adjustment.
