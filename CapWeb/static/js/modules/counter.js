const elements = document.querySelectorAll('.counter');


elements.forEach(function (element) {
    const increment = element.querySelector('.counter-plus');
    const decrement = element.querySelector('.counter-minus');
    const input = element.querySelector('.counter-value');

    increment.addEventListener('click', function () {
        const inputValue = parseInt(input.value);

        if (!isNaN(inputValue)) {
            input.value = parseInt(input.value) + 1;
        } else {
            input.value = parseInt(0);
        }
    })

    decrement.addEventListener('click', function () {
        const inputValue = parseInt(input.value);

        if (!isNaN(inputValue) && inputValue > 0) {
            input.value = parseInt(input.value) - 1;
        } else {
            input.value = parseInt(0);
        }
    })

});