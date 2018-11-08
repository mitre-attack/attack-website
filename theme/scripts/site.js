$(function () {
  $('[data-toggle="tooltip"]').tooltip();
  // $('[data-toggle="tooltip"]').tooltip({
  //       'container': 'body',
  //       'boundary': 'window',
  //       'placement': 'bottom',
  //       'toggle': 'tooltip',
  //       'trigger': 'hover focus',
  //       'animation': false,
  //       'delay': { "show": 0, "hide": 0 },
  //       'template': '<div class="tooltip tooltip-container" role="tooltip">' +
  //       '   <div class="tooltip-arrow"></div>' +
  //       '   <div class="tooltip-inner"></div>' +
  //       '</div>'
  //   });
});

// var tooltipID = [];
// $('[data-toggle="tooltip"]').each(function() {
//     var position = $('#' + this.id).position();
//     var obj = {'left': position.left, 'top': position.top};
//     tooltipID.push(obj);
//     console.log(obj);
// });
//
// $(window).scroll(function() {
//     $('[data-toggle="tooltip"]').each(function(i) {
//         tooltipID[i].id = this.id;
//         console.log(tooltipID[i]);
//         this.style.setProperty('transform', 'translate3d(' + tooltipID[i].left + 'px,' + tooltipID[i].top + 'px, 0px)', 'important');
//     });
// });

 // function to set the height on fly
 function autoHeight() {
  //  $('#content').css('min-height', 0);
  //  $('#content').css('min-height', (
  //    $(document).height() - $("footer").outerHeight() - $("header").outerHeight()
  //  ));
    if ($("html").height() < $(window).height()) {
      $("footer").addClass('sticky-footer');
    } else {
      $("footer").removeClass('sticky-footer');
    }
 }

 // onDocumentReady function bind
 $(document).ready(function() {
  $("header").css("height", $(".navbar").outerHeight());
  autoHeight();
 });

// onResize bind of the function
  $(window).resize(function() {
    autoHeight();
  });

 $('.carousel').carousel();

 // Removes extra line breaks in .card-data class text
$(".card-data").each(function(i, obj ) {
  if (($(obj).children().last().is("br"))) {
    $(obj).children().last().remove();
  }
});