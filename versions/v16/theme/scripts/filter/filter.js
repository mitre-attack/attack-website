/**
 * Initial domains.
 * @type {string[]}
 */
const domains = ['enterprise', 'ics', 'mobile'];

/**
 * On DOMContentLoaded event, show or hide elements based on saved filter
 * and update sessionStorage with the available domains.
 */
addEventListener('DOMContentLoaded', () => {
    // Get saved filter from sessionStorage or set to domains
    const savedFilter = sessionStorage.getItem('filter');
    const includedDomains = savedFilter ? savedFilter.split(',') : domains;

    // Filter domains without associated switch
    const removeDomains = domains.filter(domain => $(`#${domain}Switch`).length === 0);

    // Update domains by removing domains without a switch
    const updatedDomains = domains.filter(domain => !removeDomains.includes(domain));
    sessionStorage.setItem('filter', updatedDomains);

    // Show or hide elements based on the includedDomains
    updatedDomains.forEach(domain => {
        const switchID = `#${domain}Switch`;
        const domainClass = `.${domain}`;

        if (includedDomains.includes(domain)) {
            $(switchID).prop('checked', true); // Set switch to checked state
            $(domainClass).show();             // Show elements with the domain class
        } else {
            const objectsOfDomainClass = $(domainClass);

            // Hide elements only if none of their classes are included in the includedDomains
            if (objectsOfDomainClass.length > 0) {
          objectsOfDomainClass.each((_, obj) => {
              const { classList } = obj;
              if (Array.from(classList).every(cls => !includedDomains.includes(cls))) {
                  $(obj).hide(); // Hide elements with the domain class
              }
        });
      }
    }
  });
});

/**
 * Toggle the visibility of elements with a specific domain class based on switch state.
 * Update sessionStorage with the current filter.
 *
 * @param {HTMLElement} switchID - The switch DOM element (checkbox) that triggers the filter.
 * @param {HTMLElement} fallbackSwitchID - An optional switch DOM element (checkbox) to be checked when all other switches are unchecked.
 */
function filterTables(switchID, fallbackSwitchID) {
    const domain = switchID.id.split("Switch")[0];
    const domainClass = `.${domain}`;

    const includedDomains = sessionStorage.getItem('filter').split(",");

    if (switchID.checked) {
        $(domainClass).show();
      if (!includedDomains.includes(domain)) {
          includedDomains.push(domain);
      }
  } else {
      includedDomains.splice(includedDomains.indexOf(domain), 1);

      const objectsOfDomainClass = $(domainClass);
      if (objectsOfDomainClass.length > 0) {
        objectsOfDomainClass.each((_, obj) => {
            const { classList } = obj;
            if (Array.from(classList).every(cls => !includedDomains.includes(cls))) {
                $(obj).hide();
            }
      });
    }

      // Check switchID2 and show elements with its domain class when all other switches are unchecked
      if (includedDomains.length === 0) {
          const domain2 = fallbackSwitchID.id.split("Switch")[0];
          const id2 = `.${domain2}`;
          fallbackSwitchID.checked = true;
          $(id2).show();
          includedDomains.push(domain2);
      }
  }

    // Check if at least one technique is visible
    const techniquesVisible = $('.technique').toArray().some(technique => technique.style.display.length === 0);

    // Show or hide the message based on the visibility of the techniques
    const messageObjects = $('.no-techniques-in-data-source-message');
    messageObjects.each((_, obj) => {
        if (obj.style) {
            obj.style.display = techniquesVisible ? "none" : "";
        }
  });

    // Update sessionStorage with the current filter
    sessionStorage.setItem('filter', includedDomains);
}
