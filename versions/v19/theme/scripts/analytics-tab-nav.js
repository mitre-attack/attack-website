document.addEventListener("DOMContentLoaded", navigateToAnalyticTabFromHash);

function navigateToAnalyticTabFromHash() {
    if (window.location.hash) {
        // get analytic ID & header from URL hash
        const analyticId = window.location.hash.substring(1);
        const analyticHeader = document.getElementById(analyticId);
        if (!analyticHeader) return;

        // scope to the analytics tab container (prevents issues with top navigation bar)
        const tabsContainer = document.getElementById('analytics-tabs');
        if (!tabsContainer) return;

        // find the tab pane containing the analytic header
        const tabPane = analyticHeader.closest(".tab-pane");
        if (tabPane?.id) {
            // find tab link for the parent tab-pane
            const tabLink = tabsContainer.querySelector('.nav-link[href="#' + tabPane.id + '"]');
            if(!tabLink) return;

            // check if bootstrap api is available
            if (typeof $ !== "undefined" && typeof $.fn.tab !== "undefined") {
                // listen for tab show event, then scroll to analytic header
                $(tabLink).on('shown.bs.tab', function() {
                    analyticHeader.scrollIntoView({
                        behavior: "smooth",
                        block: "start",
                    });
                });
                // use jquery to switch to correct tab
                $(tabLink).tab('show');
            } else {
                // cannot use bootstrap, use manual tab activation instead
                // remove 'active' from all tabs
                tabsContainer.querySelectorAll('.nav-link').forEach(link => {
                    link.classList.remove('active');
                    link.setAttribute('aria-selected', 'false');
                });
                // add 'active' to the target analytic tab
                tabLink.classList.add('active');
                tabLink.setAttribute('aria-selected', 'true');

                // remove 'show active' from all tab panes
                tabsContainer.querySelectorAll('.tab-pane').forEach(pane => {
                    pane.classList.remove('show', 'active');
                    pane.setAttribute('aria-hidden', 'true');
                });
                // add 'show active' to the target analytic tab
                tabPane.classList.add('show', 'active');
                tabPane.setAttribute('aria-hidden', 'false');

                // scroll to analytic analyticHeader
                analyticHeader.scrollIntoView({
                    behavior: "smooth",
                    block: "start",
                });
            }
        }

    }
}