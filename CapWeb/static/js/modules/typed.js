import Typed from 'typed.js';

const elements = document.querySelectorAll('[data-typed]');

elements.forEach(function (element) {
    const elementOptions = JSON.parse(element.dataset.typed);
    const defaultOptions = {
        typeSpeed: 50,
        backSpeed: 40,
        backDelay: 1500,
        loop: true,
    };


    const options = {
        ...elementOptions,
        ...defaultOptions,
    };

    new Typed(element, options);
});