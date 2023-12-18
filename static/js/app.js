gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

if (ScrollTrigger.isTouch !== 1) {

    ScrollSmoother.create({
        wrapper: '.wrapper_ps',
        content: '.content_ps',
        smooth: 4,
        effects: true
    })

    if (document.getElementById("right_side")) {
        ScrollTrigger.create({    
            trigger: '.content_ps',
            start: 'top top',
            pin: '.right_side',
            pinSpacing: false    
          })

    }

};

document.addEventListener("DOMContentLoaded", function(){

    el_autohide = document.querySelector('.autohide');

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
    }
  
  }); 


  