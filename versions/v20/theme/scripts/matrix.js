/**
 * Check if the "layout-options" dropdown-toggle button element exists, then load the saved layout.
 */
if (document.getElementById("layout-options")) {
    loadSavedLayout();
}

/**
 * Toggle the visibility and expansion of a matrix technique's subtechniques.
 * @param {string} tacticId - The tactic ID.
 * @param {string} techniqueId - The technique ID.
 */
function toggleMatrixSubTechniques(tacticId, techniqueId) {
    const joined = tacticId + "--" + techniqueId;
    $(".subtechniques--" + joined).toggleClass("hidden");
    $(".sidebar--" + joined).toggleClass("expanded");
}

/**
 * Set the state of the given technique.
 * @param {string} tacticId - The tactic ID.
 * @param {string} techniqueId - The technique ID.
 * @param {string} state - State must be "open" or "closed".
 * @param {boolean} tour - If true, affects the sub-technique tour technique, ignoring the technique and tactic params.
 */
function setMatrixCellState(tacticId, techniqueId, state, tour = false) {
    const joined = tour ? 'tour' : tacticId + "--" + techniqueId;
    const subtechniques = $(".subtechniques--" + joined);
    const sidebar = $(".sidebar--" + joined);

    if (state === "open") {
        subtechniques.removeClass("hidden");
        sidebar.addClass("expanded");
    } else if (state === "closed") {
        subtechniques.addClass("hidden");
        sidebar.removeClass("expanded");
    }
}

/**
 * Open or close all techniques with sub-techniques.
 * @param {boolean} visible - If true, opens all techniques. If false, closes all techniques.
 */
function toggleAllMatrixSubTechniques(visible) {
    if (visible) {
        $(".sidebar").addClass("expanded");
        $(".subtechniques-container").removeClass("hidden");
    } else {
        $(".sidebar").removeClass("expanded");
        $(".subtechniques-container").addClass("hidden");
    }
}

/**
 * Switch tabs to the given matrix.
 * @param {string} whichMatrix - Either "flat" or "side".
 */
function showMatrix(whichMatrix) {
    if (whichMatrix === "flat") {
        showFlatMatrix();
    }
    if (whichMatrix === "side") {
        showSideMatrix();
    }
}

/**
 * Display the side matrix layout and save the layout.
 */
function showSideMatrix() {
    $(".layout-button.side").addClass("active");
    $(".layout-button.flat").removeClass("active");

    $(".matrix-type.side").removeClass("d-none");
    $(".matrix-type.flat").addClass("d-none");

    const layoutOptions = document.getElementById("layout-options");
    layoutOptions.setAttribute("data-selected_layout", "side");
    layoutOptions.innerHTML = "layout: side";
    saveLayout();
}

/**
 * Display the flat matrix layout and save the layout.
 */
function showFlatMatrix() {
    $(".layout-button.flat").addClass("active");
    $(".layout-button.side").removeClass("active");

    $(".matrix-type.flat").removeClass("d-none");
    $(".matrix-type.side").addClass("d-none");

    const layoutOptions = document.getElementById("layout-options");
    layoutOptions.setAttribute("data-selected_layout", "flat");
    layoutOptions.innerHTML = "layout: flat";
    saveLayout();
}


/**
 * Compute the scroll markers.
 */
function computeScrollMarkers() {
    const beginning = $(this).scrollLeft() === 0;
    const scrollPosition = $(this).scrollLeft() + $(this).width();
    const scrollEnd = $(this).find(".matrix").width();
    const end = Math.abs(scrollPosition - scrollEnd) < 5;
    const leftIndicator = $(this).parent().find(".scroll-indicator.left");
    const rightIndicator = $(this).parent().find(".scroll-indicator.right");

    if (!beginning) {
        leftIndicator.addClass("show");
    } else {
        leftIndicator.removeClass("show");
    }

    if (!end) {
        rightIndicator.addClass("show");
    } else {
        rightIndicator.removeClass("show");
    }
}

/**
 * Load the saved layout from local storage and display it.
 */
function loadSavedLayout() {
    const savedLayout = localStorage.getItem("saved_layout");
    if (savedLayout === "flat") {
        showFlatMatrix();
    }
}

/**
 * Save the currently selected layout to local storage.
 */
function saveLayout() {
    const savedLayout = document.getElementById("layout-options").getAttribute("data-selected_layout");
    localStorage.setItem("saved_layout", savedLayout);
}

// Respond to scrolling in matrix scroll boxes
$(".matrix-scroll-box").scroll(computeScrollMarkers);

// Initialize the scroll markers
function initScrollMarkers() {
    $(".matrix-scroll-box").each(computeScrollMarkers);
}

initScrollMarkers(); // Initial state for scroll markers
$(window).resize(initScrollMarkers); // Respond to page resize