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
        content: "You can view the current and past versions of the website by clicking on the links under the \"Version\" column."
    },
    {
        element: "#data-column",
        placement: "top",
        backdrop: false,
        title: "Versions of ATT&CK - Data",
        content: "The STIX data for each version is found under the \"Data\" column."
    },
    {
        element: "#release-notes-column",
        placement: "top",
        backdrop: false,
        title: "Versions of ATT&CK - Release Notes",
        content: "Each major release is accompanied with release notes that detail the changes."
    },
    {
        orphan: true,
        backdrop: false,
        title: "Versions of ATT&CK",
        content: "All object pages now include a \"Version Permalink\". Future updates to ATT&CK won't affect the permalinked page. To return to the live version of the object, click the \"Live Version\" link."
    },
    {
        orphan: true,
        backdrop: false,
        title: "End of tour",
        content: "We hope you have enjoyed this tour of the sub-techniques features of the ATT&CK website. If you have any feedback or suggestions, please visit <a href='" + base_url + "/contact'>the contact page</a> to get in touch.",
        onShow: function() {
            lastStepReached = true;
        },
        onNext: function() {
            window.location.href = base_url == ""? "/" : base_url;
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
        if (lastStepReached) window.location.href = base_url == ""? "/" : base_url;
    }
})

function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

if (isSiteTour) {
    start_tour();
}