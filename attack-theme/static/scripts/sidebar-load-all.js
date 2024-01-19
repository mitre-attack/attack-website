let mod_name = window.location.pathname.split("/");
let mod_entry;
if (mod_name.includes('versions') && mod_name.length > 4){
    mod_entry = "/" + mod_name[3] + "/sidebar-" + mod_name[3]
}
else{
    mod_entry = "/" + mod_name[1] + "/sidebar-" + mod_name[1]
}
if (mod_name.includes('contact')){
    mod_entry = "/" + "resources/sidebar-resources"
}
$("#sidebars").load(mod_entry, function() {
    let old_winlocation = window.location.href;
    if (mod_name.includes('versions')){
        let v_number = mod_name[2];
        old_winlocation = old_winlocation.replace('/versions/'+ v_number,'');
    }
    if (old_winlocation.includes('tour')){
        old_winlocation = old_winlocation.split('?')[0];
    }
    let navElements = document.querySelectorAll('.sidenav-head > a');
    let winlocation;
    navElements.forEach(function(element){
    if(!element.href.includes('changelog.html')){
        if(!old_winlocation.endsWith("/")){
            winlocation = old_winlocation + "/";
        }
        else{
            winlocation = old_winlocation
        }
        if(!element.href.endsWith("/")){
            element.href = element.href + "/";
        }
    }
    else{
        winlocation = old_winlocation
    }
    if(element.href == winlocation){
        $(element.parentNode).addClass("active");
    }});

    //This code is for creating a collapsable sidebar for the mobile view
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
        let sidenav = $(".sidenav-list");
        let sidenav_active_elements = $(".sidenav .active");
        if (sidenav_active_elements.length > 0) setTimeout(() => { //setTimeout gives bootstrap time to execute first
            let offsetValue = sidenav_active_elements[0].offsetTop;
            if (offsetValue <= 0){
                offsetValue = sidenav_active_elements[sidenav_active_elements.length - 1].offsetTop;
            }
            sidenav[0].scrollTop = offsetValue - 60;
        });
    });

    mediaQuery.addEventListener('change', mobileSidenav)
});