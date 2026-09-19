const CACHE_NAME = 'Elixir-static-v1';
const STATIC_ASSETS = [
    '/static/style/style.css',
    '/static/js/style.js',
    '/static/photos/logo_transparent.png',
    '/static/photos/logo_elixir.png',
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(STATIC_ASSETS))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => Promise.all(
            cacheNames
                .filter((cacheName) => cacheName !== CACHE_NAME)
                .map((cacheName) => caches.delete(cacheName))
        )).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    const requestUrl = new URL(event.request.url);

    if (event.request.method !== 'GET' || requestUrl.origin !== self.location.origin) {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                if (response.ok && requestUrl.pathname.startsWith('/static/')) {
                    const responseCopy = response.clone();
                    caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseCopy));
                }
                return response;
            })
            .catch(() => caches.match(event.request).then((cachedResponse) => cachedResponse || caches.match('/')))
    );
});