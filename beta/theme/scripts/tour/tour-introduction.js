//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

let tour = new Tour({
    storage: false, //no resuming tour if the page is reloaded.
    framework: 'bootstrap4',   // set Tourist to use BS4 compatibility
    showProgressBar: false,
    showProgressText: false
})

if (typeof tour_steps['matrix'] != 'undefined'){
    tour['_options']['steps'] = [
        {
            container: "#tour-start-container",
            element: "#tour-start",
            placement: "bottom",
            title: "Welcome to the ATT&CK sub-techniques tour!",
            content: "This guided tour will walk you through the new sub-techniques features of the ATT&CK Website.",
        },
        {
            onShow: function() { //go to the next tour module
                window.location.href = base_url + tour_steps['matrix'] + "/?tour=true"
            }
        }
    ]
}
else{
    tour['_options']['steps'] = [
        {
            container: "#tour-start-container",
            element: "#tour-start",
            placement: "bottom",
            title: "Welcome to the ATT&CK sub-techniques tour!",
            content: "The sub-techniques tour only works when sub-techniques are present on the website. Please check your site config and STIX bundles to make sure sub-techniques are present.",
        }
    ]
}

function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

if (isSiteTour) {
    start_tour();
}