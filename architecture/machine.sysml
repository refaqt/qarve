// Top-level SysML — machine requirements and composition.
// Formal requirements live here and in modules/*/architecture/ when sub-modules exist.

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
        doc /* Top-level machine composition — add sub-module parts when modules/ is populated */
    }
}
