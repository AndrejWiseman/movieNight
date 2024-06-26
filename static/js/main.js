
const menuIcon = document.querySelector('nav .menu-ikona');
const mobileMenuItems = document.querySelector('nav .mobile-menu-elementi');

menuIcon.addEventListener('click', () => {
    mobileMenuItems.classList.toggle('active');
});


// Animacije

// Animacija da li je za mobilne telefone
let mobileMedia = gsap.matchMedia();

mobileMedia.add('(max-width: 800px)', () => {
    const timeLineMobile = gsap.timeline();

    timeLineMobile
        .from('#hero', {
        opacity: 0
    }, '+=.1')
        .from('nav', {
        y: -100,
        ease: 'expo.out',
        duration: '1.7',
    }, '-=.6')
        .from('nav .logo', {
        opacity: 0,
        duration: 1,

    }, '-=1')
        .from('nav .menu-ikona', {
        x: 30,
        opacity: 0,
        duration: 1
    }, '-=1')
        .from('.mobile-menu-elementi a', {
        opacity: 0,
        scale: 0.8,
        duration: 1.5,
        ease: 'elastic.out(1, .5)',
        stagger: 0.3
    }, '-=1')
})

mobileMedia.add('(min-width: 801px)', () => {
    const timeLineDesktop = gsap.timeline();

    timeLineDesktop
        .from('#hero', {
        opacity: 0
    }, '+=.1')
        .from('nav', {
        y: -100,
        ease: 'expo.out',
        duration: '1.7',
    }, '-=.6')
        .from('nav .logo', {
        opacity: 0,
        duration: 1,

    }, '-=1')
        .from('nav .meni-elementi a', {
        opacity: 0,
        scale: 0.8,
        duration: 1.5,
        ease: 'elastic.out(1, .5)',
        stagger: 0.3
    }, '-=1')

})

mobileMedia.add('(max-width: 800px)', () => {
    const tlMobile = gsap.timeline();
    tlMobile
        .from('.element', {
        opacity: 0,
        stagger: 0.3,
        duration: 1,
        ease: 'elastic.out(1, 0.5)'
    }, '-=0.1')
})

mobileMedia.add('(min-width: 801px)', () => {
    const tlMobile = gsap.timeline();
    tlMobile
        .from('.element', {
        opacity: 0,
        stagger: 0.2,
        duration: 0.7,
        ease: 'elastic.out(1, 0.5)'
    }, '-=0.1')
})






