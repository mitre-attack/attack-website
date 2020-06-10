// position body according to header size
function positionBody() {
    $("body").css("padding-top", $(".navbar").outerHeight());
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