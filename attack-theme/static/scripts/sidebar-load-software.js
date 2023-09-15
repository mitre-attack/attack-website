$("#sidebars").load("/software/sidebar-software", function() {
        var navElements = document.querySelectorAll('.sidenav-head > a');
        var winlocation;
        navElements.forEach(function(element){
        if(!window.location.href.endsWith("/")){
            winlocation = window.location.href + "/";
        }
        else{
         winlocation = window.location.href
        }
        if(element.href == winlocation){
            $(element.parentNode).addClass("active")
        }});
        var mediaQuery = window.matchMedia('(max-width: 47.9875rem)')

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
    });