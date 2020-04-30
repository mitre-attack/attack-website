$(document).ready(function () { 

    let active_id = ""

    // Check if referrer was from the same domain
    // If not, set update to false
    // This will remove unwanted behavior that appears when
    // jumping from one domain to another. E.g. techniques to matrices
    let current_modules = window.location.pathname.split("/");

    if (document.referrer) {
        // Loop through the modules in case page is hosted from different 
        // directory
        
        let is_found = false;
        for (i = 0; i < current_modules.length; i++) {
            if ((document.referrer.includes(current_modules[i]))) {
                is_found = true;
            }
            if (!is_found) {
                localStorage.setItem("need_update", false);
            }
        }
    }
    else {
        localStorage.setItem("need_update", false);
    }
    
    // Update panes
    if (localStorage.getItem("need_update") === "true") {
        // Get active id from storage and remove update
        active_id = localStorage.getItem("new_active_id").split("-")
        localStorage.setItem("need_update", false);
    }
    else {
        // Set active id to first element that is active
        // This will open the first one in the case that there are multiple
        $(".sidenav-head.active:first").each(function () {
            active_id = $(this).attr('id').split("-");
        });
    }

    // Open necessary panes
    $(".expand-button").each(function () {
        let tree = "";
        for (i = 0; i < active_id.length; i++) {
            tree += active_id[i] + "-";
            if ($(this).attr('id') === tree+"header") {
                $(this).addClass("notransition");
                $(this).removeClass("collapsed");
            }
        }
    });

    $(".sidenav-body.collapse").each(function () {
        let tree = "";
        for (i = 0; i < active_id.length; i++) {
            tree += active_id[i] + "-";
            if ($(this).attr('id') === tree+"body") {
                $(this).addClass("show");
            }
        }
    });

    // If this method is called then the user is clicking on the sidenav
    // Set update to true and set the new id to one that was clicked
    $(".sidenav-head").click(function () {
        localStorage.setItem("need_update", true);
        localStorage.setItem("new_active_id", $(this).attr('id'));
    });

    // If this method is called, then the user has clicked on a link in the subtechniques dropdown table.
    // Sets update to true and creates a new_active_id from the active_id so that the original domain-tactic_id-tech_id path is retained.
    // This ensures that the sidenav opens the correct tactic (given the context) for the subtechnique that was clicked.
    $(".subtechnique-table-item").click(function () {
        let new_active_id = active_id;
        new_active_id.push($(this).attr('data-subtechnique_id'));
        localStorage.setItem("need_update", true);
        localStorage.setItem("new_active_id", new_active_id.join("-"));
    });

    // Remove notransition class when expand button is clicked
    $(".expand-button.notransition").click(function () {
        $(this).removeClass("notransition");
        console.log("removed class");
    });

});