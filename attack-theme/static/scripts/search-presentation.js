function searchPresentation() {
    let count = 0;
    let input, input_uppercase, cards, i, card_value;
    input = document.getElementById("searchPresentation");
    input_uppercase = input.value.toUpperCase();
    cards = $(".card");
        for (i = 0; i < cards.length; i++) {
        card_value = cards[i].innerText;
        if (card_value.toUpperCase().indexOf(input_uppercase) > -1) {
            cards[i].style.display = "";
            count = count + 1;
        } else {
            cards[i].style.display = "none";
        }
    }
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${count} of ${cards.length} Presentations`
}

$(document).ready(function() {
    cards = $(".card");
    let filter_count = document.querySelector(".presentation-count")
    filter_count.innerHTML = `${cards.length} of ${cards.length} Presentations`
});