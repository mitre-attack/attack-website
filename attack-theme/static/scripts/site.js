// position body according to header size
function positionBody() {
    let headerHeight = $(".navbar").outerHeight();
    let viewportHeight = $(".attack-website-wrapper").outerHeight();
    let sidebarHeight = viewportHeight - headerHeight + "px"
    console.log("positioning body", headerHeight, viewportHeight, sidebarHeight)
    $(".sidebar").css({
        "top": headerHeight + "px",
        "max-height": viewportHeight - headerHeight + "px"
    });
}

// when the document loads, position the body
$(document).ready(function() {
    positionBody();
    $('[data-toggle="tooltip"]').tooltip();
});

// when the document resizes, position body
$(window).resize(function() {
    positionBody();;
});