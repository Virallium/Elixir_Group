// const { response } = require("express")

// self.addEventListener('install',(event)=>{
//     console.log('Installation complète')
//     const urlsToCache=[
//         '/static/style/style.css',
//         '/static/js/style.js',
//         '/static/photos/logo_transparent.png',
//         '/static/photos/logo_elixir.png',
//     ]
//     event.waitUntil(
//         caches.open("Elixir-V1-cache").then(cache=>{
//             return cache.addAll(urlsToCache)
//         })
    
//     )
// })
// self.addEventListener('activate',(event)=>{
//     console.log('Activation complète')

// })

// self.addEventListener('fetch',(event)=>{
//     console.log('Récupération de la ressource : '+event.request.url)
//     event.respondWidth(
//         caches.match(event.request).then(response =>{
//             if(response){
//                 console.log('Reponse du cache')
//             }
//             return response || fetch(event.request);
//         })
//     )
// })