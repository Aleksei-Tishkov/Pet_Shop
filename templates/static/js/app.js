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

    gsap.fromTo('.doggo', { }, {
        
        scrollTrigger: {
            trigger: '.hero-section',
            start: 'center',
            end: '600',

            scrub: true
        }

    })

    gsap.fromTo('.main_header', { }, {
        
        scrollTrigger: {
            trigger: '.main_header',
            start: 'center',
            end: '-300',
    
            scrub: true
        }

    })

    let itemsL = gsap.utils.toArray('.left__block .left__item')

    itemsL.forEach(item => {
        gsap.fromTo(item, { x: -100 }, {
            x: 0,
            scrollTrigger: {
                trigger: item,
                scrub: true
            }
    
        })
    })

    let itemsR = gsap.utils.toArray('.right__block .right__item')

    itemsR.forEach(item => {
        gsap.fromTo(item, { x: -100 }, {
            x: 0,
            scrollTrigger: {
                trigger: item,
                scrub: true
            }
    
        })
    })

    

}