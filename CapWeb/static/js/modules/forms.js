const elements = document.querySelectorAll('.grouped-inputs');

elements.forEach(function (element) {
    const elementInputs = element.querySelectorAll('input, select');


    elementInputs.forEach(function (input) {
        input.addEventListener('focus', function () {
            element.classList.add('focused');
        })

        input.addEventListener('blur', function () {
            element.classList.remove('focused');
        })
    });

});