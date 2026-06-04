package XAxis {

    requirement def TravelRequirement {
        doc /* X-axis travel shall be ≥ 300 mm */
        attribute travel_mm : Real;
        require constraint { travel_mm >= 300.0 }
    }

    port def FrameMountInterface_v1 {
        doc /* 4× M6 holes on 80×120 mm pattern, top surface — scaffold */
    }

    port def XAxisOutputInterface_v1 {
        doc /* Tool/spindle mounting face on the carriage */
    }

    part def CarriagePlate {
        attribute material : String = "6061-T6 aluminium";
        attribute thickness_mm : Real = 8.0;
    }

    part def LinearAxis {
        attribute travel_mm : Real;
        attribute repeatability_mm : Real;
        part carriage : CarriagePlate;
        port mount_to_frame : ~FrameMountInterface_v1;
        port carriage_face : XAxisOutputInterface_v1;
    }
}
