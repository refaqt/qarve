# 2026-09-25 — Strip seal is thicker and bends on a larger radius

**Role(s):** engineering, cad

## What happened

Manual work in `cad/architecture/machine.FCStd`, body `Linear axis`, sketch `Sketch008`.

- The steel strip seal is now 0.25 mm thick instead of 0.1 mm.
- The strip no longer wraps tightly around the four rollers. Before, it bent around each
  roller at a radius of about 5 mm. Now it follows two S-curves, one on each side, with a
  bend radius of about 32 mm (32.13 mm on the inner face, 32.38 mm on the outer face).
- The flat top run is unchanged: from 47.7 mm to 170.7 mm, at 50 mm height.
- The four rollers keep their size (10 mm across) and their position.

Nothing else in the model changed. The model fingerprint was written again.

## A rough check on bending stress

Bending stress in the strip is about E × t / (2 × R), with E = 200 GPa for steel.

| | Thickness | Bend radius | Bending stress |
| --- | --- | --- | --- |
| Before | 0.1 mm | about 5 mm | about 2000 MPa |
| Now | 0.25 mm | about 32 mm | about 780 MPa |

The larger radius more than makes up for the thicker strip. The stress is less than half of
what it was. It may still be above the fatigue limit of spring steel, so it needs a proper check.

## Next Steps

- [ ] Check 780 MPa against the fatigue limit of the chosen strip material, for the planned
      number of cycles.
- [ ] Check that the S-curves still fit inside the profile with the 0.25 mm strip.
