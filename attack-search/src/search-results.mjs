// const Mutex = require('async-mutex').Mutex;
// const EventEmitter = require('events');
import { Mutex } from 'async-mutex';
import { EventEmitter } from 'events';

/**
 * Singleton class that manages the search results array.
 * @class SearchResults
 */
export class SearchResults extends EventEmitter {
    /**
     * Creates a new instance of the `SearchResults` class or returns an existing instance.
     * @constructor
     */
    constructor() {
        if (!SearchResults.instance) {
            super();
            /**
             * The array of search results.
             * @type {Array}
             */
            this.results = [];
            this.mutex = new Mutex();
            this.listeners = [];
            SearchResults.instance = this;
        }

        return SearchResults.instance;
    }

    /**
     * Adds an item to the `results` array.
     * @param {Object} item - The item to add to the array.
     */
    async add(item) {
        const release = await this.mutex.acquire();
        this.results.push(item);
        this.emit('resultsUpdated', this.results);
        release();
    }

    /**
     * Adds multiple items to the `results` array.
     * @param {Array} items - The items to add to the array.
     */
    async bulkAdd(items) {
        const release = await this.mutex.acquire();
        this.results.push(...items);
        this.emit('resultsUpdated', this.results);
        release();
    }

    /**
     * Removes an item from the `results` array.
     * @param {Object} item - The item to remove from the array.
     */
    async remove(item) {
        const release = await this.mutex.acquire();
        const index = this.results.indexOf(item);
        if (index !== -1) {
            this.results.splice(index, 1);
            this.emit('resultsUpdated', this.results);
        }
        release();
    }

    /**
     * Resets the `results` array to an empty array.
     */
    async reset() {
        const release = await this.mutex.acquire();
        this.results = [];
        this.emit('resultsUpdated', this.results);
        release();
    }

    /**
     * Alias for the `reset` method. Clears the `results` array.
     */
    clear() {
        this.reset();
    }
}
