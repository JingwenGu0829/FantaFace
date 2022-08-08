import noUiSlider from 'nouislider';

const elements = document.querySelectorAll('[data-range]');

elements.forEach(function (element) {
    const options = JSON.parse(element.dataset.range);
    const selectionMin = document.getElementById('range-min');
    const selectionMax = document.getElementById('range-max');

    noUiSlider.create(element, options);

    element.noUiSlider.on('update', function (values, handle) {
        if (handle) {
            selectionMax.innerHTML = values[handle];
        } else {
            selectionMin.innerHTML = values[handle];
        }
    });
});




