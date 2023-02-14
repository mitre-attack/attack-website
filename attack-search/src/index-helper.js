import FlexSearch from "flexsearch";
import localforage from "localforage";
import {page_limit} from "./settings.js";

export class IndexHelper {

    constructor(documents, exported) {
        this.indexes = {
            "title": new FlexSearch.create({
                encode: "simple",     //phonetic normalizations
                tokenize: "forward",  //match substring beginning of word
                threshold: 2,         //exclude scores below this number
                resolution: 9,        //how many steps in the scoring algorithm
                depth: 4,             //how far around words to search for adjacent matches. Disabled for title
                doc: {
                    id: "id",
                    field: "title"
                }
            }),
            "content": new FlexSearch.create({
                encode: "simple",     //phonetic normalizations
                tokenize: "strict",  //match substring beginning of word
                threshold: 2,        //exclude scores below this number
                resolution: 9,       //how many steps in the scoring algorithm
                depth: 4,            //how far around words to search for adjacent matches. Disabled for title
                doc: {
                    id: "id",
                    field: "content"
                }
            })
        }

        // Adding pages to index
        if (documents && !exported) {
            this.indexes.title.add(documents);
            this.indexes.content.add(documents);

            localStorage.setItem("saved_uuid", build_uuid);
            localforage.setItem("index_helper_title", this.indexes.title.export(() => {
            }))
                .then(() => {
                });
            localforage.setItem("index_helper_content", this.indexes.content.export(() => {
            }))
                .then(() => {
                });

        } else if (!documents && exported) {
            this.indexes.title.import(exported.title);
            this.indexes.content.import(exported.content);
        } else {
            console.error("invalid argument: constructor must be called with either documents or exported");
        }

        this.setQuery("");
    }

    setQuery(query) {
        this.query = query;
        this.nextPageRef = true;
        this.titleStage = true;
        this.seenPaths = new Set();
    }

    nextPage() {
        let results = this.nextPageHelper();
        let self = this;
        results = results.filter(function (result) {
            return !self.seenPaths.has(result.path)
        });
        results.forEach(function (result) {
            self.seenPaths.add(result.path)
        });

        // keep fetching until we have no more results or we have enough results
        while (results.length < page_limit) {
            let newResults = this.nextPageHelper(page_limit - results.length);
            if (newResults.length == 0) break; //ran out of results
            // cull duplicates
            newResults = newResults.filter(function (result) {
                return !self.seenPaths.has(result.path)
            });
            newResults.forEach(function (result) {
                self.seenPaths.add(result.path)
            });
            // append to master list
            results = results.concat(newResults);
        }

        return results;
    }

    /**
     * Get the next page of results, or null if no more pages
     * @param {int} limit the number of results to get (default is the page_limit)
     */
    nextPageHelper(limit = page_limit) {
        if (!this.nextPageRef) {
            console.warn("no next page")
            return []
        }

        if (this.titleStage) {
            // console.log("fetching next title page")
            let response = this.indexes.title.search(this.query, {
                limit: limit,
                page: this.nextPageRef
            });
            let results = response.result.map(function (result) {
                result.source = "title";
                return result;
            });

            if (response.next) { //next page exists on title stage
                this.nextPageRef = response.next;
                return results;
            } else { //end of title stage
                this.titleStage = false;
                this.nextPageRef = true;
                return results;
            }
        } else { //content stage
            // console.log("fetching next content page")
            let response = this.indexes.content.search(this.query, {
                limit: limit,
                page: this.nextPageRef
            });
            this.nextPageRef = response.next;
            return response.result.map(function (result) {
                result.source = "content";
                return result;
            });
        }

    }
}
