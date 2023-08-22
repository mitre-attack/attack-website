//This code is for being able to resize the sidebar in the desktop view
var resizer = document.querySelector(".resizer");
var sidebar = document.querySelector(".sidebar");

if(resizer!=null) {
  resizeSidebar( resizer, sidebar );
}

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
  localStorage.setItem("sidebarWidth", sidebar.style.width);
}

function resizeSidebar_mouseupHandler() {
  document.removeEventListener("mouseup", resizeSidebar_mouseupHandler);
  document.removeEventListener("mousemove", resizeSidebar_mousemoveHandler);
}

resizer.addEventListener("mousedown", resizeSidebar_mousedownHandler);
}

//This code is for creating a collapsable sidebar for the mobile view
const mediaQuery = window.matchMedia('(max-width: 47.9875rem)')

function mobileSidenav(e) {
  if (e.matches) {
      $('#sidebar-collapse').collapse('hide')
  }
  else{
      $('#sidebar-collapse').collapse('show')
  }
}
$(document).ready(function() {
  mobileSidenav(mediaQuery)
});

mediaQuery.addEventListener('change', mobileSidenav)