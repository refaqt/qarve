# QARVE — Compact 5-Axis CNC Milling Machine: Design Overview

*Reference summary derived from `QARVE__Architecture_Calculations_BOM__20260716.xlsx` (preliminary design, updated 2026-07-16). This document is a navigation aid for the project: it summarizes the concept, kinematics, key calculated numbers, the major components and their suppliers, and known data-quality caveats so that questions can be answered without re-reading the full workbook. Changes versus the prior 2026-06-18 revision are noted inline (the X-axis linear-motor peak-force shortfall is now resolved; the BOM was reorganized and the machine total is lower).*

---

## 1. What QARVE is

QARVE is a **compact, table-tilting 5-axis CNC milling machine** intended to sit on roughly **half a EUR pallet**. The three linear axes (X, Y, Z) position the spindle/tool, and two rotary axes (A, C) orient the workpiece on a **trunnion (cradle) rotary table**. It is built largely from **aluminium extrusion** and uses **direct-drive linear motors** on the linear axes and **frameless torque motors** on the rotary axes.

The design is captured in a single workbook that combines a **parametric system model** (cutting physics → axis loads → motor/component sizing), a **bill of materials with architecture tree**, and a **supplier/specification comparison** that checks each chosen component against the model's requirements.

### Headline figures

| Item                       | Value                                                                                                                                                                                                                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Axes                       | 5 — X, Y, Z (linear) + A, C (rotary)                                                                                                                                                                                                                                                                                |
| Linear travels             | X = 310 mm · Y ≈ 356 mm total (≈256 mm machining + 100 mm tool change) · Z = 222 mm                                                                                                                                                                                                                                 |
| Max workpiece              | Ø230 mm × 210 mm tall; ≈163 × 163 mm if square; **15 kg** max                                                                                                                                                                                                                                                       |
| Target machine footprint   | ≤ 600 mm (X, ½ EUR-pallet length) × 800 mm (Y, EUR-pallet width)                                                                                                                                                                                                                                                    |
| Spindle                    | Jianken JGY-80/3.2R24-encoder, PMSM, **ISO20**, up to ~30,000 rpm                                                                                                                                                                                                                                                   |
| Materials targeted         | Aluminium 6061, Stainless 304L, Titanium Ti-425 (roughing + finishing each)                                                                                                                                                                                                                                         |
| Finishing stiffness target | ≤ **2 µm** deflection at ≈95 N finishing force                                                                                                                                                                                                                                                                      |
| Indicative total BOM cost  | ≈ **€21,029** (Parts/Architecture roll-up, EUR). Note: this **excludes the Accessories block (A21, ≈€2,820)**, which is defined but currently detached from the machine tree — see §7–8. With accessories re-attached the effective total is ≈**€23,850**. See §8 for the one USD-quoted line and how it's handled. |

---

## 2. Kinematics & axis architecture

QARVE is a **moving-gantry / tilting-table** configuration:

- **Gantry** spans the work zone on two **80 mm support columns**; the gantry beam is ~530 mm long.
- **X axis** — the spindle carriage traverses *along* the gantry beam (310 mm travel).
- **Y axis** — motion along the machine frame (≈356 mm total travel; frame length in Y ≈760 mm).
- **Z axis** — vertical spindle motion (222 mm), counterbalanced by gas springs.
- **A axis** — the **trunnion/cradle tilt** that swings the rotary table; carries the largest rotary load (heavy, eccentric — see §4).
- **C axis** — the **rotary worktable** (circular T-slot table) seated in the cradle.

> **Naming note (updated):** In the 2026-07-16 workbook the *Groups* sheet now labels the rotary-table group **G05 as "Axis C"**, consistent with Parts/Architecture. The earlier "Axis B (G05)" discrepancy is resolved. A = tilt, C = table rotation.

All three linear axes share a common motion architecture: HIWIN profile rail + blocks, an iron-core linear motor (Saho **WJM50-3** — new selection this revision, see §4), a linear encoder for feedback, bellows covers, end stops, limit sensors, and shock dampers. Both rotary axes share: a frameless torque motor, roller bearings, bearing/motor housings, a rotor disk, and a rotary encoder.

---

## 3. Cutting capability & the system model

