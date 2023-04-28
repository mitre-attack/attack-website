// position body according to header size
function positionBody() {
    let headerHeight = $(".navbar").outerHeight();
    let viewportHeight = $(".attack-website-wrapper").outerHeight();
    let sidebarHeight = viewportHeight - headerHeight + "px";
    $(".sidebar.nav").css({
        "top": headerHeight + "px",
        "max-height": viewportHeight - headerHeight + "px"
    });
}

//scroll the active element into view in the sidenav
function initSidenavScroll() {
    let sidenav = $(".sidenav-list");
    let sidenav_active_elements = $(".sidenav .active");
    if (sidenav_active_elements.length > 0) setTimeout(() => { //setTimeout gives bootstrap time to execute first
        sidenav[0].scrollTop = sidenav_active_elements[0].offsetTop - 60;
    });
}

// when the document loads, position the body
$(document).ready(function() {
    positionBody();
    initSidenavScroll();
    $('[data-toggle="tooltip"]').tooltip();
});

// when the document resizes, position body
$(window).resize(function() {
    positionBody();;
});
