$("#sidebars").load("/resources/sidebar-check", function() {
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
        console.log(element)
        console.log(element.parentNode)
        $(element.parentNode).addClass("active")
    }});
});