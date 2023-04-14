let domains = ['enterprise', 'ics', 'mobile']; //initial domains

// On page load
addEventListener('DOMContentLoaded', (event) => {
    if (!sessionStorage.getItem('filter')) {
        var removeDomains = [];
        for (i in domains) {
            var switchID = "#" + domains[i] + "Switch";
            if ($(switchID).length == 0 ) {
                removeDomains.push(domains[i]);
            }
        }

        // remove domains that do not have a switch
        for (i in removeDomains) {
            index = domains.indexOf(removeDomains[i]);
            if (index != -1) {
                domains.splice(index, 1);
            }
        }

        sessionStorage.setItem('filter', domains);
    }

    includedDomains = sessionStorage.getItem('filter').split(',');
    for (i in domains) {
        index = includedDomains.indexOf(domains[i]);
        var domainClass = '.' + domains[i];
        if (index != -1) {
            var switchID = "#" + domains[i] + "Switch";
            if ($(switchID).length > 0 ) {
                $(switchID)[0].checked = true; // toggle on
                $(domainClass).show();         // show domain
            }
        }
        else {
            // Hide only if other domains are not enabled
            var objectsOfDomainClass = $(domainClass);
            if (objectsOfDomainClass.length > 0) {
                for (i in objectsOfDomainClass) {
                    var classList = objectsOfDomainClass[i].classList;
                    var hide = true;
                    if (classList) {
                        for (let j = 0; j < classList.length; j++ ) {
                            if (includedDomains.includes(classList[j])) {
                                hide = false;
                            }
                        }
                        if (hide) $(objectsOfDomainClass[i]).hide(); // hide
                    }
                }
            }
        }
    }
});

// filter all objects with class from switch click
// switch id must contain the domain for it to work. e.g., 
// Switch ID2 is optional switch in case all other switched have been disabled
function filterTables(switchID, switchID2) {
    if (switchID.length > 1)
        switchID = switchID[0];

    var domain = switchID.id.split("Switch")[0];
    var domainClass = '.' + domain;

    // Get current selected domains
    var includedDomains = sessionStorage.getItem('filter');
    if (!includedDomains) includedDomains = [];
    else includedDomains = includedDomains.split(",");

    if (switchID.checked) {
        $(domainClass).show();
        index = includedDomains.indexOf(domain);
        if (index == -1) {
            includedDomains.push(domain);
        }
    }
    else {
        // Find index in storage and remove from includedDomains
        index = includedDomains.indexOf(domain);
        if (index != -1) {
            includedDomains.splice(index, 1);
        }

        // Hide only if other domains are not enabled
        var objectsOfDomainClass = $(domainClass);
        if (objectsOfDomainClass.length > 0) {
            for (i in objectsOfDomainClass) {
                var classList = objectsOfDomainClass[i].classList;
                var hide = true;
                if (classList) {
                    for (let j = 0; j < classList.length; j++ ) {
                        if (includedDomains.includes(classList[j])) {
                            hide = false;
                        }
                    }
                    if (hide) $(objectsOfDomainClass[i]).hide(); // hide
                }
            }
        }

        if (switchID2.length > 1) switchID2 = switchID2[0];

        // Set switch 2 to checked if all other domains have been unchecked
        if (includedDomains.length == 0) {
            var domain2 = switchID2.id.split("Switch")[0];
            var id2 = '.' + domain2;
            switchID2.checked = true;
            $(id2).show();
            // Add to includedDomains
            index = includedDomains.indexOf(domain2);
            if (index == -1) {
                includedDomains.push(domain2);
            }
        }
    }

    // Determine if any of the associated techniques are visible
    var techniqueObjects = $('.technique');
    var techniquesVisible = false;
    for (let techniqueObject of techniqueObjects) {
        var display = techniqueObject.style.display;
        if (display.length === 0) {
            techniquesVisible = true;
        }
    }

    // Only show the message if all the associated techniques are hidden
    var messageObjects = $('.no-techniques-in-data-source-message');
    if (messageObjects.length > 0) {
        for (i in messageObjects) {
            if (messageObjects[i].style) {
                if (techniquesVisible) {
                    messageObjects[i].style.display = "none";
                } else {
                    messageObjects[i].style.display = "";
                }
            }
        }
    }

    // Update session storage
    sessionStorage.setItem('filter', includedDomains);
}