# 2026-08-28 — Taiwanese ATC spindle supplier research

## Goal

Identify Taiwanese spindle suppliers and catalog models matching Qarve spindle requirements:

| Criterion | Requirement |
|-----------|-------------|
| Tool interface | ATC; ISO20 or larger, or HSK |
| Power | > 1.1 kW |
| Min speed | < 3000 rpm (low-speed capability) |
| Max speed | > 23,000 rpm |
| Torque | > 0.94 Nm |

## Work Done

- Searched public catalogs and datasheets for Taiwan spindle manufacturers.
- Mapped published models against power, speed range, torque, taper, and ATC capability.
- Flagged gaps where min speed or torque are not published online.

**Note:** Min speed < 3000 rpm is the binding constraint. Many Taiwan high-frequency (HF) built-in spindles publish minimum speeds of 6,000–10,000+ rpm. For ISO20-class spindles, verify low-speed torque and cooling with the vendor before selecting.

## Suppliers and candidate models

### 1. 普慧 Parfaite Tools — Taichung area

Website: https://parfaite.com/

| Model | Taper | Power | Torque | Speed range | Meets spec? |
|-------|-------|-------|--------|-------------|-------------|
| [EIA0820-30](https://parfaite.com/en/product/eia0820-30/) | ISO20 | 2.0 kW | 1.1 Nm | 10,000–30,000 rpm | Min speed too high |
| [EIA0845-50](https://parfaite.com/en/product/eia0845-50/) | ISO10/15T/HSK25E | 4.5 kW | 1.1 Nm | 20,000–50,000 rpm | Min speed too high |
| [MIA1275-24](https://parfaite.com/en/product/mia1275-24/) | BT30 / HSK40E | 7.5 kW | 6.0 Nm | 6,000–24,000 rpm | Max OK; min speed high |
| [MIA1291-30](https://parfaite.com/en/product/mia1291-30/) | HSK40E / BT30N | 9.1 kW | 6.5 Nm | 7,500–30,000 rpm | All except min speed |

Best Parfaite pick for ISO20 + torque: **EIA0820-30** — only misses low-speed requirement on paper.

### 2. 矩將科技 MicroLab — Taichung

Website: https://www.twspindle.com/  
Contact: microlab@twspindle.com · +886-4-22392345

| Model | Taper | Power | Max rpm | ATC | Notes |
|-------|-------|-------|---------|-----|-------|
| [M2-QMS](https://www.twspindle.com/zh-TW/product/built-in-motor-high-speed-spindle-diameter-80_M2-QMS.html) | ISO20 | 2 kW | 36,000 | Pneumatic | Torque/min speed not published — RFQ |
| M25-GMSA / M25-GMSA-FG | ISO25 | 3.7 kW | 30,000 | Pneumatic/oil | Same |
| H3-GMSA-FG | HSK32E | 3.7 kW | 24,000 | Pneumatic | HSK option |

Good candidate for compact ISO20 ATC (Ø80); confirm VFD low-speed torque with vendor.

### 3. 釸達精密 Theta Precision — Taichung (Dayi)

Website: https://www.theta-spindle.com/

| Model | Taper | Power | Torque (S1) | Max rpm | ATC |
|-------|-------|-------|-------------|---------|-----|
| TH-80.02 | ISO20 | 2.5 kW | **0.7 Nm** | 40,000 | Tool sensors; confirm ATC |
| [TH-100.03](https://www.theta-spindle.com/en/products/th-100-03-3kw-iso-25-30-000rpm-model) | ISO25 | 3 kW | 2.4 Nm | 30,000 | Confirm ATC |
| [TH-100.03](https://www.theta-spindle.com/en/products/th-100-03-3kw-hsk-e32-40-000rpm-model) | HSK-E32 | 3 kW | 2.4 Nm | 40,000 | Confirm ATC |
| [TH-120.03](https://www.theta-spindle.com/en/products/th-120-03-4-6kw-hsk-e40-36-000rpm-model) | HSK-E40 | 4.6 kW | 4.5 Nm | 36,000 | Confirm ATC |
| [TH-120.15](https://www.timtos.com.tw/en/product/D2652059A509F0CCD929D219C19DC84A3E250D31F8B64F7C/info.html) | HSK-E40 | 7.5 kW | 5.9 Nm | 40,000 | ATC standard |

TH-80.02 **fails torque** (0.7 Nm S1). HF base speed typically ~9,700–11,700 rpm; low-speed operation below 3000 rpm unlikely without field weakening.

### 4. 恩德 Anderson Group — Taiwan

Website: https://spindle.anderson.com.tw/

Best documented option for wide speed range on integrated machines (e.g. HSK-63F at **1,000–22,000 rpm**). PMSM line advertises high torque at low speed.

| Model (ATS series) | Taper | Power | Max rpm | Notes |
|--------------------|-------|-------|---------|-------|
| AST80L-I20-P | **ISO20** | 4 kW | 40,000 | PMSM; ATC; ask min speed & torque |
| AST80L-E25-P | HSK-E25 | 4 kW | 50,000 | Same |
| AST100L-E32-P | HSK-E32 | 15 kW | 36,000 | Same |
| AST120L-E40-P | HSK-E40 | 20 kW | 30,000 | Same |
| AST150L-F63-P | HSK-F63 | 20 kW | 24,000 | Used on machines at 1000+ rpm min |

Best Anderson pick for full envelope: **AST80L-I20-P** (ISO20) or **AST80L-E25-P** (HSK).

### 5. Spintrue Tech — Taiwan

Website: https://www.spintrue-spindle.com/

Machine-tool grade; HSK-E40 and up (no ISO20 in standard catalog). Custom ODM available.

| Model | Taper | Power | Torque | Max rpm |
|-------|-------|-------|--------|---------|
| CB34C (CB0 series) | HSK-E40 | 4.6 kW | 6 Nm | 30,000 |

### 6. KENTURN — Changhua (est. 1983)

Website: https://www.kenturn.com.tw/

Large machining-center spindles; HSK-E40+ built-in motors. No ISO20 in public catalog; custom possible.

| Model | Taper | Power | Max rpm |
|-------|-------|-------|---------|
| MVB0925 | BBT30 (HSK-E40 category) | 10 kW | 24,000 |
| GVB0520 | ER16 only | 2 kW | 24,000 |

### 7. Paul Jet Hitechnology Corp. — Taiwan

Listed on [MachineTo](https://www.machineto.com/spindle-th-series-pauljet-10154773) with TH series nearly identical to Theta naming (TH-80 ISO20, TH-100 HSK-E32, etc.). Treat as related/OEM channel; cross-check specs with Theta.

## Models that clearly miss one requirement

| Model | Issue |
|-------|-------|
| Theta TH-80.02 (ISO20) | Torque 0.7 Nm < 0.94 Nm |
| Parfaite EIA0827-40 (ISO20) | Torque 1.0 Nm (borderline) |
| Parfaite EIA0820-30 | Min speed 10,000 rpm |
| Theta TH-170.09 (HSK-A63) | Oversized (18.5 kW) though max 24,000 rpm OK |

## Contact priority

| Priority | Supplier | Rationale |
|----------|----------|-----------|
| 1 | Parfaite | Best published ISO20 ATC data (EIA0820-30 hits power/torque/max speed) |
| 2 | Anderson | Best bet for min speed < 3000 rpm with HSK/ISO20 PMSM spindles |
| 3 | MicroLab | Compact ISO20 ATC (Ø80/Ø100); needs torque + min-speed confirmation |
| 4 | Theta | Strong HSK-E32/E40 ATC line if HF min-speed limits acceptable |
| 5 | Spintrue / Kenturn | If stepping up to HSK-E40+ for machining-center class |

## RFQ questions for vendors

1. Minimum continuous speed (not just base frequency speed)
2. Torque at 1000 / 2000 / 3000 rpm (not only at rated power point)
3. ATC interface (drawbar, tool-present sensors, magazine compatibility)
4. Cooling (water/oil) and controller (VFD vs FANUC/closed-loop)
5. Lubrication (grease vs oil-air) — affects max rpm

## Open Questions

- [ ] Is ISO20 mandatory, or are HSK-E32/E40 acceptable?
- [ ] Router-class (VFD) vs machining-center-class (FANUC/closed-loop) spindle?
- [ ] Confirm min speed < 3000 rpm is required for tapping/drilling vs. preference

## Next Steps

- [ ] Shortlist 2–3 models after taper and machine-class decision
- [ ] Send RFQ to Parfaite and Anderson first
- [ ] Capture selected spindle in SysML / BOM when part number is chosen
