if (document.getElementById("layout-options")) {
    load_saved_layout();
}

function matrix_toggle_technique(tactic_id, technique_id) {
    var joined = tactic_id + "--" + technique_id;
    $(".subtechniques--" + joined).toggleClass("hidden");
    $(".sidebar--" + joined).toggleClass("expanded");
}

// set the state of the given technique
// state must be "open" or "closed"
// if tour is true, affects the sub-technique tour technique, ignoring the technique and tactic params
function setMatrixCellState(tactic_id, technique_id, state) {
    if (state == "open") {
        var joined = tour? 'tour' : tactic_id + "--" + technique_id;
        $(".subtechniques--" + joined).removeClass("hidden");
        $(".sidebar--" + joined).addClass("expanded");
    } else if (state == "closed") {
        var joined = tour? 'tour' : tactic_id + "--" + technique_id;
        $(".subtechniques--" + joined).addClass("hidden");
        $(".sidebar--" + joined).removeClass("expanded");
    }
}

//open or close all techniques with sub-techniques
//param is boolean, if true opens all, if false closes all
function matrix_toggle_all(visible) {
    if (visible) {
        $(".sidebar").addClass("expanded");
        $(".subtechniques-container").removeClass("hidden");
    } else {
        $(".sidebar").removeClass("expanded");
        $(".subtechniques-container").addClass("hidden");
    }
}

// switch tabs to the given matrix, param is either "flat" or "side"
function showMatrix(whichMatrix) {
    if (whichMatrix == "flat") show_flat_matrix();
    if (whichMatrix == "side") show_side_matrix();
}

function show_side_matrix() {
    $(".layout-button.side").addClass("active");
    $(".layout-button.flat").removeClass("active");

    $(".matrix-type.side").removeClass("d-none");
    $(".matrix-type.flat").addClass("d-none");

    layoutOptions = document.getElementById("layout-options");
    layoutOptions.setAttribute("data-selected_layout", "side");
    layoutOptions.innerHTML = "layout: side";
    save_layout();
}

function show_flat_matrix() {
    $(".layout-button.flat").addClass("active");
    $(".layout-button.side").removeClass("active");

    $(".matrix-type.flat").removeClass("d-none");
    $(".matrix-type.side").addClass("d-none");

    layoutOptions = document.getElementById("layout-options");
    layoutOptions.setAttribute("data-selected_layout", "flat");
    layoutOptions.innerHTML = "layout: flat";
    save_layout();
}

function computeScrollMarkers() {
    let beginning = $(this).scrollLeft() == 0; //is the scroll at the left side?
    //is the scroll at the right side? 
    let scrollPosition = ($(this).scrollLeft() + $(this).width()); //the right side of the scroll viewport
    let scrollEnd = $(this).find(".matrix").width(); // the right side of the scrollABLE area
    let end = Math.abs(scrollPosition - scrollEnd) < 5; //are they roughly the same?
    let leftIndicator = $(this).parent().find(".scroll-indicator.left")
    let rightIndicator = $(this).parent().find(".scroll-indicator.right")
    if (!beginning) leftIndicator.addClass("show");
    else            leftIndicator.removeClass("show");
    if (!end)       rightIndicator.addClass("show");
    else            rightIndicator.removeClass("show");
}

function load_saved_layout() {
    let saved_layout = localStorage.getItem("saved_layout");
    if (saved_layout == "flat") {
        show_flat_matrix();
    }
}

function save_layout() {
    let saved_layout = document.getElementById("layout-options").getAttribute("data-selected_layout");
    localStorage.setItem("saved_layout", saved_layout);
}

$(".matrix-scroll-box").scroll(computeScrollMarkers); //respond to scrolling in matrix scroll boxes
function initScrollMarkers() { $(".matrix-scroll-box").each(computeScrollMarkers); } 
initScrollMarkers(); //initial state for scroll markers
$(window).resize(initScrollMarkers); //respond to page resize