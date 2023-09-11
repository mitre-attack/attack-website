$(document).ready(function () { 
console.log("by");
});

    console.log("hi");
    $("#sidebars").load("/docs/sidebar.html", function() {
        // put the code here that you want to run when the .load() 
        // has completed and the content is available
        // Or, you can call a function from here
        let active_id = ""

    // Check if referrer was from the same domain
    // If not, set update to false
    // This will remove unwanted behavior that appears when
    // jumping from one domain to another. E.g. techniques to matrices
    $(".sidenav-head").each(function () {
        let check = localStorage.getItem("need_update");
        if($(this)[0].id == localStorage.getItem("new_active_id") && check === true){
        $(this).addClass("active");
        }
    });

    var sidebar = document.querySelector(".sidebar");
    var sidebarSize = localStorage.getItem('sidebarWidth');
    sidebar.style.width = sidebarSize;

    let current_modules = window.location.pathname.split("/");

    if (document.referrer) {
        // Loop through the modules in case page is hosted from different 
        // directory
        
        let is_found = false;
        for (let i = 0; i < current_modules.length; i++) {
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
        $(this).addClass("active");
    }
    else {
        // Set active id to first element that is active
        // This will open the first one in the case that there are multiple
        $(".sidenav-head.active:first").each(function () {
            active_id = $(this).attr('id').split("-");
            $(this).addClass("active");
        });
    }

    // If this method is called then the user is clicking on the sidenav
    // Set update to true and set the new id to one that was clicked
    $(".sidenav-head").click(function () {
        localStorage.setItem("need_update", true);
        localStorage.setItem("new_active_id", $(this).attr('id'));
    });
});