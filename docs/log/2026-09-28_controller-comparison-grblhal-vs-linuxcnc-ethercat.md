# 2026-09-28 — Controller comparison: grblHAL and ncSender against LinuxCNC and EtherCAT

**Role(s):** engineering, firmware, software

## What happened

We compared the controller that Richner Precision uses with the controller we plan for Qarve.
The result: the Richner setup is simpler and cheaper, but it does not fit a 5-axis machine with
linear motors and linear encoders. LinuxCNC with EtherCAT stays our plan.

Richner Precision is a Swiss maker of CNC mills, routers, and lathes. Their RUIX router runs
**grblHAL** on a 32-bit controller board, with **ncSender** as the operator program.

- **grblHAL** is firmware on a small microcontroller board. The board reads the G-code, plans the
  moves, and sends step and direction pulses to the motor drives. It does all the timing work
  itself, so the PC does not need to be fast or real-time.
- **ncSender** is a "G-code sender". It runs on a desktop or in a browser. It sends the program to
  the board over USB or Ethernet and shows a 3D preview, jogging, probing, and tool management. It
  does not control motion. Its project page says it was only tested on one board (Sienci SLEB-EXT).

Our plan is different. **LinuxCNC** runs on the mini-PC with a real-time Linux kernel and does
the path planning and machine geometry. **EtherCAT** is an industrial network. Every
millisecond, the PC sends a target position to each drive and reads back the real position and
the drive status. The drives close the control loops locally.

| Topic | grblHAL + ncSender (Richner) | LinuxCNC + EtherCAT (Qarve plan) |
| --- | --- | --- |
| Where the timing work runs | Microcontroller board | Real-time Linux on the mini-PC |
| Link to the drives | Step and direction pulses, one way only | Digital network, both ways |
| Position feedback to the controller | None. The controller assumes every step happened | Real position every cycle, so it detects position errors |
| Linear motors with linear encoders | Only if the drive closes the loop on its own; the controller never sees the encoder | Good fit: the drive and the controller both see the encoder |
| 5-axis trunnion (A tilt, C table) | Rotary axes move, but no tool-tip control (RTCP). The CAM program must calculate everything for one fixed setup | Built-in trunnion geometry with tool-tip control |
| Tool changer, spindle, extra inputs and outputs | Plugins exist; a full tool changer needs custom work | Configured in LinuxCNC; the spindle drive and I/O can share the EtherCAT network |
| Hardware cost | Low: one board (about €100–300) and any PC | Mini-PC with good real-time behaviour, EtherCAT drives, EtherCAT I/O modules |
| Setup work | Low: flash the board and set parameters | High: real-time kernel, EtherCAT configuration, drive tuning |
| Operator screen | Clean and simple out of the box | Needs work to reach the same quality |

The board price is an estimate and must be checked before we use it in a quote.

## Decisions

- Keep LinuxCNC with EtherCAT as the planned controller. The reasons are the 5-axis trunnion
  (we need tool-tip control) and the linear motors on X, Y, and Z (the controller must see real
  positions to stop the machine after a crash or a lost position).
- Use ncSender as a model for our operator screen. Its one-screen workflow is its strongest point.

This is not yet a formal decision record. The design overview only says "mini-PC" for the
controller.

## Open Questions

- Is the Nanotec N5-2-1 in the bill of materials the EtherCAT version? The N5 family also comes
  with other network interfaces.
- Which mini-PC has a low and stable real-time delay, and a separate network port for EtherCAT?
- Which operator screen do we start from (for example Probe Basic or a custom QtVCP screen)?

## Next Steps

- Write a decision record in `docs/decisions/` for the controller choice.
- Confirm the N5-2-1 order code with Nanotec.
- Measure the real-time delay on candidate mini-PCs before we buy one.

## Sources

- [Richner-Precision homepage](https://richner-precision.ch/)
- [Richner RUIX-Router](https://richner-precision.ch/RUIX-Router/)
- [ncSender website](https://ncsender.xyz/)
- [ncSender on GitHub](https://github.com/siganberg/ncSender)
- [QARVE design overview](../../QARVE_Design_Overview_20260716.md) (drives and power section)
