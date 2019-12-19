
//tour technique is scheduled task under privilege escalation
let example_cell = {
    "tactic": "x-mitre-tactic--5e29b093-294e-49e9-a803-dab3d73b77dd",
    "technique": "attack-pattern--35dd844a-b219-4e2b-a6bb-efa9a75995a9"
}
function close_example() {
    setMatrixCellState(example_cell["tactic"], example_cell["technique"], "closed")
}
function open_example() {
    setMatrixCellState(example_cell["tactic"], example_cell["technique"], "open")
}
function tour_technique_clicked() {
    if (tour.getCurrentStep() == 2 || tour.getCurrentStep() == 5) tour.next(); //user was following prompt, triggering next step
}
function tour_layout_clicked() {
    if (tour.getCurrentStep() == 4) tour.next();
}

let tour = new Tour({
    steps: [
        {
            path: "/",
            container: "#tour-start-container",
            element: "#tour-start",
            placement: "bottom",
            title: "Welcome to the ATT&CK sub-techniques tour!",
            content: "This guided tour will walk you through the new sub-techniques features of the ATT&CK Website."
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#layouts-content",
            placement: "top",
            backdrop: true,
            title: "The sub-techniques matrix",
            content: "The ATT&CK matrix has been redesigned to support sub-techniques. Sub-techniques are hidden by default.",
            onShow: function() {
                showMatrix("side");
            }
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#tour-side-technique",
            placement: "right",
            backdrop: true,
            title: "Showing sub-techniques",
            content: "Techniques which have sub-techniques are denoted by a gray sidebar. Not all techniques have sub-techniques. Click the gray sidebar to show the sub-techniques of the technique.",
            onShow: function() {
                showMatrix("side");
                close_example();
            }
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#tour-side-subtechniques",
            placement: "top",
            backdrop: true,
            title: "Showing sub-techniques",
            content: "The sub-techniques of the technique are displayed in a subcolumn to the right.",
            onShow: function() {
                showMatrix("side");
                open_example();
            }
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#layout-options",
            placement: "top",
            title: "Using the flat matrix layout",
            content: "There are multiple ways subtechniques can be represented in the matrix. Click the 'layouts' dropdown and select 'flat layout' to see the alternate layout."
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#tour-flat-technique",
            placement: "left",
            backdrop: true,
            title: "Showing sub-techniques",
            content: "Techniques which have sub-techniques are denoted by a gray sidebar. Click the gray sidebar to show the sub-techniques of the technique.",
            onShow: function() {
                showMatrix("flat");
                close_example();
            }
        },
        {
            path: "/matrices/enterprise/",
            container: "#tour-matrix-container",
            element: "#tour-flat-subtechniques",
            placement: "left",
            backdrop: true,
            title: "Showing sub-techniques",
            content: "The sub-techniques of the technique are displayed below the technique.",
            onShow: function() {
                showMatrix("flat");
                open_example();
            }
        },
    ],
    debug: true
})

tour.init();

function start_subtechniques_tour() {
    if (tour.ended()) tour.restart();
    else tour.start(true);
}

