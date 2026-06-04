// Top-level SysML — imports module architecture and defines machine composition.
// Formal requirements live here and in module architecture/ folders only.

import '../modules/x-axis/architecture/x-axis.sysml'::XAxis::*;

package QarveMachine {

    requirement def WorkEnvelope {
        doc /* The machine shall provide a work envelope of at least 300 × 200 × 150 mm */
        attribute x_mm : Real;
        attribute y_mm : Real;
        attribute z_mm : Real;
        require constraint { x_mm >= 300.0 and y_mm >= 200.0 and z_mm >= 150.0 }
    }

    requirement def PositioningAccuracy {
        doc /* Repeatability shall be ≤ 0.05 mm on all axes */
        attribute repeatability_mm : Real;
        require constraint { repeatability_mm <= 0.05 }
    }

    part def Machine {
        doc /* Top-level machine composition — extend as modules are added */
        part xAxis : XAxis::LinearAxis;
    }
}
