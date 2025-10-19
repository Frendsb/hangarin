const CACHE_NAME = 'hangarin-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/static/css/bootstrap.min.css',
  '/static/js/demo.js'
];

// Install event
self.addEventListener('install', event => {
  console.log('Service Worker installing...');
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return Promise.all(
        ASSETS_TO_CACHE.map(url =>
          cache.add(url).catch(err => console.warn('Failed to cache', url, err))
        )
      );
    })
  );
});

// Fetch event (serve cached files)
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

// Activate event (clear old caches)
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
  console.log('Service Worker activated.');
});
