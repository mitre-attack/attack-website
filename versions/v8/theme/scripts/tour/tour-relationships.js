//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Technique tables",
        content: "On tactic, software, group, and mitigation pages, tables showing techniques have been revised to support sub-techniques.",
    }    
]

if (isSiteTour && tour_steps['relationships']['step1'] != 'undefined') tourSteps.push({
    element: "#uses-" + tour_steps['relationships']['step1'],
    placement: "left",
    backdrop: false,
    title: "Technique tables",
    content: "In cases where a technique exists in the table but not its sub-techniques, the row format is unchanged."
})

if (isSiteTour && tour_steps['relationships']['step2'] != 'undefined') tourSteps.push({
    element: "#uses-" + tour_steps['relationships']['step2'],
    placement: "left",
    backdrop: false,
    title: "Technique tables",
    content: "In cases where both the technique and its sub-techniques exists in the table, the sub-techniques are shown nested beneath their parent in the ID column."
})

if (isSiteTour && tour_steps['relationships']['step3'] != 'undefined') tourSteps.push({
    element: "#uses-" + tour_steps['relationships']['step3'],
    placement: "left",
    backdrop: false,
    title: "Technique tables",
    content: "In cases where a sub-technique exists in the table but not the parent technique, the parent technique row is omitted entirely."
})

if (isSiteTour) tourSteps.push({
    onShow: function() { //go to the next tour module
        window.location.href = base_url + "resources/versions/?tour=true"
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