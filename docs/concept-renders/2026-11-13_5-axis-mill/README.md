# 5-axis milling machine — concept renders (2026-11-13)

These are concept pictures of a 5-axis milling machine built from AQTUATOR CS linear stages. The
founder drew the layout and gave the sizes in two sketches. We then checked the 3D picture
together in six rounds on 13-11-2026. The pictures are a concept, not a finished design. No
FreeCAD model exists yet.

## Files

| File | What it is |
| --- | --- |
| `mill-full.png` | The whole machine on its stand |
| `mill-close.png` | The work area: cradle, turning table, spindle, front plate |
| `mill-chip-pocket.png` | The cradle tilted back, to show the chip pocket under it |
| `sketch-1-machine.webp` | Founder sketch 1: the machine and the axes |
| `sketch-2-front-view.webp` | Founder sketch 2: front view with the sizes |
| `render-machines.html` | Copy of the model that draws the pictures (three.js) |

## The machine

- **Size:** machine 560 mm wide and 760 mm deep, on a stand of 600 × 800 mm. The stand is a
  black steel tube frame with cover plates and a door. It holds the chip bin.
- **Body:** walls of 100 mm (80 mm aluminium profile between two 10 mm plates), all black
  anodised. A 10 mm front plate has the opposite shape of the cradle, with 10 mm space.
- **Y axis:** two CS-520 stages, on their edge on top of the side walls.
- **X axis:** one CS-220 stage, bolted to the front of a 160 mm beam between the two Y carriages.
  Together they look like one 200 mm thick beam.
- **Z axis:** one CS-220 stage inside a closed column. A solid ram carries the 80 mm spindle.
- **A axis:** a cradle that turns around X. Its rotary stage is 210 mm across and sits in the
  right wall, with its edge 20 mm from the front. A bearing sits in the left wall.
- **C axis:** a turning table that lies on the cradle bottom. Its drive is inside the cradle.
- **Width, left to right:** wall 100 | cradle side 20 | 10 | spindle 80 | X travel 220 | 10 |
  cradle side 20 | wall 100 = 560 mm.
- **Height, from the machine bottom:** bottom part 180 | 10 | cradle bottom 100 | cradle sides
  up to 10 mm under the Y stages.
- **Chips:** a large pocket under the cradle has four slopes. They lead the chips through a
  hole into the bin in the stand.
- **Light:** a green LED strip on the back plate, right under the Y axis.

## How to draw the pictures again

The copy of `render-machines.html` here needs files from the website repository, so it does not
run on its own. The working version is in `refaqt/refaqt-web`, file
`tools/render-machines.html`, on branch `claude/eager-cannon-fwsggr` (commit `c6f8bab`). The
machine is the `mill()` function. In the root of `refaqt-web`, run:

```bash
python3 -m http.server 8765
```

```bash
ONLY=mill node tools/render_machines.cjs
```

Add `CAM=x,y,z` to choose the camera position, and `TILT=1.4` to tilt the cradle (radians).
