//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Technique tables",
        content: "On tactic, software, group, and mitigation pages, tables showing techniques have been revised to support sub-techniques.",
    },
    {
        element: "#uses-T1203",
        placement: "left",
        backdrop: false,
        title: "Technique tables",
        content: "In cases where a relationship exists with a technique exists in the table but not its sub-techniques, the row format is unchanged.",
    },
    {
        element: "#uses-T1059",
        placement: "left",
        backdrop: false,
        title: "Technique tables",
        content: "In cases where both the parent and its sub-techniques exists in the table, the sub-techniques are shown nested beneath their parent in the ID column.",
    },
    {
        element: "#uses-T1071-001",
        placement: "left",
        backdrop: false,
        title: "Technique tables",
        content: "In cases where a sub-technique exists in the table but not the parent technique, the parent technique row is omitted entirely.",
    },
    
]

let lastStepReached = false;

if (isSiteTour) tourSteps.push({
    orphan: true,
    backdrop: false,
    title: "End of tour",
    content: "We hope you have enjoyed this tour of the sub-techniques features of the ATT&CK website. If you have any feedback or suggestions, please visit <a href='/contact'>the contact page</a> to get in touch.",
    onShow: function() {
        lastStepReached = true;
    },
    onNext: function() {
        window.location.href = "/";
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
    onEnd: function() {
        if (lastStepReached) window.location.href = "/";
    }
})

function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

if (isSiteTour) {
    console.log("continuing tour")
    start_tour();
}