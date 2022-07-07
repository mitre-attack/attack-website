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
    "title": new FlexSearch({
        encode: "simple",
        //phonetic normalizations
        tokenize: "forward",
        //match substring beginning of word
        threshold: 50,
        //exclude scores below this number
        resolution: 50,
        //how many steps in the scoring algorithm
        depth: 4,
        //how far around words to search for adjacent matches. Disabled for title
        doc: {
          id: "id",
          field: "title"
        }
      }),
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
    var til = this.indexes.title;
    let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve(int.add(documents)))
  });
  let prom = new Promise((resolve, reject) => {
    setTimeout(() => resolve(til.add(documents)))
  });
  let result = await promise;
  let res = await prom;
  localforage.setItem("index_helper_content", int.export());
  localforage.setItem("index_helper_title", til.export());
  localStorage.setItem("forage_used", "true");
  localStorage.setItem("saved_uuid", build_uuid);
}
// when the document loads, position the body
$(document).ready(function() {
var saved_uuid = localStorage.getItem("saved_uuid");
if(localStorage.getItem("forage_used") != "true" || !saved_uuid || saved_uuid != build_uuid){
$.ajax({
        //if docs have not yet been loaded
        url: base_url + "index.json",
        dataType: "json",
        success: function success(data) {
          Indexer(data,null);
        }
      });
}
    
    positionBody();
    initSidenavScroll();
    $('[data-toggle="tooltip"]').tooltip();
});

// when the document resizes, position body
$(window).resize(function() {
    positionBody();;
});
