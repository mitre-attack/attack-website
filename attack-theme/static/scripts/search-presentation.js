function searchPresentation() {
    let count = 0;
    let input, input_uppercase, cards, i, card_value, displayed, card_display;
    displayed = true;
    card_display = false;
    input = document.getElementById("searchPresentation");
    input_uppercase = input.value.toUpperCase();
    cards = $(".card-presentation");
    if($("#filterMenu").length > 0){
        displayed = false;
        filterMenu();
    }
    for (i = 0; i < cards.length; i++) {
        card_value = cards[i].innerText;
        if (card_value.toUpperCase().indexOf(input_uppercase) > -1) {
            if(cards[i].style.display != "none" && !displayed){
                card_display = true;
            }
            else if(displayed){
                card_display = true;
            }
            if(card_display){
                cards[i].style.display = "";
                count = count + 1;
                card_display = false;
            }
        } else {
            cards[i].style.display = "none";
        }
    }
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${count} of ${cards.length} Presentations`
}

function filter_all(selected) {
    let count = 0;
    let cards, i, card_value, dates;
    cards = $(".card-presentation");
    dates = $(".date");
    for (i = 0; i < cards.length; i++) {
        card_value = cards[i].innerText;
        let row_count = 0
        for(let j = 0; j<selected.length; j++){
            let filter_value = selected[j];
            if (card_value.indexOf(filter_value) > -1 && cards[i].style.display != "none") {
                if(selected[selected.length - 1].includes("year")){
                    let filter_date = filter_date_helper(dates[i])
                    if(filter_date){
                        row_count = row_count + 1;
                    }
                }
                else{
                    row_count = row_count + 1;
                }
            }
        }
        if(row_count > 0){
            cards[i].style.display = "";
            count = count + 1;
        }
        else {
            cards[i].style.display = "none";
        }
    }
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${count} of ${cards.length} Presentations`
}

function filter_date_helper(input_date) {
    let currentDate = new Date();
    let year, date_year;
    let filter_date = false;
    let date_list = document.getElementsByName('dates');
    year = currentDate.getFullYear();
    date_year = input_date.innerText.split(" ")[1];
    for (let j = 0; j < date_list.length; j++) {
        if (date_list[j].checked){
            if(date_list[j].id.includes("Current")){
                if(year-date_year == 0){
                    filter_date = true;
                }
            }
            else if(date_list[j].id.includes("3")){
                if(year-date_year == 3){
                    filter_date = true;
                }
            }
            else{
                filter_date = true;
            }
        }
    }
    return filter_date;
}

function filterMenu() {
    let selected = [];
    if($("#filterMenu input:checked").length <= 0){
        $('#filterMenu input:checkbox').each(function() {
            if($(this).attr('id').includes("-")){
                selected.push($(this).attr('id').replaceAll("-"," "));
            }
            else{
                selected.push($(this).attr('id'))
            }
            $(this).prop("checked", "true");
        });
    }
    else{
        $('#filterMenu input:checked').each(function() {
            if($(this).attr('id').includes("-")){
                selected.push($(this).attr('id').replaceAll("-"," "));
            }
            else{
                selected.push($(this).attr('id'))
            }
        });
    }
    let cards = $(".card-presentation");
    for (let i = 0; i < cards.length; i++) {
        cards[i].style.display = "";
    }
    let selected_reversed = selected.toReversed()
    filter_all(selected_reversed);
}

$(document).ready(function() {
    cards = $(".card-presentation");
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${cards.length} of ${cards.length} Presentations`
});