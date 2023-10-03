let mod_name = window.location.pathname.split("/")
let mod_entry = "/" + mod_name[1] + "/sidebar-" + mod_name[1]
if (mod_name.includes('contact')){
    mod_entry = "/" + "resources/sidebar-resources"
}
$("#sidebars").load(mod_entry, function() {
    let navElements = document.querySelectorAll('.sidenav-head > a');
    let winlocation;
    navElements.forEach(function(element){
    if(!window.location.href.endsWith("/")){
        winlocation = window.location.href + "/";
    }
    else{
        winlocation = window.location.href
    }
    if(!element.href.endsWith("/")){
        element.href = element.href + "/";
    }
    if(element.href == winlocation){
        $(element.parentNode).addClass("active")
    }});

    //This code is for creating a collapsable sidebar for the mobile view
    let mediaQuery = window.matchMedia('(max-width: 47.9875rem)')
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
        if (sidenav_active_elements.length > 0) setTimeout(() => { //setTimeout gives bootstrap time to execute first
            sidenav[0].scrollTop = sidenav_active_elements[0].offsetTop - 60;
        });
    });

    mediaQuery.addEventListener('change', mobileSidenav)
});