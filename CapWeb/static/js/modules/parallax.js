import skrollr from "./skrollr.min";

window.onload = function () {
    // parallax
    skrollr.init({  
            forceHeight: false,        
            mobileCheck: function() {
                    return false;
            }
    });
};