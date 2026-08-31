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
    if (!menu_btn || !nav) return;
    menu_btn.addEventListener('click', ()=>{
        nav.classList.toggle('active')
    })
}
menu()

function applyGlobalAOS(){
    if (typeof AOS === 'undefined') return;

    const animatedGroups = document.querySelectorAll('.page-hero, .content-section, .box, .admin-panel, .admin-stat-card, .contact-layout, .contact-form, .admin-event-row, .admin-people-list li, .boxs > .box');

    animatedGroups.forEach((element, index) => {
        if (element.hasAttribute('data-aos')) return;

        if (element.classList.contains('page-hero')) {
            element.setAttribute('data-aos', 'fade-up');
            element.setAttribute('data-aos-delay', String(index * 80));
            return;
        }

        if (element.classList.contains('contact-form') || element.classList.contains('contact-layout')) {
            element.setAttribute('data-aos', 'fade-left');
            element.setAttribute('data-aos-delay', String(index * 80));
            return;
        }

        if (element.classList.contains('admin-panel') || element.classList.contains('admin-stat-card')) {
            element.setAttribute('data-aos', 'zoom-in');
            element.setAttribute('data-aos-delay', String(index * 70));
            return;
        }

        element.setAttribute('data-aos', 'fade-up');
        element.setAttribute('data-aos-delay', String(index * 60));
    });

    AOS.init({
        duration: 700,
        once: false,
        offset: 30,
        easing: 'ease-out-cubic',
        mirror: true
    });
}

applyGlobalAOS();

function prevent_navlinks(){
    const links = document.querySelectorAll('.plus')
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
        });
    });
}
prevent_navlinks()