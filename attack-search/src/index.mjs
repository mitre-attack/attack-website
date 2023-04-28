/** main thread **/

import { Workbox } from 'workbox-window';
import { registerRoute } from "workbox-routing";
import { CacheFirst } from "workbox-strategies";
import { ExpirationPlugin } from "workbox-expiration";

import { SearchRenderer } from "./search-renderer.mjs";

// Create a service worker to handle search
if ('serviceWorker' in navigator) {

  let workbox;

  window.addEventListener('load', async () => {
    console.debug('Initializing the search module in a service worker.');

    try {
      const swURL = `/search_bundle.worker.js?build_uuid=${build_uuid}`;
      workbox = new Workbox(swURL);

      workbox.addEventListener('controlling', () => {
        console.debug('Service worker registered:', workbox);
      });

      await workbox.register();

      const searchRenderer = new SearchRenderer(workbox);
      searchRenderer.initializeEventHandlers();

      // Register a route to cache the search_bundle.worker.js file
      registerRoute(
          ({ url }) => url.pathname.startsWith('/search'),
          new CacheFirst({
            cacheName: 'scripts-cache',
            plugins: [
              new ExpirationPlugin({
                maxAgeSeconds: 60 * 60 * 24 * 30, // 30 Days
              }),
            ],
          })
      );

    } catch (error) {
      console.error('Failed to register service worker:', error);
    }
  });
  // Listen for controllerchange event to reinitialize search renderer
  navigator.serviceWorker.addEventListener('controllerchange', () => {
    console.debug('Service worker controlling a new page.');
    if (workbox){
      const searchRenderer = new SearchRenderer(workbox);
      searchRenderer.initializeEventHandlers();
    } else {
      console.warn('workbox not registered yet.');
    }
  });
}
else {
  console.warn('Service worker is not supported in this browser.');
}

// Log that search module is loaded
console.debug('search module is loaded.');
