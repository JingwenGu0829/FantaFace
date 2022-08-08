import Plyr from "plyr"


const elements = document.querySelectorAll('[data-video]');

elements.forEach(function (element) {
    new Plyr(element);
});