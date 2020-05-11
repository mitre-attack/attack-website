let json_data;

$(document).ready(function () {
    $.ajax({ //if docs have not yet been loaded
        url: site_base_url + "/random_page.json",
        dataType: "json",
        success: function (data) {
            json_data = data;

            for (category of Object.keys(data)) {
                let category_link = document.createElement("a");
                category_link.setAttribute("class", "dropdown-item");
                category_link.setAttribute("href", "#");
                category_link.setAttribute("onclick", "navigate_random('" + category + "');");
                category_link.appendChild(document.createTextNode(category[0].toUpperCase() + category.slice(1)));

                $('#div-random-page-dropdown').append(category_link);
            }
        }
    });
});

function navigate_random(category) {
    new_random_page = json_data[category][Math.floor(Math.random() * json_data[category].length)];
    window.location.href = new_random_page;
}