gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

if (ScrollTrigger.isTouch !== 1) {

    ScrollSmoother.create({
        wrapper: '.wrapper_ps',
        content: '.content_ps',
        smooth: 2,
        effects: true
    })

    gsap.fromTo('.hero-section', {opacity: 1}, {
        opacity: 0,
        scrollTrigger: {
            trigger: '.hero-section',
            start: 'center',
            end: '650',

            scrub: true
        }

    })

    gsap.fromTo('.doggo', {}, {
        
        scrollTrigger: {
            trigger: '.hero-section',
            start: 'center',

            scrub: true
        }

    })


}