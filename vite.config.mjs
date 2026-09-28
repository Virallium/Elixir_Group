import { defineConfig } from 'vite'
import { VitePWA } from 'vite-plugin-pwa'

export default defineConfig({
  base: '/',
  plugins: [VitePWA({
    registerType: 'autoUpdate',
    injectRegister: null,
    filename: 'sw.js',
    manifest: false,
    workbox: {
      globPatterns: ['**/*.{js,css,html,ico,png,svg,webp,woff2}'],
      inlineWorkboxRuntime: true,
      navigateFallback: null,
      modifyURLPrefix: {
        '': '/static/pwa-build/',
      },
      cleanupOutdatedCaches: true,
      runtimeCaching: [
        {
          urlPattern: ({ request, url }) => request.mode === 'navigate'
            && url.origin === self.location.origin
            && !/^\/(admin|administration|authentification)(\/|$)/.test(url.pathname),
          handler: 'NetworkFirst',
          options: {
            cacheName: 'elixir-public-pages',
            networkTimeoutSeconds: 3,
            expiration: {
              maxEntries: 40,
              maxAgeSeconds: 86400,
            },
            cacheableResponse: {
              statuses: [200],
            },
          },
        },
        {
          urlPattern: ({ url }) => url.origin === self.location.origin
            && url.pathname.startsWith('/static/'),
          handler: 'StaleWhileRevalidate',
          options: {
            cacheName: 'elixir-static-assets',
            expiration: {
              maxEntries: 200,
              maxAgeSeconds: 2592000,
            },
            cacheableResponse: {
              statuses: [0, 200],
            },
          },
        },
      ],
    },
    manifest: false,
  })],
  build: {
    outDir: 'static/pwa-build',
    emptyOutDir: true,
    rollupOptions: {
      input: 'static/js/pwa-register.js',
      output: { entryFileNames: 'pwa-register.js' },
    },
  },
})