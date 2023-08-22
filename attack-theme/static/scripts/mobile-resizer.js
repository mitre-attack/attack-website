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