
//  Preloader
jQuery(window).on("load", function () {
    $('#preloader').fadeOut(500);
    $('#main-wrapper').addClass('show');
});


(function ($) {


    //  Header fixed
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.header').addClass("animated slideInDown fixed"), 3000;
        } else {
            $('.header').removeClass("animated slideInDown fixed"), 3000;
        }
    });

    $('select').niceSelect();

    $(function () {
        for (var nk = window.location,
            o = $(".menu a").filter(function () {
                return this.href == nk;
            })
                .addClass("active")
                .parent()
                .addClass("active"); ;) {
            // console.log(o)
            if (!o.is("li")) break;
            o = o.parent()
                .addClass("show")
                .parent()
                .addClass("active");
        }

    });

    $(function () {
        // var win_w = window.outerWidth;
        var win_h = window.outerHeight;
        var win_h = window.outerHeight;
        if (win_h > 0 ? win_h : screen.height) {
            $(".content-body").css("min-height", (win_h + 60) + "px");
        };
    });

    $('.sidebar-right-trigger').on('click', function () {
        $('.sidebar-right').toggleClass('show');
    });


})(jQuery);;




//ripple effect on button
Waves.init();
Waves.attach('.wave-effect');
Waves.attach('.btn');
Waves.attach('button');
