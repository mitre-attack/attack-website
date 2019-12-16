function matrix_toggle_technique(tactic_id, technique_id) {
    var joined = tactic_id + "--" + technique_id;
    $(".subtechniques--" + joined).toggleClass("hidden");
    $(".sidebar--" + joined).toggleClass("expanded");
}

function matrix_toggle_all(visible) {
    if (visible) {
        $(".sidebar").addClass("expanded");
        $(".subtechniques-container").removeClass("hidden");
    } else {
        $(".sidebar").removeClass("expanded");
        $(".subtechniques-container").addClass("hidden");
    }
}

function show_side_matrix() {
    $(".matrix-type.side").removeClass("d-none");
    $(".matrix-type.flat").addClass("d-none");
}

function show_flat_matrix() {
    $(".matrix-type.flat").removeClass("d-none");
    $(".matrix-type.side").addClass("d-none");
}