function filter_row(selected) {
    col_index = 3
    const rows = document.querySelectorAll("#ds-table tbody tr");
    let count = 0;
    rows.forEach((row) => {
        let row_count = 0
        var row_visited = false;
        row_data = row.querySelector("td:nth-child(" + col_index + ")").innerHTML
        for(let i = 0; i<selected.length; i++){
            filter_value = selected[i];
            var display_row = true;
            if (row_data.indexOf(filter_value) == -1 && !row_visited) {
                display_row = false;
            }
            if (display_row == true) {
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
    filter_count = document.querySelector(".table-object-count")
    filter_count.innerHTML = `Data Sources: ${count}`
}

$(document).ready(function() {
    var arrow_up = document.getElementById("arrow-up-0");
    var arrow_down = document.getElementById("arrow-down-0");
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    arrow_up = document.getElementById("arrow-up-1");
    arrow_down = document.getElementById("arrow-down-1");
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    showDomain();
});
  
function showDomain() {
    var selected = [];
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

function sortTable(col_no) {
    var table = document.getElementById("ds-table");
    var direction = "asc";
    var table_switching = true;
    var asc_direction = false;
    var arrow_up = document.getElementById("arrow-up-"+col_no);
    var arrow_down = document.getElementById("arrow-down-"+col_no);
    arrow_down.style.display = "inline-block";
    arrow_up.style.display = "none";
    rows = table.rows;
    while (table_switching) {
        table_switching = false;
        if (direction == "desc"){
            for (let i = 1; i <= (rows.length - 1); i++) {
                for (let j = 1; j <= (rows.length - i - 1); j++) {
                    var x = rows[j].getElementsByTagName("TD")[col_no];
                    var y = rows[j + 1].getElementsByTagName("TD")[col_no];
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
                    var x = rows[j].getElementsByTagName("TD")[col_no];
                    var y = rows[j + 1].getElementsByTagName("TD")[col_no];
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