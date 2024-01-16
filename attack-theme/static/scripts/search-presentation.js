function searchPresentation() {
    let count = 0;
    let input, input_uppercase, cards, card_value, displayed;
    displayed = true;
    input = document.getElementById("searchPresentation");
    input_uppercase = input.value.toUpperCase();
    cards = $(".card-presentation");
    if($("#filterMenu").length > 0){
        displayed = false;
        filterMenu();
    }
    for (let card of cards) {
        card_value = card.innerText;
        if (card_value.toUpperCase().indexOf(input_uppercase) > -1) {
            if((card.style.display != "none" && !displayed) || displayed){
                card.style.display = "";
                count = count + 1;
            }
        } else {
            card.style.display = "none";
        }
    }
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${count} of ${cards.length} Presentations`
}

function count_helper(card, selected, date, filter_value) {
    if (card.innerText.indexOf(filter_value) > -1 && card.style.display != "none") {
        if(selected[selected.length - 1].includes("year")){
            let filter_date = filter_date_helper(date);
            if (filter_date) {
                return 1;
            }
        }
        else{
            return 1;
        }
    }
    return 0;
}

function filter_all(selected) {
    let count = 0;
    let cards, i, dates;
    cards = $(".card-presentation");
    dates = $(".date");
    for (i = 0; i < cards.length; i++) {
        let row_count = 0
        for(let filters of selected){
            row_count += count_helper(cards[i], selected, dates[i], filters);
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

    for (let date_value of date_list) {
        if (!date_value.checked) continue;

        if(date_value.id.includes("1")){
            if(year-date_year <= 1){
                filter_date = true;
            }
        }
        else if(date_value.id.includes("3")){
            if(year-date_year <= 3){
                filter_date = true;
            }
        }
        else{
            filter_date = true;
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
    for (let card of cards) {
        card.style.display = "";
    }
    let selected_reversed = selected.toReversed()
    filter_all(selected_reversed);
}

$(document).ready(function() {
    let cards = $(".card-presentation");
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${cards.length} of ${cards.length} Presentations`
});