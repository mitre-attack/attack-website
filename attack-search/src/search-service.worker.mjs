/** service worker - runs on separate thread **/

// Import necessary modules and libraries
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate } from 'workbox-strategies';

import { SearchService } from './search-service.mjs';
import { baseURL, searchFilePaths, MessageType } from "./settings.mjs";
import databaseManager from "./db/database-manager.mjs";

// Declare search service variable
let build_uuid;
let searchService;

function getBuildUUIDFromURL() {
    const url = new URL(self.location);
    return url.searchParams.get('build_uuid');
}

// Helper function to fetch and parse JSON
async function fetchJSON(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
    }
    return await response.json();
}

function postMessageSafe(port, message) {
    try {
        port.postMessage(message);
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

// Initialize the search service
async function initializeSearchService() {
    console.debug('Initializing search service...');

    searchService = new SearchService();

    // Get the saved_uuid from the UUID database
    const saved_uuid = await databaseManager.uuidDb.get(0);
    console.debug(`Retrieved the saved_uuid from UUIDDatabase: ${saved_uuid}`);

    // Verify if the buildUUID is already cached in LocalStorage. This check is performed to determine if the search
    // service has been initialized. Each website build instance possesses a unique buildUUID, preventing different
    // website builds from sharing the same search index.
    if (saved_uuid && saved_uuid === build_uuid) {
        // Restore search service from IndexedDB
        try {
            console.debug('Initializing SearchService (assume documents already cached)...');
            await searchService.initializeAsync(null);
            console.debug('SearchService is initialized.');
        } catch (error) {
            console.error('Failed to initialize SearchService:', error);
            searchService = null;
        }
    } else {

        // Initialize search service from scratch
        console.debug('Documents not cached yet.');

        const baseUrl = `${baseURL}/search/`;
        const jsonFiles = [];

        // Download all JSON files from directory
        // Loop through the searchFilePaths array to construct the URLs
        searchFilePaths.forEach(function (filename) {
            jsonFiles.push(baseUrl + filename);
        });

        // Download all files concurrently
        Promise.all(jsonFiles.map(url => fetchJSON(url)))
            .then(async data => {
                // Concatenate all file data into a single array
                const combinedData = data.reduce((acc, curr) => acc.concat(curr), []);

                // Initialize search service with combined data
                return await searchService.initializeAsync(combinedData);
            })
            .then(async () => {
                // Save the build_uuid to the UUID database
                await databaseManager.uuidDb.put({ build_uuid: build_uuid });
                console.debug('Saved the build_uuid to UUIDDatabase.');
                console.debug('SearchService is initialized.');
            })
            .catch(error => {
                console.error('Failed to initialize SearchService:', error);
            });
    }
}

// Listen for messages from the main thread
self.addEventListener('message', async (event) => {
    console.debug('Service Worker received message: ', event);
    const { type, data } = event.data;
    try {
        switch (type) {
            case MessageType.SEARCH:
                console.debug(`Executing search: ${data}`);
                const results = await searchService.query(data);
                console.debug('Search Service returned results: ', results);
                postMessageSafe(event.ports[0], {
                    type: MessageType.SEARCH_RESULTS,
                    data: results
                });
                console.debug('Service Worker sent results to main thread.');
                break;
            default:
                console.warn('Unknown message type:', type);
                postMessageSafe(event.ports[0], {
                    type: MessageType.ERROR,
                    error: `Unknown message type: ${type}`
                });
                break;
        }
    } catch (error) {
        console.error('Error executing message:', error);
        postMessageSafe(event.ports[0], {
            type: MessageType.ERROR,
            error: error.message
        });
    }
});

// Perform the initialization during the service worker installation
self.addEventListener('install', (event) => {
    build_uuid = getBuildUUIDFromURL();
    event.waitUntil(initializeSearchService());
    console.debug('Service Worker: Installed');
});

// Force the service worker to take control immediately after activation
self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim());
    console.debug('Service Worker: Activated');
});

// Precache search JSON files
const searchFileURLs = searchFilePaths.map((filePath) => `${baseURL}/search/${filePath}`);
precacheAndRoute(searchFileURLs);

// Cache additional assets using StaleWhileRevalidate strategy
registerRoute(
    ({ request }) => request.destination === 'script' || request.destination === 'style',
    new StaleWhileRevalidate({
        cacheName: 'assets-cache'
    })
);
