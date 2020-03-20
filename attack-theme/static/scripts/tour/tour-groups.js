//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Relationship tables",
        content: "On tactic, software, group, and mitigation pages, tables showing relationships with techniques have been revised to support sub-techniques.",
    },
    {
        element: "#uses-T1203",
        placement: "left",
        backdrop: false,
        title: "Relationship tables: techniques",
        content: "In cases where a relationship exists with a technique but not the technique's sub-techniques, the row format is unchanged.",
    },
    {
        element: "#uses-T1059",
        placement: "left",
        backdrop: false,
        title: "Relationship tables: techniques with sub-techniques",
        content: "In cases where a relationship exists with a technique and its sub-techniques, the sub-techniques are shown nested beneath their parent in the ID column.",
    },
    {
        element: "#uses-T1071-001",
        placement: "left",
        backdrop: false,
        title: "Relationship tables: sub-techniques",
        content: "In cases where a relationship exists with a sub-technique but not the parent technique, the parent technique row is omitted entirely. The grouping of sibling sub-techniques is displayed by a row-spanning parent ID sub-column.",
    },
    
]

if (isSiteTour) tourSteps.push({
    orphan: true,
    backdrop: false,
    title: "End of tour",
    content: "We hope you have enjoyed this tour of the sub-techniques features of the ATT&CK website. If you have any feedback or suggestions, please visit <a href='/contact'>the contact page</a> to get in touch.",
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