function filter_rows() {
    col_index = 3
    const domainOptions = document.getElementById("domain-options");
    filter_value = domainOptions.getAttribute("data-selected_domain");

    const rows = document.querySelectorAll("#ds-table tbody tr");
    let count = 0
    rows.forEach((row) => {
        var display_row = true;
        row_data = row.querySelector("td:nth-child(" + col_index + ")").innerHTML
        if (row_data.indexOf(filter_value) == -1 && filter_value != "All") {
            display_row = false;
        }
        if (display_row == true) {
            row.style.display = "table-row"
            count = count + 1
        } else {
            row.style.display = "none"
        }
    })
    filter_count = document.querySelector(".table-object-count")
    filter_count.innerHTML = `Data Sources: ${count}`
}

$(document).ready(function() {
    filter_rows()
});
  
function showAllDomains() {
    const domainOptions = document.getElementById("domain-options");
    domainOptions.setAttribute("data-selected_domain", "All");
    domainOptions.innerHTML = "Domain: All";
    filter_rows();
}


function showEnterprise() {
    const domainOptions = document.getElementById("domain-options");
    domainOptions.setAttribute("data-selected_domain", "Enterprise");
    domainOptions.innerHTML = "Domain: Enterprise";
    filter_rows();
}

/**
 * Display the flat matrix domain and save the domain.
 */
function showMobile() {
    const domainOptions = document.getElementById("domain-options");
    domainOptions.setAttribute("data-selected_domain", "Mobile");
    domainOptions.innerHTML = "Domain: Mobile";
    filter_rows();
}

function showIcs() {
    const domainOptions = document.getElementById("domain-options");
    domainOptions.setAttribute("data-selected_domain", "ICS");
    domainOptions.innerHTML = "Domain: ICS";
    filter_rows();
}

function sortTable(col_no) {
    var table = document.getElementById("ds-table");
    rows = table.rows;
      for (let i = 1; i <= (rows.length - 1); i++) {
        for (let j = 1; j <= (rows.length - i - 1); j++) {
            var x = rows[j].getElementsByTagName("TD")[col_no];
            var y = rows[j + 1].getElementsByTagName("TD")[col_no];
            if(x.innerText.toLowerCase() > y.innerText.toLowerCase()){
                rows[j].parentNode.insertBefore(rows[j + 1], rows[j]);
            }
        }
  }
}