The "System model" sheet is the parametric heart of the workbook. For each **material × operation** it sets cutting parameters and tool geometry, then computes forces, torque, power and required dynamics. Cases modelled:

| Case                        | Tool (Hans Treiber) | Ø     | Flutes | vc (m/min) | Spindle (rpm) | Cutting power (W) | Spindle torque (Nm) | Resultant cut force (N) |
| --------------------------- | ------------------- | ----- | ------ | ---------- | ------------- | ----------------- | ------------------- | ----------------------- |
| Aluminium 6061 — roughing   | RG28-88RZ (N 1.2)   | 10 mm | 3      | 620        | ~19,700       | ~1,491            | 0.72                | ~192                    |
| Aluminium 6061 — finishing  | HP-AL3L-DLC (N 1.2) | 6 mm  | 3      | 450        | ~23,900       | ~236              | 0.094               | ~42                     |
| Stainless 304L — roughing   | RG26-48TZ (M 2.1)   | 10 mm | 4      | 130        | ~4,140        | ~325              | 0.75                | ~201                    |
| Stainless 304L — finishing  | RG26-44T (M 2.1)    | 6 mm  | 4      | 120        | ~6,370        | ~115              | 0.17                | ~77                     |
| Titanium Ti-425 — roughing  | RG26-48TZ (S 1.2)   | 10 mm | 4      | 100        | ~3,180        | ~239              | 0.72                | ~192                    |
| Titanium Ti-425 — finishing | RG26-48TZ (S 1.2)   | 6 mm  | 4      | 100        | ~5,310        | ~118              | 0.21                | ~95                     |

Material cutting coefficients used: aluminium Kc1.1 = 800 MPa (mc 0.25); stainless Kc1.1 = 2150 MPa (mc 0.20); titanium Kc1.1 = 2110 MPa (mc 0.22). Target metal-removal rate (MRR) for aluminium roughing is 50 cm³/min.

The model uses a chip-thinning / energy-weighted Kc approach (radial chip-thinning factor, average Kc at max chip thickness) to derive **tangential, feed, transverse and axial forces**, and from those the **spindle torque/power** and the **per-axis acceleration forces**. The governing worst case for sizing the linear axes and rotary process force is **≈201 N resultant cutting force** (stainless/titanium roughing); the **finishing** worst case (~95 N, titanium) drives the **2 µm stiffness** requirement.

> Two trailing sheets — *"Oblique cutting constants (not used)"* and *"Cutting force model (replaced w…)"* — are **deprecated**. The oblique-cutting table holds representative orthogonal constants that the notes say were *not* used; the old cutting-force model sheet is full of `#REF!` errors and has been superseded by the per-case calculations in "System model." Treat both as historical, not authoritative.

---

## 4. Motor & drive sizing (calculated requirements → selected hardware)

### Linear axes (X / Y / Z)

- Peak per-axis acceleration ≈ 19.1 m/s² (feed) / 13.9 m/s² (rapids); rapid speed 5,000 mm/min.
- Continuous motor force required ≈ **201 N**; peak force required ≈ **418 N (Z) / 479 N (Y) / 565 N (X)** — X remains the worst case at **564.8 N**.
- **Selected (changed this revision):** Saho **WJM50-3** forcer (200 mm, force constant 52.2 N/A, 240 N continuous, **750 N peak**, 4.6 A cont., 600 V, 139.7 W thermal @100 °C) on Saho **DJM050** stators (DJM050-L80 + DJM050-L200). Forcer unit cost ≈€101 (vs ≈€172 for the old WKM030-2), which is the main reason the X/Y/Z assembly costs dropped (§7).
- ✅ **Open issue RESOLVED:** with the WJM50-3's **750 N peak** rating, the X-axis peak-force requirement (564.8 N) now passes with margin. **All linear-motor spec lines are TRUE** in this revision. (The previously selected Saho WKM030-2 — 532 N peak, 106 W thermal, 4.5 A — failed on peak force, continuous current, force constant, resistance and thermal power, and is now the rejected alternative.)
- ⚠ Note the trade: WJM50-3 continuous thermal dissipation is **139.7 W** per forcer (vs 106 W for the old part), raising per-axis and total machine heat (see below) — worth watching for natural-cooling margin, though continuous force (201 N) sits well under the 240 N continuous rating.

