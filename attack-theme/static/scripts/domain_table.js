// this function filters table rows based on the selection
function filter_row(selected) {
    let col_index = 3
    const rows = document.querySelectorAll("#ds-table tbody tr");
    let count = 0;
    rows.forEach((row) => {
        let row_count = 0
        let row_visited = false;
        let row_data = row.querySelector("td:nth-child(" + col_index + ")").innerHTML
        for(let i = 0; i<selected.length; i++){
            let filter_value = selected[i];
            let display_row = true;
            if (row_data.indexOf(filter_value) == -1 && !row_visited) {
                display_row = false;
            }
            if (display_row) {
                row.style.display = "table-row";
                row_visited = "true";
                row_count = row_count + 1;
            } else {
                row.style.display = "none"
            }
        }
        if(row_count > 0){
            count = count + 1;
        }
    })
    let filter_count = document.querySelector(".table-object-count")
    filter_count.innerHTML = `Data Sources: ${count}`
}

$(document).ready(function() {
    let arrow_up = document.getElementById("arrow-up-0");
    let arrow_down = document.getElementById("arrow-down-0");
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    arrow_up = document.getElementById("arrow-up-1");
    arrow_down = document.getElementById("arrow-down-1");
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    showDomain();
});

// this function determines which domain options were checked
function showDomain() {
    let selected = [];
    if($("#filterMenu input:checked").length <= 0){
        $('#filterMenu input:checkbox').each(function() {
            selected.push($(this).attr('id'));
            $(this).prop("checked", "true");
        });
    }
    else{
        $('#filterMenu input:checked').each(function() {
            selected.push($(this).attr('id'));
            
        });
    }
    filter_row(selected);
}

// this function sorts the table based on either ID or Name
function sortTable(col_no) {
    let table = document.getElementById("ds-table");
    let direction = "asc";
    let table_switching = true;
    let asc_direction = false;
    let arrow_up = document.getElementById("arrow-up-"+col_no);
    let arrow_down = document.getElementById("arrow-down-"+col_no);
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    let rows = table.rows;
    while (table_switching) {
        table_switching = false;
        if (direction == "desc"){
            for (let i = 1; i <= (rows.length - 1); i++) {
                for (let j = 1; j <= (rows.length - i - 1); j++) {
                    let x = rows[j].getElementsByTagName("TD")[col_no];
                    let y = rows[j + 1].getElementsByTagName("TD")[col_no];
                    if(x.innerText.toLowerCase() < y.innerText.toLowerCase()){
                        rows[j].parentNode.insertBefore(rows[j + 1], rows[j]);
                    }
                }
            }
            arrow_up.style.display = "inline-block";
            arrow_down.style.display = "none";
        }
        else{
            for (let i = 1; i <= (rows.length - 1); i++) {
                for (let j = 1; j <= (rows.length - i - 1); j++) {
                    let x = rows[j].getElementsByTagName("TD")[col_no];
                    let y = rows[j + 1].getElementsByTagName("TD")[col_no];
                    if(x.innerText.toLowerCase() > y.innerText.toLowerCase()){
                        rows[j].parentNode.insertBefore(rows[j + 1], rows[j]);
                        asc_direction = true;
                    }
                }
            }
        }
        if (direction == "asc" && !asc_direction) {
            direction = "desc";
            table_switching = true;
        }
    }
}