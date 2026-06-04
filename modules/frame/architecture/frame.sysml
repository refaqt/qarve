package Frame {

    port def FrameMountInterface_v1 {
        doc /* 4× M6 holes on 80×120 mm pattern, top surface — scaffold */
        attribute hole_pattern : String = "M6x4, 80x120 grid";
        attribute load_kg : Real = 50.0;
    }

    part def Frame_v1 {
        port mount : FrameMountInterface_v1;
    }
}
