import BigPicture from "bigpicture";

const bigPictureElements = document.querySelectorAll("[data-bp]");

bigPictureElements.forEach((bigPictureElement) => {
    const elementOptions = JSON.parse(bigPictureElement.dataset.bp);

    bigPictureElement.addEventListener("click", (e) => {
        let defaultOptions = {
            el: e.target,
            noLoader: true,
        };

        if (elementOptions.parentGalleryClass) {
            const galleryImages = document.querySelectorAll(
                `.${elementOptions.parentGalleryClass} [data-bp]`
            );

            let gallery = [];
            galleryImages.forEach((image) => {
                const imageOptions = JSON.parse(image.dataset.bp);
                const src = imageOptions.imgSrc;
                gallery.push({ src });
            });

            const position = gallery.findIndex(
                (item) => item.src === elementOptions.imgSrc
            );

            defaultOptions.gallery = gallery;
            defaultOptions.position = position;
        }

        BigPicture({
            ...defaultOptions,
            ...elementOptions,
        });
    });
});