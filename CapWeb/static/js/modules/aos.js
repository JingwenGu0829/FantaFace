import AOS from 'aos';

AOS.init({
    duration: 800
});

function heightChange(elm, callback) {
    var lastHeight = elm.clientHeight
    var newHeight;

    (function run() {
        newHeight = elm.clientHeight;
        if (lastHeight !== newHeight) callback();
        lastHeight = newHeight;

        if (elm.heightChangeTimer) {
            clearTimeout(elm.heightChangeTimer);
        }

        elm.heightChangeTimer = setTimeout(run, 200);
    })();
}

heightChange(document.body, function () {
    AOS.refresh();
});