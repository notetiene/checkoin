jQuery(document).ready(function($) {

    function scroll() {

        $('#float_column').outerWidth($('.col-md-3').outerWidth()-50);

        if($('.col-md-3').offset().top - $(window).scrollTop() < 20) {
            $('#float_column').css({'position': 'fixed', 'top': '20px'});
        } else {
            $('#float_column').css({'position': 'relative', 'top': ''});
        }
    }

    function window_resize() {

        // Hide the scroll bar to get actual viewport width.
        $('html').css('overflow-y', 'hidden');
        $('body').css('overflow-y', 'hidden');
        var w = $(window).width();
        $('html').css('overflow-y', '');
        $('body').css('overflow-y', '');

        if(w > 768) {
            $('video.hd').css('display', 'block');
            $('video.hd').get(0).play();
            $('video.hd').get(1).load();
            $('video.small').hide();
        } else {
            $('video.hd').hide();
            $('video.small').css('display', 'block');
            $('video.small').get(0).play();
            $('video.small').get(1).load();
        }

        scroll();
    }

    function play_show() { $("#play").show(); }

    $("#play").on('click', function() {
        $('.they_carry_gold:visible').get(0).play();
        $("#play").hide();
        $('.they_carry_gold:visible').off(play_show);
        $('.they_carry_gold:visible').on('ended', play_show);
    });

    window_resize();
    $(window).resize(window_resize);

    $(window).on('scroll', scroll);
});
