const element = document.querySelectorAll('[data-countdown]');

element.forEach(function (item) {

    var x = setInterval(function () {
        var a = item.dataset.countdown;
        var b = new Date(a).getTime();
        var c = new Date().getTime();

        function numberLayout(n) {
            return n < 10 && n >= 0 ? "0" + n : n;
        }

        var diff = b - c;

        var d = Math.floor(diff / (1000 * 60 * 60 * 24));
        var h = Math.floor(diff % (1000 * 60 * 60 * 24) / (1000 * 60 * 60));
        var m = Math.floor(diff % (1000 * 60 * 60) / (1000 * 60));
        var s = Math.floor(diff % (1000 * 60) / 1000);

        d = numberLayout(d);
        h = numberLayout(h);
        m = numberLayout(m);
        s = numberLayout(s);

        const days = `<div class="countdown-item"><div class="countdown-value"><span>${d}</span> days</div></div>`;
        const hours = `<div class="countdown-item"><div class="countdown-value"><span>${h}</span> hours</div></div>`;
        const minutes = `<div class="countdown-item"><div class="countdown-value"><span>${m}</span> minutes</div></div>`;
        const seconds = `<div class="countdown-item"><div class="countdown-value"><span>${s}</span> seconds</div></div>`;

        item.innerHTML = days + hours + minutes + seconds;
    }, 10);

})