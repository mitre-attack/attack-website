$(document).ready(function () {

    var domains = ['enterprise', 'mobile', 'pre-att&ck', 'pre-attack'];

    var joinLinkName = function(array) {
        array[1] = array[1] + "-" + array[2];
        for(var i = 2; i < array.length - 1; i++) {
            array[i] = array[i+1]
        }
        array[array.length] = "";
        array.length--;

        return array;
    };

    if(localStorage.getItem("needUpdate") === "true") {
        var activeObj = $(".nav-link.side.active.show");

        if(activeObj.attr('id').includes("-")) {
            var obj = activeObj.attr('id').split("-");

            if(obj.length > 4) {
                obj = joinLinkName(obj);
            }

            $(".expand-title").each(function () {
                var tmp = obj[0] + "-" + obj[2] + "-" + obj[3];
                if($(this).attr('id') === tmp) {
                    $(this).children("span:last-child").removeClass("glyphicon-minus");
                    $(this).children("span:last-child").addClass("glyphicon-plus");
                    return false;
                }
            });
            $(".collapse.show").removeClass("show");
            activeObj.removeClass("active show");
        }

        $(".nav-link.side").each(function () {
            if($(this).attr('id') === localStorage.getItem("newId")) {
                if ($(this).attr('id').includes("-")) {
                    obj = $(this).attr('id').split("-");

                    if(obj.length > 4) {
                        obj = joinLinkName(obj);
                    }

                    $(".expand-title").each(function () {
                        var tmp = obj[0] + "-" + obj[2] + "-" + obj[3];
                        if ($(this).attr('id') === tmp) {
                            $(this).children("span:last-child").removeClass("glyphicon-plus");
                            $(this).children("span:last-child").addClass("glyphicon-minus");

                            $(".collapse").each(function () {
                                if ($(this).attr('id') === obj[2]) {
                                    $(this).addClass("show");
                                    return false;
                                }
                            });
                            return false;
                        }
                    });
                    $(this).addClass("active show");
                }
                return false;
            }
        });
        localStorage.setItem("needUpdate", false);
    }

    $(".expand-title").each(function () {
        if ($(this).html().indexOf("All") == -1 || $(this).html().indexOf("Overview") == -1) {
            $(this).on("click", function () {
                // console.log($(this).children("span"))
                if ($(this).children("span").hasClass("glyphicon-plus")) {
                    $(this).children("span:last-child").removeClass("glyphicon-plus")
                    $(this).children("span:last-child").addClass("glyphicon-minus")
                }
                else if ($(this).children("span").hasClass("glyphicon-minus")){
                    $(this).children("span:last-child").removeClass("glyphicon-minus")
                    $(this).children("span:last-child").addClass("glyphicon-plus")
                }
            })
        }
    });

    $(".nav-link.side").click(function () {
        var oldLink = $(".nav-link.side.show.active").attr('id');
        var newLink = $(this).attr('id');

        if(oldLink && newLink) {
            if(oldLink.includes("-") && newLink.includes("-")) {
                var old_split = oldLink.split("-");
                var new_split = newLink.split("-");

                if(old_split.length > 4) {
                    old_split = joinLinkName(old_split);
                }

                if(new_split.length > 4) {
                    new_split = joinLinkName(new_split);
                }

                var text = $(this).text().toLowerCase();

                if(text !==  domains[0] && text !==  domains[1] && text !==  domains[2] && text !==  domains[3]) {
                    if(new_split.length > 3 && old_split.length > 3 ) {
                        if((old_split[1] === new_split[1] && old_split[2] !== new_split[2]) ||
                            (old_split[1] !== new_split[1] && old_split[2] === new_split[2]) ||
                            (old_split[1] !== new_split[1] && old_split[2] !== new_split[2])) {
                            localStorage.setItem("needUpdate", true);
                            localStorage.setItem("newId", newLink);
                        }
                    } else if(((old_split[1] === "{}" || new_split[1] === "{}")) && new_split.length > 2) {
                        localStorage.setItem("needUpdate", true);
                        localStorage.setItem("newId", newLink);
                    }
                }
            }
        }
    });

    $(".technique-mapping").click(function() {
        localStorage.setItem("needUpdate", true);
        localStorage.setItem("newId", $(this).attr('id'));
    });
});