### Rotary axes (A / C)

- A-axis (trunnion) continuous torque required ≈ **27.7 Nm** (dominated by the eccentric centre-of-gravity of the cradle, ~31.4 Nm static term, plus eccentric workpiece up to ~4.6 Nm and process torque).
- C-axis (table) continuous torque required ≈ **23.1 Nm**.
- **Selected:** **Mosrac U16060** frameless torque motor (torque constant 1.6 Nm/A, 32 Nm continuous, 45 A peak, 48 V DC, 0.96 Nm cogging, 0.24 Ω) — unchanged; all spec lines pass. Unit cost rolled in ≈€520 (USD-quoted supplier line, see §8). Resistive heaters appear on the A-axis (thermal conditioning).
- Alternatives evaluated but rejected: Mosrac U20060, and Seninter/3Phis DDM140050-PM and DDM140070-PM (the DDM140050-PM fails several lines — torque constant 9.9 vs 1.6 Nm/A, continuous/instant current, and 380 V vs 48 V DC-voltage mismatch).

### Drives & power

- **Servo drives:** Nanotec **N5-2-1** (one per motion axis; 6 listed in the BOM, ≈€363 each rolled).
- **Spindle drive:** **Cumark ES850S-02-4K0G-encoder** VFD (≈€327), matched to the encoder spindle for closed-loop / constant-torque-at-low-speed operation.
- **Power:** 48 V / 500 W supply + 12 V supply; per-motor fuses, overcurrent protection, differential breaker; a **mini-PC** acts as the controller.
- Estimated **max continuous machine heat ≈ 171 W** (up from ≈159 W, driven by the higher-dissipation linear forcers); A-axis still dominates at ~72 W (C ~50 W, X ~49 W, Y ~49 W, Z ~27 W).

---

## 5. Spindle

- **Selected (model designation updated):** Jianken **JGY-80/3.2R24-encoder** — a permanent-magnet synchronous-motor spindle, 80 mm body, **ISO20** tool interface, ~10 kg (12 kg with mount), 8.6 A. This revision selects the **encoder-equipped** variant (closed-loop, constant torque at low speed), rolled in at **≈€1,378** (the plain JGY-80/3.2R24 without encoder was ≈€1,178). The earlier "JGY-80/3.7R24" designation is now a listed alternative with no confirmed price.
- Requirement checks all pass: needs ≥3,200 W rated (model needs ~1,657 W), ≥1.32 Nm (needs 0.75 Nm), reach the ~23,900 rpm finishing speed (spindle goes to ~30,000 rpm), runout ≤5 µm (spindle 3 µm), ISO20 match, 8.6 A.
- Paired VFD: **Cumark ES850S-02-4K0G-encoder** (≈€327).
- Spindle rigidity at the tool tip is taken as ~47 N/µm.
- **Alternatives evaluated:** HSD ES330 (€3,500), Teknomotor ATC71-A-ISO30 (€3,500), Hiteco QE-1F (€4,045) / QD-1F (€3,495), and the cheaper Jianken JGL-80/2.2R30. The encoder JGY unit was chosen as the best cost/performance fit.

---

## 6. Structure, precision & enclosure

- **Frame & base:** aluminium extrusion — 80×80 profiles (large), 40 mm (small). The base uses ~17× 80×80×1000 extrusions plus support feet, chip bin, doors and covers; the frame uses 80×80×600 extrusions plus laser-cut side/front/back/inner plates and rubber feet.
- **Gantry beam:** aluminium, area moment of inertia 4,202,400 mm⁴ (from the Misumi catalog), E = 69,000 MPa → ~**374 N/µm** stiffness for a centre point load (clamped-clamped, rails not included).
- **Precision target:** ≤ **2 µm** total machine deflection during finishing at the ~95 N finishing force; tool-tip spindle rigidity ~47 N/µm.
- **Enclosure/housing:** 15 mm enclosure walls with 5 mm clearance to the machine; housing side panels, extrusion sub-frame and a door.

---

## 7. Bill of materials & sub-systems

