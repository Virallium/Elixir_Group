function Loading(){
    const loading= document.querySelector('.loading')
    window.addEventListener("load", ()=>{
        setTimeout(() => {
           loading.classList.add('end_animation') 
        }, 1000);
    })
}
Loading()
/*==========================================
    Section gestion du skeleton Animation
 ===========================================*/






/************************
 Animation scroll change
************************/
function Scrolltap_screen(){
    const scrolltop=170
    const header = document.querySelector('header')
    window.addEventListener('scroll', ()=>{
        if (scrollY>scrolltop){
            header.classList.add('header_scrolled')
        }
        else{
            header.classList.remove('header_scrolled')
        }
    })
}
Scrolltap_screen()


function menu(){
    const menu_btn = document.getElementById('menu_btn')
    const nav = document.querySelector('nav')
    menu_btn.addEventListener('click', ()=>{
        nav.classList.toggle('active')
    })
}
menu()