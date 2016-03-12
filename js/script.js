jQuery(document).ready(function($) {


    function window_resize() {

        // Hide the scroll bar to get actual viewport width.
        $('html').css('overflow-y', 'hidden');
        $('body').css('overflow-y', 'hidden');
        var w = $(window).width();
        $('html').css('overflow-y', '');
        $('body').css('overflow-y', '');
    }

    window_resize();
    $(window).resize(window_resize);

});
