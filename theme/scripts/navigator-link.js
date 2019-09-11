function setNavLinkHref(id, path){
    if(id == "mobile-layer"){
        document.getElementById(id).href = "https://mitre-attack.github.io/attack-navigator/mobile/#layerURL=" + encodeURIComponent(window.location.protocol + "//" + window.location.hostname + path);
    }
    else{
        document.getElementById(id).href = "https://mitre-attack.github.io/attack-navigator/enterprise/#layerURL=" + encodeURIComponent(window.location.protocol + "//" + window.location.hostname + path);
    }
}