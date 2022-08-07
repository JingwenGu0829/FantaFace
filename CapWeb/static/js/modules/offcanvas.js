
const elements = document.querySelectorAll('.offcanvas');
const body = document.querySelector("body");

elements.forEach(function (element) {
    element.addEventListener('show.bs.offcanvas', function () {
        body.classList.add('offcanvas-push');
    })

    element.addEventListener('hide.bs.offcanvas', function () {
        body.classList.remove('offcanvas-push');
    })
})

