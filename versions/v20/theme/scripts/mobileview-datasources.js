// This code is for creating a collapsable sidebar for the mobile view
let mediaQuery = window.matchMedia('(max-width: 74.938rem)')

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