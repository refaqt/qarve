# 2026-09-22 — Linear axis reworked around the steel strip seal

**Role(s):** engineering, cad

## What happened

Two rounds of manual work in `cad/architecture/machine.FCStd`, body `Linear axis`.

### Round 1 — more room inside the profile

- The axis profile is now 210 mm wide instead of 195 mm.
- The two rail carriages moved 2.5 mm closer to the centre line each. Their spacing
  went from 133 mm to 128 mm.
- Together this gives 14 mm of free space between the outer wall and each rail
  carriage, instead of 4 mm before.
- The drive block in the middle keeps its 86 mm width and sits on the new centre
  line at 105 mm.

### Round 2 — the seal itself

- The top of the base is now closed. The steel strip seal is drawn lying across it:
  170.5 mm long and 0.1 mm thick, held by a lip at each end.
- The side walls moved. Their inner faces are now at 23 mm and 187 mm, instead of
  10 mm and 200 mm. The outer faces sit at 0 mm and 210 mm.
- The bottom corners of the base got a relief, 11.5 mm wide and 5 mm high.
- The seal pocket drawn in round 1 is gone. The strip now runs over the closed top
  instead of inside a side pocket.
- New parts on the left inner wall only: a plate 0.4 mm thick and 8 mm tall, and a
  block 10 mm wide and 13.5 mm tall with chamfered corners.
- The four seal rollers are now 10 mm and 9.8 mm across, instead of 14 mm and
  13.8 mm. The two outer rollers moved 2 mm further apart and 2 mm down. The two
  inner rollers moved 2 mm up. The strip now runs a flatter path.

The machine footprint, enclosure, boundary, top view and both rotary-axis bodies
were not touched. The overall size of the linear axis stayed 210 mm by 60 mm.

## Open question

The stated goal was to fit **larger** rollers. The drawing now shows **smaller**
rollers. Confirm which diameter is the one we build.

## Next Steps

- [ ] Confirm the roller diameter, then pick the supplier and add the roller to the parts list.
- [ ] Name the two new parts on the left inner wall, so the drawing is readable.
- [ ] Check whether the 15 mm of extra width changes the machine footprint and the enclosure.
- [ ] Mirror the new left-side parts to the right side, if the design needs them on both sides.
