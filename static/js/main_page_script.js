if (ScrollTrigger.isTouch !== 1) {

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
            end: '1600',

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
        gsap.fromTo(item, { x: -1000 }, {
            x: 0,
            scrollTrigger: {
                trigger: item,
                end: '-150',
                scrub: true
            }
    
        })
    })

    let itemsR = gsap.utils.toArray('.right__block .right__item')

    itemsR.forEach(item => {
        gsap.fromTo(item, { x: 1000 }, {
            x: 0,
            scrollTrigger: {
                trigger: item,
                end: '-150',
                scrub: true
            }
    
        })
    })

    let totalSection = document.querySelectorAll(".animate-heading")
    totalSection.forEach((char, index) => {
        
        gsap.from(char, {
            scrollTrigger: {
                trigger: char,
                scrub: true,
                start: "top 80%",
                end: "top 10%"
            },
            opacity: 0
            })
    })

}