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
        gsap.fromTo(item, { x: 100 }, {
            x: 0,
            scrollTrigger: {
                trigger: item,
                scrub: true
            }
    
        })
    })

}

document.addEventListener("DOMContentLoaded", function(){

    el_autohide = document.querySelector('.autohide');
    
    // add padding-top to bady (if necessary)
    navbar_height = document.querySelector('.navbar').offsetHeight;
    
  
    if(el_autohide){
      var last_scroll_top = 0;
      window.addEventListener('scroll', function() {
            let scroll_top = window.scrollY;
           if(scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            }
            else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');
            }
            last_scroll_top = scroll_top;
      }); 
      // window.addEventListener
    }
    // if
  
  }); 