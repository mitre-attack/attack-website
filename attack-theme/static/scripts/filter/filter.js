let domains = ['enterprise', 'ics'];

addEventListener('DOMContentLoaded', (event) => {
    if (!sessionStorage.getItem('filter')) {
        sessionStorage.setItem('filter', domains);
    }

    includedDomains = sessionStorage.getItem('filter').split(',');
    for (i in domains) {
        index = includedDomains.indexOf(domains[i]);
        var domainClass = '.' + domains[i];
        if (index != -1) {
            var switchID = "#" + domains[i] + "Switch";
            $(switchID)[0].checked = true; // toggle on
            $(domainClass).show();         // show domain
        }
        else {
            $(domainClass).hide(); // hide
        }
    }
});

function filterTables(switchID, switchID2) {
    if (switchID.length > 1)
        switchID = switchID[0];

    var domain = switchID.id.split("Switch")[0];
    var id = '.' + domain;

    // Get current selected domains
    var includedDomains = sessionStorage.getItem('filter');
    if (!includedDomains) includedDomains = [];
    else includedDomains = includedDomains.split(",");

    if (switchID.checked) {
        $(id).show();
        index = includedDomains.indexOf(domain);
        if (index == -1) {
            includedDomains.push(domain);
        }
    }
    else {
        $(id).hide();

        // Find index in storage and remove from includedDomains
        index = includedDomains.indexOf(domain);
        if (index != -1) {
            includedDomains.splice(index, 1);
        }

        // At least one domain must be checked
        if (switchID2.length > 1)
            switchID2 = switchID2[0];
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
    // Update session storage
    sessionStorage.setItem('filter', includedDomains);
}