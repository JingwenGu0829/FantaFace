import { tns } from 'tiny-slider/src/tiny-slider';

const carousel = document.querySelectorAll('[data-carousel]');

carousel.forEach(function (element) {
    const settings = JSON.parse(element.dataset.carousel);

    settings.container = element;
    settings.controlsText = [
        '<i class="bi bi-arrow-left"></i>',
        '<i class="bi bi-arrow-right"></i>'
    ];

    tns(settings);
});