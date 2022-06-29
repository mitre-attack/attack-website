// position body according to header size
function positionBody() {
    let headerHeight = $(".navbar").outerHeight();
    let viewportHeight = $(".attack-website-wrapper").outerHeight();
    let sidebarHeight = viewportHeight - headerHeight + "px";
    $(".sidebar.nav").css({
        "top": headerHeight + "px",
        "max-height": viewportHeight - headerHeight + "px"
    });
}

//scroll the active element into view in the sidenav
function initSidenavScroll() {
    let sidenav = $(".sidenav-list");
    let sidenav_active_elements = $(".sidenav .active");
    if (sidenav_active_elements.length > 0) setTimeout(() => { //setTimeout gives bootstrap time to execute first
        sidenav[0].scrollTop = sidenav_active_elements[0].offsetTop - 60;
    });
}
async function Indexer(documents, exported) {
    this.indexes = {
      "content": new FlexSearch({
        encode: "simple",
        //phonetic normalizations
        tokenize: "strict",
        //match substring beginning of word
        threshold: 50,
        //exclude scores below this number
        resolution: 50,
        //how many steps in the scoring algorithm
        depth: 4,
        //how far around words to search for adjacent matches. Disabled for title
        doc: {
          id: "id",
          field: "content"
        }
      })
    }; // console.log("adding pages to index");
    
    var int = this.indexes.content;
    let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve(int.add(documents)))
  });
  let result = await promise;
  localforage.setItem("index_helper_content", int.export());
    //alert("hi");
}
// when the document loads, position the body
$(document).ready(function() {
    $.ajax({
        //if docs have not yet been loaded
        url: base_url + "index.json",
        dataType: "json",
        success: function success(data) {
          Indexer(data,null);
        }
      });
    positionBody();
    initSidenavScroll();
    $('[data-toggle="tooltip"]').tooltip();
});

// when the document resizes, position body
$(window).resize(function() {
    positionBody();;
});
