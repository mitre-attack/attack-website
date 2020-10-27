let json_data;
let all_pages = [];

$(document).ready(function () {
    $.ajax({ //if docs have not yet been loaded
        url: base_url + "random_page.json",
        dataType: "json",
        success: function (data) {
            json_data = data;

            for (route of Object.keys(json_data)) {
                all_pages = all_pages.concat(json_data[route]);
            }
        }
    });
});

function navigate_random(category) {
    let new_random_page;
    if (category) {
        new_random_page = json_data[category][Math.floor(Math.random() * json_data[category].length)];
    }
    else {
        new_random_page = all_pages[Math.floor(Math.random() * all_pages.length)];
    }
    window.location.href = new_random_page;
}