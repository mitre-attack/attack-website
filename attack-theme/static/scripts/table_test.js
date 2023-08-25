function filter_rows() {
    filter_row = document.querySelector(".table-filter")
    col_index = 3
    filter_value = filter_row.value

    const rows = document.querySelectorAll("#ds-table tbody tr");
    let count = 0
    rows.forEach((row) => {
        var display_row = true;
        row_data = row.querySelector("td:nth-child(" + col_index + ")").innerHTML
        if (row_data.indexOf(filter_value) == -1 && filter_value != "all") {
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
  
