function matrix_toggle_technique(tactic_id, technique_id) {
    var joined = tactic_id + "--" + technique_id;
    $(".subtechniques--" + joined).toggleClass("hidden");
    $(".sidebar--" + joined).toggleClass("expanded");
}

// set the state of the given technique
// state must be "open" or "closed"
function setMatrixCellState(tactic_id, technique_id, state) {
    if (state == "open") {
        var joined = tactic_id + "--" + technique_id;
        $(".subtechniques--" + joined).removeClass("hidden");
        $(".sidebar--" + joined).addClass("expanded");
    } else if (state == "closed") {
        var joined = tactic_id + "--" + technique_id;
        $(".subtechniques--" + joined).addClass("hidden");
        $(".sidebar--" + joined).removeClass("expanded");
    }
}

// switch tabs to the given matrix, param is either "flat" or "side"
function showMatrix(whichMatrix) {
    if (whichMatrix != "flat" && whichMatrix != "side") return;
    let otherMatrix = whichMatrix == "flat"? "side" : "flat";
    $("#" + whichMatrix + "-tab").addClass("active");
    $("#" + otherMatrix + "-tab").removeClass("active");

    $("#" + whichMatrix + "-layout").addClass("show active");
    $("#" + otherMatrix + "-layout").removeClass("show active");
}