The **Parts** sheet defines the assemblies (`A01…A21`) and parts (`P01…P82`); **Architecture** is the parent→child tree that rolls quantities and costs up to the top-level assembly **QARVE (A01)**.

**BOM reorganization this revision (read before quoting the total):** the top-level tree was restructured. The **tool setter (P75)**, **wireless touch probe (P76)** and a new **Lighting (P82)** item were promoted to *direct* children of QARVE (A01), and **Control panel (A12)** is now a direct A01 child. Crucially, the **Accessories assembly (A21)** — 12× ISO20 tool holders (€1,800), a **vise set** (€300) and a 12-piece **tool set** (€720), €2,820 total — is **defined but no longer attached to A01**, so it is **not rolled into the machine total**. This is most likely an unintended orphan from the restructure (the probe/setter were moved out of A21 to A01 but the remaining accessories were left detached); flag it before treating €21,029 as the all-in cost.

Direct children of QARVE (A01) and their rolled costs (EUR, as recorded in the workbook):

| Assembly / part                        | Rolled cost (€) | Notes                                                              |
| -------------------------------------- | --------------- | ------------------------------------------------------------------ |
| X-axis (A02)                           | 1,920           | linear motor (WJM50-3) + HIWIN guides + encoder + extrusion        |
| Y-axis (A03)                           | 1,654           | two forcers (longer travel)                                        |
| Z-axis (A04)                           | 1,020           | + gas-spring counterbalance                                        |
| A-axis (A05)                           | 1,990           | trunnion: torque motor, bearings, cradle plates, heaters           |
| C-axis (A06)                           | 1,960           | rotary T-slot table, torque motor, bearings                        |
| Spindle assembly (A07)                 | 1,778           | spindle + bracket + Cumark VFD                                     |
| Frame (A08)                            | 1,980           | extrusion + plates                                                 |
| Base (A09)                             | 2,260           | extrusion, doors, chip bin                                         |
| Housing (A10)                          | 380             | panels + door                                                      |
| Electronic system (A11)                | 3,477           | drives, PSUs, protection, mini-PC, cabinet                         |
| Control panel (A12)                    | 700             | now a direct A01 child                                             |
| Tool coolant system (A13)              | 350             | **MQL** (minimum-quantity lubrication)                             |
| Pneumatic system (A14)                 | 600             | compressor, filter, valve, components                              |
| Tool cabinet (A15)                     | 760             | manual tool storage (tool array holders)                           |
| Tool setter (P75)                      | 50              | promoted to direct A01 child                                       |
| Wireless touch probe (P76)             | 150             | promoted to direct A01 child                                       |
| Lighting (P82)                         | 0               | new line, placeholder cost                                         |
| **QARVE total (A01)**                  | **≈ 21,029**    | top-level roll-up (**excludes** detached Accessories A21)          |
| *Accessories (A21) — detached*         | *2,820*         | *vises, tool set + 12 holders; not in the A01 total this revision* |
| *Effective total with A21 re-attached* | *≈ 23,849*      | *if the orphan is intended to be included*                         |

**Accessories & metrology:** a **wireless touch probe** and a **tool setter** (now direct machine sub-assemblies); a **vise set** (low-profile vise + dedicated 5-axis vise); a **tool set** of 12 tools on 12 ISO20 tool holders stored in the tool cabinet (no automatic tool changer — tool change uses the 100 mm Y allowance and the cabinet). The vise set, tool set and tool holders sit under the currently-detached A21 assembly.

### Key suppliers (selected)

- **Sorotec** (DE) — tool holder (ISEL SK20), HIWIN linear guide rails (HGR20) and blocks (HGH20CA).
- **Saho** — linear motor forcers and stators (**WJM50-3** forcer + **DJM050-L80 / DJM050-L200** stators; changed from WKM030-2 / DKM030 this revision).
- **Sino** — linear encoders (KA-500 series).
- **Nanotec** — N5-2-1 servo drives.
- **Mosrac** — U16060 frameless torque motors.
- **Jianken** — **JGY-80/3.2R24-encoder** spindle, with a **Cumark ES850S** VFD.
- **Hans Treiber / fraeser-shop** — solid-carbide end mills (the tools in §3).

