$("#sidebars").load("/groups/sidebar-groups", function() {
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
        let sidenav = $(".sidenav-list");
        let sidenav_active_elements = $(".sidenav .active");
        sidenav_active_elements[0].scrollIntoView({ block: 'nearest', inline: 'start' })
    });

    mediaQuery.addEventListener('change', mobileSidenav)
});