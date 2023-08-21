const mediaQuery = window.matchMedia('(max-width: 47.9875rem)')

    function mobileSidenav(e) {
    // Check if the media query is true
    if (e.matches) {
        // Then log the following message to the console
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