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
    $(".layout-button.side").addClass("active");
    $(".layout-button.flat").removeClass("active");

    $(".matrix-type.side").removeClass("d-none");
    $(".matrix-type.flat").addClass("d-none");
}

function show_flat_matrix() {
    $(".layout-button.flat").addClass("active");
    $(".layout-button.side").removeClass("active");

    $(".matrix-type.flat").removeClass("d-none");
    $(".matrix-type.side").addClass("d-none");
}