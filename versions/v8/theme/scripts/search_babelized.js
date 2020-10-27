function _instanceof2(left, right) { if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) { return !!right[Symbol.hasInstance](left); } else { return left instanceof right; } }

function _createForOfIteratorHelper(o, allowArrayLike) {
  var it;

  if (typeof Symbol === "undefined" || o[Symbol.iterator] == null) {
    if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") {
      if (it) o = it;
      var i = 0;

      var F = function F() {};

      return {
        s: F,
        n: function n() {
          if (i >= o.length) return {
            done: true
          };
          return {
            done: false,
            value: o[i++]
          };
        },
        e: function e(_e) {
          throw _e;
        },
        f: F
      };
    }

    throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
  }

  var normalCompletion = true,
      didErr = false,
      err;
  return {
    s: function s() {
      it = o[Symbol.iterator]();
    },
    n: function n() {
      var step = it.next();
      normalCompletion = step.done;
      return step;
    },
    e: function e(_e2) {
      didErr = true;
      err = _e2;
    },
    f: function f() {
      try {
        if (!normalCompletion && it.return != null) it.return();
      } finally {
        if (didErr) throw err;
      }
    }
  };
}

function _unsupportedIterableToArray(o, minLen) {
  if (!o) return;
  if (typeof o === "string") return _arrayLikeToArray(o, minLen);
  var n = Object.prototype.toString.call(o).slice(8, -1);
  if (n === "Object" && o.constructor) n = o.constructor.name;
  if (n === "Map" || n === "Set") return Array.from(o);
  if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen);
}

function _arrayLikeToArray(arr, len) {
  if (len == null || len > arr.length) len = arr.length;

  for (var i = 0, arr2 = new Array(len); i < len; i++) {
    arr2[i] = arr[i];
  }

  return arr2;
}

function _instanceof(left, right) {
  if (right != null && typeof Symbol !== "undefined" && right[Symbol.hasInstance]) {
    return !!right[Symbol.hasInstance](left);
  } else {
    return _instanceof2(left, right);
  }
}

