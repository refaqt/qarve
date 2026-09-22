# 2026-09-22 — Linear axis reshaped for larger seal rollers

**Role(s):** engineering, cad

## What happened

- Reworked the linear axis layout in `cad/architecture/machine.FCStd` (body `Linear axis`)
  so that larger rollers for the steel strip seal fit inside the profile.
- The axis profile is now 210 mm wide instead of 195 mm.
- The two rail carriages moved 2.5 mm closer to the centre line each. Their spacing went
  from 133 mm to 128 mm.
- Together these two moves give 14 mm of free space between the outer wall and each rail
  carriage, instead of 4 mm before.
- The seal pocket on both sides of the profile was redrawn. It is now about 13 mm wide and
  9.7 mm high, with a lip at the top edge and a reference point for the roller position.
- The drive block in the middle keeps its 86 mm width and is centred on the new middle
  line at 105 mm.
- The machine footprint, enclosure, boundary and both rotary-axis sketches were not touched.

## Next Steps

- [ ] Choose the roller diameter and the roller supplier, then lock it in the parts list.
- [ ] Check whether the 15 mm of extra width changes the machine footprint and the enclosure.
- [ ] Update `architecture/machine.sysml` if the wider axis changes the work envelope.
