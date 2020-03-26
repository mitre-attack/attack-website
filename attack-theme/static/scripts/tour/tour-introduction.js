let tour = new Tour({
    steps: [
        {
            container: "#tour-start-container",
            element: "#tour-start",
            placement: "bottom",
            title: "Welcome to the ATT&CK sub-techniques tour!",
            content: "This guided tour will walk you through the new sub-techniques features of the ATT&CK Website.",
        },
        {
            onShow: function() { //go to the next tour module
                window.location.href = "/matrices/enterprise/?tour=true"
            }
        }
    ],
    storage: false, //no resuming tour if the page is reloaded.
    framework: 'bootstrap4',   // set Tourist to use BS4 compatibility
    showProgressBar: false,
    showProgressText: false
})


function start_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}