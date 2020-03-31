//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Sub-techniques on the technique pages",
        content: "The techniques page has been redesigned to support sub-techniques.",
    },
    {
        element: "#subtechniques-card-body",
        placement: "right",
        backdrop: false,
        title: "Showing sub-techniques of a technique",
        content: "The sub-techniques of the technique are displayed within this panel. If the panel is omitted, then the technique has no sub-techniques.",
        onShow: function() {
            $("#subtechniques-card-body").collapse("show");
        },
        // next: isSiteTour? 3 : -1, //if it's a site tour, there is a next page.
    },
]

if (isSiteTour) tourSteps.push({
    onShow: function() { //go to the next tour module
        window.location.href = "/beta/techniques/T1053/001/?tour=true"
    }
})

let tour = new Tour({
    container: "#tab-content",
    steps: tourSteps,
    container: "#v-tabContent",
    storage: false, //no resuming tour if the page is reloaded.
    framework: 'bootstrap4',   // set Tourist to use BS4 compatibility
    showProgressBar: !isSiteTour,
    showProgressText: !isSiteTour,
})

function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

if (isSiteTour) {
    console.log("continuing tour")
    start_tour();
}