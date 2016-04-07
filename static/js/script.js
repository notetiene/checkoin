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
            $('video.small').hide();
            $('video.hd').css('display', 'block');
        } else {
            $('video.hd').hide();
            $('video.small').css('display', 'block');
        }

        $('.tuco_bites_coin:visible').get(0).play();
        $('.they_carry_gold:visible').get(0).load();

        $('video:visible').each(function(k, v) {
            $(v).height($(v).width()*.425);
            // 0.425
        });

        scroll();
    }

    function play_show() { $("#play").show(); }

    $("#play").on('click', function() {
        $('.they_carry_gold:visible').get(0).play();
        $("#play").hide();
        $('.they_carry_gold:visible').off(play_show);
        $('.they_carry_gold:visible').on('ended', play_show);
    });

    // Chrome for smartphones requires user interaction to play medias.
    if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) &&
       /Chrome/i.test(navigator.appVersion)) {
        $('body').on('tap click swipe', function() {
            $('.tuco_bites_coin:visible').get(0).play();
        });
    }

    window_resize();
    $(window).resize(window_resize);

    $(window).on('scroll', scroll);

    $('h4').nextUntil('h4,h3,h2,h1').addClass('h4-siblings');
    $('strong:contains(before)').addClass('info');
});
