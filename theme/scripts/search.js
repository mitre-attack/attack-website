
$.ajax({
  url: "/index.json",
  dataType: "json",
  success: function (data) {
    idx = lunr.Index.load(data)
  }
})

$(document).keypress(
  function(e){
   if (e.which == '13') {
      e.preventDefault();
    }
});

function search(str) {
  if (str == "") {
    return
  }
  str = str.replace(/\s+$/, '')
  data = idx.search("*" + str + "*")
  data = data.concat(idx.search(str));

  if (data.length == 0) {
    $(".search-results").html("No results found.");
    return;
  }

  var categories = { "blog": [], "groups": [], "software": [], "tactics": [], "techniques": [] };

  $(".search-results").css('visibility', 'visible');
  $(".search-results").html("");

  var len = data.length;
  var upperBound;
  if (len < 10) {
    var upperBound  = len;
  } else {
    var upperBound = 10;
  }

  for (var i = 0; i < upperBound; i++) {
    var tokens = data[i]["ref"].split("|||");
    url = tokens[0];
    title = tokens[1];

    if (title.toLowerCase().includes(str.toLowerCase())) {
      highlightIdx = title.toLowerCase().indexOf(str.toLowerCase());
      if (highlightIdx == 0) {
        title = "<strong class='search-highlight'>" + title.substring(0, str.length) + "</strong>" + title.substring(str.length);
      } else if (highlightIdx == title.length - 1) {
        title = title.substring(0, title.toLowerCase().indexOf(str.toLowerCase())) + "<strong class='search-highlight'>" + title.substring(title.toLowerCase().indexOf(str.toLowerCase())) + "</strong>";
      } else {
        title = title.substring(0, title.toLowerCase().indexOf(str.toLowerCase())) + "<strong class='search-highlight'>" + title.substring(title.toLowerCase().indexOf(str.toLowerCase()), title.toLowerCase().indexOf(str.toLowerCase()) + str.length) + "</strong>" + title.substring(title.toLowerCase().indexOf(str.toLowerCase()) + str.length);
      }
    }

    for (var key in categories) {
      if (url.includes(key)) {
        categories[key].push("<a href='" + url + "'>" + title + "</a>");
      }
    }
  }

    for (var key in categories) {
      if (categories[key].length > 0) {
        $(".search-results").html($(".search-results").html() + "<span class='search-header'>" + key.charAt(0).toUpperCase() + key.slice(1) + "</span><hr class='search-divider' />");
        $(".search-results").append("<div class='" + key + "'></div>")
        // true if search term found in description
        var descriptionHeader = true;
        for (var i = 0; i < categories[key].length; i++) {
          if (categories[key][i].includes("search-highlight")) {
            // $(".search-results").html($(".search-results").html() + categories[key][i]);
            $("." + key).append(categories[key][i]);
          } else {
            if (descriptionHeader) {
              $(".search-results").html($(".search-results").html() + "<span class='text-muted'>Term found in description</span>");
            }
            descriptionHeader = false;
            $(".search-results").html($(".search-results").html() + categories[key][i]);
          }
          
        }
      }
    }
  }

$("#search").on('input keypress', function (e) {
  if (e.target.value != "") {
    clearTimeout(timeoutID);
    timeoutID = setTimeout(() => search(e.target.value), 500);
  } else {
    $(".search-results").css('visibility', 'hidden');
  }
});

$(window).click(function() {
  if(!$(event.target).closest('.search-results').length) {
    if($('.search-results').is(":visible")) {
        $('.search-results').css('visibility', 'hidden');
    }
  }
});

var timeoutID = null;