let mod_name = window.location.pathname.split("/")
let mod_entry = "/" + mod_name[1] + "/sidebar-" + mod_name[1]
$("#sidebars").load(mod_entry, function() {
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
        var parentElement = $(element.parentNode);
        var elementID = document.getElementById(parentElement[0].id)
        elementID.scrollIntoView({ behavior: "smooth", block: "center" })
    }});
    var mediaQuery = window.matchMedia('(max-width: 47.9875rem)')

    function mobileSidenav(e) {
    if (e.matches) {
      $('#sidenav-list').collapse('hide')
    }
    else{
      $('#sidenav-list').collapse('show')
    }
    }
    $(document).ready(function() {
        mobileSidenav(mediaQuery)
        let sidenav = $(".sidenav-list");
        let sidenav_active_elements = $(".sidenav .active");
        sidenav_active_elements[0].scrollIntoView({ behavior: "smooth", block: "center" })
    });

    mediaQuery.addEventListener('change', mobileSidenav)
});