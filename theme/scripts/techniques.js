$(document).ready(function () {
  $(".expand-title").each(function (index) {
    if ($(this).html().indexOf("All") == -1) {
      $(this).on("click", function () {
        console.log($(this).children("span"))
        if ($(this).children("span").hasClass("glyphicon-plus")) {
          $(this).children("span:last-child").removeClass("glyphicon-plus")
          $(this).children("span:last-child").addClass("glyphicon-minus")
        } 
        else if ($(this).children("span").hasClass("glyphicon-minus")){
          $(this).children("span:last-child").removeClass("glyphicon-minus")
          $(this).children("span:last-child").addClass("glyphicon-plus")
        }
      })
    }
  })
});