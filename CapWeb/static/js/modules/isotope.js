

import imagesLoaded from 'imagesloaded';
import Isotope from 'isotope-layout';


const layout = document.querySelectorAll('[data-isotope]');
const filter = document.querySelectorAll('[data-filter]');


// filtration
filter.forEach(function (element) {
    element.addEventListener("click", () => {
        const value = element.dataset.filter;
        const target = element.dataset.target;
        const siblings = element.parentNode.querySelectorAll('button');

        for (var i = 0; i < siblings.length; i++) {
            siblings[i].classList.remove('current');
        }
        element.classList.add('current');

        Isotope.data(target).arrange({
            filter: value,
        })
    })
})


// layout
layout.forEach(function (element) {
    imagesLoaded(element, function () {
        new Isotope(element);
    });
})