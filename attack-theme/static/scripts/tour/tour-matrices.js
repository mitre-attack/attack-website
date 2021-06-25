//is the user doing a tour of the entire site, or just this module?
isSiteTour = window.location.href.includes("?tour=true");

function close_example() {
    setMatrixCellState(null, null, "closed", tour)
}
function open_example() {
    setMatrixCellState(null, null, "open", tour)
}

function tour_technique_clicked() {
    if (tour.getCurrentStepIndex() == 1 || tour.getCurrentStepIndex() == 4) tour.next(); //user was following prompt, triggering next step
}
function tour_layout_clicked() {
    if (tour.getCurrentStepIndex() == 3) tour.next();
}

tourSteps = [
        {
        orphan: true,
        backdrop: false,
        title: "The sub-techniques matrix",
        content: "The ATT&CK matrix has been redesigned to support sub-techniques. Sub-techniques are hidden by default.",
        onShow: function() {
            showMatrix("side");
        }
    },
    {
        container: "#tour-matrix-container",
        element: "#tour-side-technique",
        placement: "right",
        backdrop: false,
        title: "Showing sub-techniques",
        content: "Techniques that have sub-techniques are denoted by a gray sidebar. Not all techniques have sub-techniques. Click the gray sidebar to show the sub-techniques of the technique.",
        onShow: function() {
            showMatrix("side");
            close_example();
        }
    },
    {
        container: "#tour-matrix-container",
        element: "#tour-side-subtechniques",
        placement: "top",
        backdrop: false,
        title: "Showing sub-techniques",
        content: "The sub-techniques of the technique are displayed in a subcolumn to the right.",
        onShow: function() {
            showMatrix("side");
            open_example();
        }
    },
    {
        container: "#tour-matrix-container",
        element: "#layout-options",
        placement: "top",
        title: "Using the flat matrix layout",
        content: "There are multiple ways sub-techniques can be represented in the matrix. Click the 'layout' dropdown and select 'flat' to see the alternate layout."
    },
    {
        container: "#tour-matrix-container",
        element: "#tour-flat-technique",
        placement: "left",
        backdrop: false,
        title: "Showing sub-techniques",
        content: "Techniques which have sub-techniques are denoted by a gray sidebar. Click the gray sidebar to show the sub-techniques of the technique.",
        onShow: function() {
            showMatrix("flat");
            close_example();
        }
    },
    {
        container: "#tour-matrix-container",
        element: "#tour-flat-subtechniques",
        placement: "left",
        backdrop: false,
        title: "Showing sub-techniques",
        content: "The sub-techniques of the technique are displayed below the technique.",
        onShow: function() {
            showMatrix("flat");
            open_example();
        }
    }
]

if (isSiteTour && tour_steps['technique'] != 'undefined') tourSteps.push({
    onShow: function() { //go to the next tour module
        window.location.href = base_url + tour_steps['technique'] + "/?tour=true"
    }
})

let tour = new Tour({
    steps: tourSteps,
    container: "#tour-matrix-container",
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