---

## 8. Data-quality caveats (read before quoting numbers)

1. **Cost reconciliation error (persists).** The *Groups* sheet still flags **"ERROR: double-counted — an assembly…"**. The sum of the per-group costs (now ≈**13,426**, down from ≈14,452) does **not** equal the top-level QARVE cost (≈21,029); the difference is partly un-grouped systems (frame, base, housing, electronics, coolant, pneumatics, tool cabinet, control panel, probe/setter) and partly a flagged double-count (servo drives are children of the Electronic system yet also tagged to axis groups). The reconciliation's "top-level (root) cost" cell also reads 0 because its `SUMIFS` matches `type="assembly"` (lower-case) while Parts stores `"Assembly"` — a case-mismatch that leaves the check permanently in the error state. **Use the Parts/Architecture roll-up (≈21,029) as the machine total**, and treat group subtotals with caution.
2. **Detached Accessories block (new this revision).** Assembly **A21 (Accessories, €2,820)** is defined but **not a child of A01**, so it is excluded from the €21,029 roll-up (see §7). The tool setter and touch probe were promoted to direct A01 children, but the vise set, tool set and 12 tool holders were left orphaned — most likely unintended. If accessories belong in the machine cost, the effective total is ≈**€23,849**. Decide and re-attach (or confirm the exclusion is deliberate) before quoting a single "machine cost".
3. **Currency — confirmed EUR.** All BOM/unit costs in the workbook are EUR. One supplier line is quoted in USD — the Mosrac U16060 torque motor (Suppliers note: *"2pcs: 520USD/pcs, 20pcs:480USD/pcs, …"*). This revision converts it **live** via `GOOGLEFINANCE("CURRENCY:USDEUR")` (cached ≈0.87 EUR/USD, giving ≈€478.6 at the 2-piece break, plus a small handling term); the unit cost actually rolled into the total (**≈€520.4**) comes from a power-law curve fit across the quantity breaks evaluated at the machine quantity. Either way the figure is in EUR terms, so the ≈€21,029 total is not understated by an unconverted USD amount. No other USD lines exist in the workbook.
4. **X-axis peak force — RESOLVED.** The linear motor was changed from Saho WKM030-2 (532 N peak, which failed the 564.8 N requirement) to Saho **WJM50-3 (750 N peak)**; all linear-motor spec lines now pass (§4). This caveat from the prior revision is closed. Watch item: WJM50-3 thermal dissipation is higher (139.7 W vs 106 W per forcer), nudging total machine heat to ≈171 W.
5. **Deprecated sheets.** "Oblique cutting constants (not used)" and "Cutting force model (replaced w…)" are historical; the latter still contains thousands of `#REF!` cells. Don't rely on them.
6. **Preliminary status.** This is a *preliminary* design updated 2026-07-16; numbers are model outputs and supplier quotes, not as-built measurements.

---

## 9. Workbook map (where to find what)

| Sheet                         | Contents                                                                                                                                              |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System model**              | Parametric calculations: per-material cutting cases, axis loads, motor sizing, geometry/travel, thermal. The single source of truth for requirements. |
| **Parts**                     | Flat list of every assembly/part with type, supplier flag, unit & rolled cost, quantity.                                                              |
| **Architecture**              | Parent→child BOM tree; rolls quantities/costs up to QARVE (A01); assigns axis groups.                                                                 |
| **Groups**                    | Per-group (axis) cost subtotals + the cost reconciliation check (still flagging an error; group sum ≈13,426). G05 now labelled "Axis C".              |
| **Suppliers**                 | Candidate suppliers per part with model numbers, links, price breaks, and the "chosen supplier" flag.                                                 |
| **Specifications**            | Each candidate component's specs checked against the model's requirement (OK? column).                                                                |
| **Tools**                     | End-mill catalog (brand, geometry, cutting speed, feed-per-tooth, ae) used by the cutting cases.                                                      |
| **Material constants**        | Kc1.1 / mc lookup by material and material group.                                                                                                     |
| **Oblique cutting constants** | *Deprecated / not used.*                                                                                                                              |
| **Cutting force model**       | *Deprecated / replaced;* contains `#REF!` errors.                                                                                                     |
