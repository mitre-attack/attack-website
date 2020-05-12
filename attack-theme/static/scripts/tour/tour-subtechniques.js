//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Sub-technique pages",
        content: "Sub-technique pages are laid out very much like those of techniques.",
    },
    {
        element: "#subtechnique-parent-name",
        placement: "bottom",
        backdrop: false,
        title: "Sub-technique names",
        content: "Sub-technique names are prefixed with the name of their parent technique.",
    },
    {
        element: "#subtechniques-card-body",
        placement: "right",
        backdrop: false,
        title: "Sibling sub-techniques",
        content: "You can see other sub-techniques under the same parent within this panel. The current sub-technique is highlighted.",
        onShow: function() {
            $("#subtechniques-card-body").collapse("show");
        },
    },
    {
        element: "#card-id",
        placement: "left",
        backdrop: false,
        title: "Sub-technique IDs",
        content: "Sub-technique IDs are a suffix of their parent IDs.",
    },
    {
        element: "#card-tactics",
        placement: "left",
        backdrop: false,
        title: "Sub-technique tactics",
        content: "Sub-techniques have the same tactics as their parent technique.",
    },
    {
        element: "#card-platforms",
        placement: "left",
        backdrop: false,
        title: "Sub-technique platforms",
        content: "Sub-techniques have a subset of their parent technique's platforms.",
        // next: isSiteTour? 6 : -1, //if it's a site tour, there is a next page.
    }
]

if (isSiteTour && tour_steps['obj'] != 'undefined') tourSteps.push({
    onShow: function() { //go to the next tour module
        window.location.href = base_url + tour_steps['relationships']['obj_id'] + "/?tour=true"
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
    start_tour();
}