gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

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
;

document.addEventListener("DOMContentLoaded", function () {

    el_autohide = document.querySelector('.autohide');

    navbar_height = document.querySelector('.navbar').offsetHeight;


    if (el_autohide) {
        var last_scroll_top = 0;
        window.addEventListener('scroll', function () {
            let scroll_top = window.scrollY;
            if (scroll_top < last_scroll_top) {
                el_autohide.classList.remove('scrolled-down');
                el_autohide.classList.add('scrolled-up');
            } else {
                el_autohide.classList.remove('scrolled-up');
                el_autohide.classList.add('scrolled-down');
            }
            last_scroll_top = scroll_top;
        });
    }

});

document.addEventListener('DOMContentLoaded', (e) => {
    let addButtons = document.getElementsByClassName("add_to_cart");
    for (let index = 0; index < addButtons.length; index++) {
        modalForm(addButtons[index], {
            formURL: addButtons[index]["dataset"]["formUrl"]
        });
    }
});


document.addEventListener('DOMContentLoaded', (e) => {
    let addButtons = document.getElementsByClassName("edit_cart");
    for (let index = 0; index < addButtons.length; index++) {
        modalForm(addButtons[index], {
            formURL: addButtons[index]["dataset"]["formUrl"]
        });
    }
});


document.addEventListener('DOMContentLoaded', (e) => {
    modalForm(document.getElementById('clear-cart'), {
        formURL: "clear_cart/"
    })
});

let constrain = 20;
let mouseOverContainer = document.getElementById('card-row');
let card_wrappers = document.getElementsByClassName('card__wrapper');
let cards = document.getElementsByClassName('card');

function transforms(x, y, el) {
    let box = el.getBoundingClientRect();
    let calcX = -(y - box.y - (box.height / 2)) / constrain / 50;
    let calcY = (x - box.x - (box.width / 2)) / constrain / 50;

    return "perspective(100px) "
        + "   rotateX(" + calcX + "deg) "
        + "   rotateY(" + calcY + "deg) ";
};

function translateZ(el) {
    el.style.transform = 'translateZ(10px)'
}

function transformElement(el, xyEl) {
    el.style.transform = transforms.apply(null, xyEl);
};

mouseOverContainer.onmousemove = function (e) {
    for (let idx = 0; idx < cards.length; idx++) {
        let position = [e.clientX, e.clientY].concat([cards[idx]]);
        window.requestAnimationFrame(function () {
            transformElement(cards[idx], position);
        });
    }
};
