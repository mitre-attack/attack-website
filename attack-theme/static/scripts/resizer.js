var resizer = document.querySelector(".resizer");
var sidebar = document.querySelector(".sidebar");
$(document).ready(function (){
resizeSidebar( resizer, sidebar );
});


function resizeSidebar( resizer, sidebar ) {
var x = 0;
var w = 0;

function resizeSidebar_mousedownHandler( event ) {
  x = event.clientX;
  var sidebarWidth = window.getComputedStyle( sidebar ).width;
  w = parseInt( sidebarWidth );
  document.addEventListener("mousemove", resizeSidebar_mousemoveHandler);
  document.addEventListener("mouseup", resizeSidebar_mouseupHandler);
}

function resizeSidebar_mousemoveHandler( event ) {
  var dx = event.clientX - x;
  var newsidebarWidth = w + dx;
  sidebar.style.width = `${ newsidebarWidth }px`;
}

function resizeSidebar_mouseupHandler() {
  document.removeEventListener("mouseup", resizeSidebar_mouseupHandler);
  document.removeEventListener("mousemove", resizeSidebar_mousemoveHandler);
}

resizer.addEventListener("mousedown", resizeSidebar_mousedownHandler);
}