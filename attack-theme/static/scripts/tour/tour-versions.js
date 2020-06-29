//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let lastStepReached = false;

let tourSteps = [
    {
        orphan: true,
        backdrop: false,
        title: "Versions of ATT&CK",
        content: "Versions of the ATT&CK website are preserved on this page."
    },
    {
        element: "#version-column",
        placement: "top",
        backdrop: false,
        title: "Versions of ATT&CK - Version",
        content: "You can view the current and past versions of the website by clicking on the links under this column."
    },
    {
        element: "#data-column",
        placement: "top",
        backdrop: false,
        title: "Versions of ATT&CK - Data",
        content: "The STIX bundles are also preserved by versions. The latest release of each major version can be found under the Data column."
    },
    {
        element: "#release-notes-column",
        placement: "top",
        backdrop: false,
        title: "Versions of ATT&CK - Release Notes",
        content: "Each major release is accompanied with release notes that detail the changes. View the release notes under this column, alternatively they can be found <a href='" + base_url + "resources/updates'>here</a>."
    },
    {
        orphan: true,
        backdrop: false,
        title: "Versions of ATT&CK",
        content: "When you visit an ATT&CK page, a pre-perserved version of the page can be found by clicking on the hyperlink named 'Version Permalink'. To return to the live version of the current page, click on the same hyperlink, now named 'Live Version'."
    },
    {
        orphan: true,
        backdrop: false,
        title: "End of tour",
        content: "We hope you have enjoyed this tour of the sub-techniques features of the ATT&CK website. If you have any feedback or suggestions, please visit <a href='" + base_url + "contact'>the contact page</a> to get in touch.",
        onShow: function() {
            lastStepReached = true;
        },
        onNext: function() {
            window.location.href = base_url;
        }
    }    
]

let tour = new Tour({
    steps: tourSteps,
    storage: false, //no resuming tour if the page is reloaded.
    framework: 'bootstrap4',   // set Tourist to use BS4 compatibility
    showProgressBar: !isSiteTour,
    showProgressText: !isSiteTour,
    onEnd: function() {
        if (lastStepReached) window.location.href = base_url;
    }
})

function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

if (isSiteTour) {
    start_tour();
}