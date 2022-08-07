const navbar = document.querySelectorAll('.navbar');
const body = document.body;

navbar.forEach(function (element) {
    element.addEventListener('hide.bs.collapse', function () {
        body.classList.remove('navbar-active');
    })
    element.addEventListener('show.bs.collapse', function () {
        setTimeout(() => {
            body.classList.add('navbar-active');
        }, 0)
    })
})