function _classCallCheck(instance, Constructor) {
  if (!_instanceof(instance, Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
}

function _defineProperties(target, props) {
  for (var i = 0; i < props.length; i++) {
    var descriptor = props[i];
    descriptor.enumerable = descriptor.enumerable || false;
    descriptor.configurable = true;
    if ("value" in descriptor) descriptor.writable = true;
    Object.defineProperty(target, descriptor.key, descriptor);
  }
}

function _createClass(Constructor, protoProps, staticProps) {
  if (protoProps) _defineProperties(Constructor.prototype, protoProps);
  if (staticProps) _defineProperties(Constructor, staticProps);
  return Constructor;
}

var page_limit = 5; //number of results per page

var buffer = 200; //2* buffer is roughly the size of the result preview
// overlay container

var search_overlay = $("#search-overlay"); // button in header to open search

var search_open_trigger = $("#search-button"); // button to close search

var close_button = $("#close-search-icon"); // text input on search page

var search_input = $("#search-input"); // body of search results

var search_body = $("#search-body"); // button to show more results

var load_more_results = $("#load-more-results");
var load_more_results_button = $("#load-more-results-button"); // search parsing icon

var search_parsing_icon = $("#search-parsing-icon"); // register custom matchers globally

FlexSearch.registerMatcher({
  //attack and ATT&CK are equivalent for the purposes of search
  "ATT&CK": "ATTACK",
  "ATTACK": "ATT&CK"
});
var isChromium = window.chrome;
var isEdgeChromium = isChromium && navigator.userAgent.indexOf("Edg") != -1;
var isGoogleChrome = isChromium && !isEdgeChromium ? true : false;

var IndexHelper = /*#__PURE__*/function () {
  "use strict";

  function IndexHelper(documents, exported) {
    _classCallCheck(this, IndexHelper);

    this.indexes = {
      "title": new FlexSearch({
        encode: "simple",
        //phonetic normalizations
        tokenize: "forward",
        //match substring beginning of word
        threshold: 2,
        //exclude scores below this number
        resolution: 9,
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
        threshold: 2,
        //exclude scores below this number
        resolution: 9,
        //how many steps in the scoring algorithm
        depth: 4,
        //how far around words to search for adjacent matches. Disabled for title
        doc: {
          id: "id",
          field: "content"
        }
      })
    }; // console.log("adding pages to index");

    if (documents && !exported) {
      this.indexes.title.add(documents);
      this.indexes.content.add(documents);
      localStorage.setItem("saved_uuid", build_uuid);
      localforage.setItem("index_helper_title", this.indexes.title.export());
      localforage.setItem("index_helper_content", this.indexes.content.export());
    } else if (!documents && exported) {
      this.indexes.title.import(exported.title);
      this.indexes.content.import(exported.content);
    } else {
      console.error("invalid argument: constructor must be called with either documents or exported");
    }

    this.setQuery("");
  }

  _createClass(IndexHelper, [{
    key: "setQuery",
    value: function setQuery(query) {
      this.query = query;
      this.nextPageRef = true;
      this.titleStage = true;
      this.seenPaths = new Set();
    }
  }, {
    key: "nextPage",
    value: function nextPage() {
      var results = this.nextPageHelper();
      var self = this;
      results = results.filter(function (result) {
        return !self.seenPaths.has(result.path);
      });
      results.forEach(function (result) {
        self.seenPaths.add(result.path);
      }); // keep fetching until we have no more results or we have enough results

      while (results.length < page_limit) {
        var newResults = this.nextPageHelper(page_limit - results.length);
        if (newResults.length == 0) break; //ran out of results
        // cull duplicates

        newResults = newResults.filter(function (result) {
          return !self.seenPaths.has(result.path);
        });
        newResults.forEach(function (result) {
          self.seenPaths.add(result.path);
        }); // append to master list

        results = results.concat(newResults);
      }

      return results;
    }
    /**
     * Get the next page of results, or null if no more pages
     * @param {int} limit the number of results to get (default is the page_limit)
     */

  }, {
    key: "nextPageHelper",
    value: function nextPageHelper() {
      var limit = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : page_limit;

      if (!this.nextPageRef) {
        console.warn("no next page");
        return [];
      }

      if (this.titleStage) {
        // console.log("fetching next title page")
        var response = this.indexes.title.search(this.query, {
          limit: limit,
          page: this.nextPageRef
        });
        var results = response.result.map(function (result) {
          result.source = "title";
          return result;
        });

        if (response.next) {
          //next page exists on title stage
          this.nextPageRef = response.next;
          return results;
        } else {
          //end of title stage
          this.titleStage = false;
          this.nextPageRef = true;
          return results;
        }
      } else {
        //content stage
        // console.log("fetching next content page")
        var _response = this.indexes.content.search(this.query, {
          limit: limit,
          page: this.nextPageRef
        });

        this.nextPageRef = _response.next;
        return _response.result.map(function (result) {
          result.source = "content";
          return result;
        });
      }
    }
  }]);

  return IndexHelper;
}();

var SearchService = /*#__PURE__*/function () {
  "use strict";

  function SearchService(tag, documents, exported) {
    _classCallCheck(this, SearchService); // init indexes


    this.index = new IndexHelper(documents, exported);
    this.current_query = {
      clean: "",
      words: [
        /* 
         * { 
         *    word: the raw word
         *    regex: regular expression to find this word in the document
         * }
         */
      ],
      joined: "" //alternation

    };
    this.render_container = $("#" + tag);
  }
  /**
   * update the search (query) string
   * @param {str} querystr string to search for in the indexes
   */


  _createClass(SearchService, [{
    key: "query",
    value: function query(querystr) {
      this.current_query.clean = querystr.trim(); // build joined string

      var joined = "(" + this.current_query.clean.split(" ").join("|") + ")";
      this.current_query.joined = new RegExp(joined, "gi"); //build regex for each word

      var escaped = this.current_query.clean.replace(/\s+/, " "); //remove double spaces which causes query to match on every 0 length string and flip out

      this.current_query.words = escaped.split(" ").map(function (searchword) {
        var regexstr = searchword.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); //escape all regex chars so that entering ".." doesn't cause it to flip out

        regexstr = regexstr.replace(/((?:att&ck)|(?:attack))/gi, '((?:att&ck)|(?:attack))'); //equivalence of ATT&CK and attack

        return {
          word: searchword,
          regex: new RegExp(regexstr, "gi")
        };
      });
      this.index.setQuery(this.current_query.clean);
      this.clearResults();
      this.nextPage(); //render first page of results
    }
    /**
     * parse the result to the HTML required to render it
     * @param result object of format {title, path, content} which describes a page on the site
     */

  }, {
    key: "result_to_html",
    value: function result_to_html(result) {
      //create title and path
      var title = result.title;
      var path = base_url.slice(0, -1) + result.path;

      if (path.endsWith("/index.html")) {
        path = path.slice(0, -11);
      } // create preview html


      var preview = result.content; // Find a position where the search words occur near each other

      var positions = [];
      this.current_query.words.forEach(function (searchword) {
        var currMatches;

        while ((currMatches = searchword.regex.exec(preview)) !== null) {
          positions.push({
            index: searchword.regex.lastIndex,
            word: searchword.word
          });
        }
      });
      positions.sort(function (a, b) {
        return a.index - b.index;
      }); //are two sets equal

      function setsEqual(s1, s2) {
        if (s1.size !== s2.size) return false;

        var _iterator = _createForOfIteratorHelper(s1),
            _step;

        try {
          for (_iterator.s(); !(_step = _iterator.n()).done;) {
            var a = _step.value;
            if (!s2.has(a)) return false;
          }
        } catch (err) {
          _iterator.e(err);
        } finally {
          _iterator.f();
        }

        return true;
      }

      var allWords = new Set(this.current_query.words.map(function (word) {
        return word.word;
      }));
      var pos = 0;
      var best = {
        min: 0,
        max: 0,
        totalDist: Infinity,
        //distance between words
        totalFound: 0 //total number of words found

      };

      for (var i = 0; i < positions.length; i++) {
        var position = positions[i];
        var word = position.word;
        var index = position.index; // find out how far we have to go from this position to find all words

        var foundWords = new Set();
        foundWords.add(position.word);
        var totalDist = 0; //total distance between words for this combination

        var max = index; //leftmost word find

        var min = index; //rightmost word find

        if (setsEqual(allWords, foundWords)) {
          //1 word search
          best.min = index + 10;
          best.max = index - 10;
          break;
        } else {
          // search around this word
          for (var j = 0; i + j < positions.length || i - j > 0; j++) {
            // search j ahead
            var exceeded = 0;

            if (i + j < positions.length - 1) {
              var ahead = positions[i + j];
              var dist = ahead.index - index;

              if (dist > buffer) {
                //exceeded buffer
                exceeded++;
              } else if (!foundWords.has(ahead.word)) {
                // found a word
                foundWords.add(ahead.word);
                max = ahead.index;
                totalDist += ahead.index - index;
              }
            } //search j behind


            if (i - j >= 0) {
              var behind = positions[i - j];

              var _dist = index - behind.index;

              if (_dist > buffer) {
                //exceeded buffer
                exceeded++;
              } else if (!foundWords.has(behind.word)) {
                // found a word
                foundWords.add(behind.word);
                min = behind.index;
                totalDist += index - behind.index;
              }
            }

            if (setsEqual(allWords, foundWords) || exceeded == 2) {
              //found all the words in proximity, or both searches exceeded the buffer
              break;
            }
          }
        } //by now we must have found as many words as we can
        //total found words takes priority over the distance


        if (foundWords.size > best.totalFound || totalDist < best.totalDist && foundWords.size >= best.totalFound) {
          // new best
          best.totalDist = totalDist;
          best.max = max;
          best.min = min;
          best.totalFound = foundWords.size;
        }
      } // buffer around keyword


      var left = Math.max(0, best.min - buffer);
      var right = Math.min(preview.length, best.max + buffer);
      preview = preview.slice(left, right); //extract buffer
      // add elipses to preview so people know that the preview is not the complete page data

      if (right < result.content.length) preview += "&hellip;";
      if (left > 0) preview = "&hellip; " + preview; // surround preview keywords with highlight class span tags

      preview = preview.replace(this.current_query.joined, "<span class='search-word-found'>$1</span>"); // surround title keywords with highlight class span tags

      title = title.replace(this.current_query.joined, "<span class='search-word-found'>$1</span>"); // result html template

      return "\n            <div class=\"search-result mb-4\">\n                <div class=\"title\">\n                    <a href=\"".concat(path, "\">").concat(title, "</a>\n                </div>\n                <div class=\"preview\">\n                    ").concat(preview, "\n                </div>\n            </div>\n        "); //end template
    }
    /**
     * clear the rendered results from the page
     */

  }, {
    key: "clearResults",
    value: function clearResults() {
      this.render_container.html("");
      this.hasResults = false;
    }
    /**
     * render the next page of results if one exists
     */

  }, {
    key: "nextPage",
    value: function nextPage() {
      var results = this.index.nextPage();
      if (results.length > 0) this.hasResults = true;

      if (this.hasResults) {
        search_body.show();
        var self = this;
        var resultHTML = results.map(function (result) {
          return self.result_to_html(result);
        });
        resultHTML = resultHTML.join("");
        this.render_container.append(resultHTML);
        if (this.index.nextPageRef) load_more_results.show();else load_more_results.hide();
      } else {
        if (this.current_query.clean !== "") {
          //search with no results
          search_body.show();
          this.render_container.html("\n                    <div class=\"search-result\">no results</div>\n                ");
          load_more_results.hide();
        } else {
          // query for empty string
          search_body.hide();
        }
      }
    }
  }]);

  return SearchService;
}();

var openSearch = function openSearch() {
  // console.log("open search")
  search_body.hide();
  search_overlay.show();
  search_overlay.removeClass("hidden");
  search_input.focus();
};

var closeSearch = function closeSearch() {
  // console.log("close search")
  search_input.val('');
  search_overlay.hide();
  search_overlay.addClass("hidden");
};

var search_service = null;

var search = function search(query) {
  if (search_service == null) {
    search_parsing_icon.show(); // console.log("initializing search service")

    var saved_uuid = localStorage.getItem("saved_uuid");

    if (!isGoogleChrome && 'indexedDB' in window && saved_uuid && saved_uuid == build_uuid) {
      // console.log("getting cached flexsearch objects");
      localforage.getItem("index_helper_title").then(function (saved_title) {
        localforage.getItem("index_helper_content").then(function (saved_content) {
          exported = {
            title: saved_title,
            content: saved_content
          };
          search_service = new SearchService("search-results", null, exported);
          search_service.query(query);
          search_parsing_icon.hide();
        });
      });
    } else {
      // console.log("making new flexsearch objects");
      $.ajax({
        //if docs have not yet been loaded
        url: base_url + "index.json",
        dataType: "json",
        success: function success(data) {
          search_service = new SearchService("search-results", data, null);
          search_service.query(query);
          search_parsing_icon.hide();
        }
      });
    }
  } else {
    search_service.query(query);
  }
}; //utility class for debouncing function calls.
//used to debounce keyboard input so that rapid keypresses doesn't overwhelm the computer.


var Debouncer = /*#__PURE__*/function () {
  "use strict"; // new debouncer, param is the amount of debounce delay time in ms

  function Debouncer(delay) {
    _classCallCheck(this, Debouncer);

    this.callback = null;
    this.i = 0;
    this.delay = delay;
  } //callback with debounce


  _createClass(Debouncer, [{
    key: "debounce",
    value: function debounce(callback) {
      this.callback = callback;
      this.i++;
      var i = this.i;
      var self = this;
      setTimeout(function () {
        self.resolve(i);
      }, this.delay);
    } //resolve the debounced callback

  }, {
    key: "resolve",
    value: function resolve(i) {
      // only do the callback if a new debounced input hasn't been added.
      if (this.i == i) this.callback();
    }
  }]);

  return Debouncer;
}();

var debounce = new Debouncer(300); // triggers for closing search

search_overlay.on("click", function (e) {
  if (e.target != this) return; //don't close for children
  else closeSearch();
});
$(document).keyup(function (e) {
  e.key === 'Escape' ? closeSearch() : null;
});
close_button.on("click", closeSearch); // triggers for opening search

search_open_trigger.on("click", openSearch); // triggers for performing search functions

search_input.on("input", function (e) {
  debounce.debounce(function () {
    search(e.target.value);
  });
}); // trigger to render more results

load_more_results_button.on("click", function () {
  if (search_service) search_service.nextPage();
  load_more_results_button.blur(); //onfocus
}); //internet explorer compatability patches

if (!String.prototype.includes) {
  String.prototype.includes = function (search, start) {
    if (typeof start !== 'number') {
      start = 0;
    }

    if (start + search.length > this.length) {
      return false;
    } else {
      return this.indexOf(search, start) !== -1;
    }
  };
}

if (typeof String.prototype.endsWith !== 'function') {
  String.prototype.endsWith = function (suffix) {
    return this.indexOf(suffix, this.length - suffix.length) !== -1;
  };
}