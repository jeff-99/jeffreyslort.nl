function setup_cv_blokken(){
    $(".roll-with-description.hide").each(function(){
        $(this).each(function(){
            $(this).find(".description").css('display','none');
        });
    });

    $(".roll-with-description.show").each(function(){
        $(this).each(function(){
            $(this).find(".description").css('display','block');
        });
    });

    $(".roll-with-description").each(function(){
        $(this).click(function(){
            var speed = 600;
            if ($(this).hasClass("show")) {
                $(this).removeClass("show");
                $(this).find(".description").slideUp(speed);
                setTimeout($(this).addClass("hide"), speed);

            }
            else if ($(this).hasClass("hide")) {
                $(this).removeClass("hide");
                $(this).find(".description").slideDown(speed);
                setTimeout($(this).addClass("show"), speed);
            }
        });
    });
}

/* AJAX LOADING */
$(document).on({
    ajaxStart: function() { $("#container").addClass("loading");    },
     ajaxStop: function() { $("#container").removeClass("loading"); },
    ajaxComplete: function(){
        /* fix voor de cv pagina */
        setup_cv_blokken();
    }
});
/* END AJAX LOADING */

$(document).ready(function(){
    /* ---------------------------------------------------------------------- */
    /*	Portfolio Page
    /* ---------------------------------------------------------------------- */
    var $portfoliocontainer	 	= $('#portfolio-container');
    var $portfoliofilter 		= $('#portfolio-menu');

    $portfoliocontainer.isotope({
        filter				: '*',
        layoutMode   		: 'masonry',
        animationOptions	: {
            duration		: 600,
            easing			: 'linear'
        }
    });

    $portfoliofilter.find('a').click(function(){
        var selector = $(this).attr('data-filter');
        $portfoliocontainer.isotope({
            filter				: selector,
            animationOptions	: {
                duration		: 600,
                easing			: 'linear',
                queue			: false
            }
        });
        return false;
    });

    $portfoliocontainer.find('img').adipoli({
        'startEffect' 	: 'transparent',
        'hoverEffect' 	: 'boxRandom',
        'imageOpacity' 	: 0.5,
        'animSpeed' 	: 100
    });

    $portfoliofilter.find('a').click(function() {
        var currentOption = $(this).attr('data-filter');
        $portfoliofilter.find('a').removeClass('current');
        $(this).addClass('current');
    });

    $(".popup").fancybox({
        openEffect	: 'fade',
        closeEffect	: 'fade',
        scrolling   : 'no',
        fitToView   : false,
        autoResize  : true,
        aspectRation: false,
        keys    :   {
            next   : {
                13 : 'left', // enter
                34 : 'up',   // page down
                39 : 'left', // right arrow
                40 : 'up'    // down arrow
            },
            prev : {
                8  : 'right',  // backspace
                33 : 'down',   // page up
                37 : 'right',  // left arrow
                38 : 'down'    // up arrow
            },
            close  : [27], // escape key
            play   : [32], // space - start/stop slideshow
            toggle : [70]  // letter "f" - toggle fullscreen
        }
    });

    /* ---------------------------------------------------------------------- */
    /*	Progressbar load page
    /* ---------------------------------------------------------------------- */
    $(".progressbar > span").each(function() {
        var bar = $(this);
        var level = $(this).attr('level');
        bar.width(0);
        bar.animate({
            width: level+'%'
        }, 800);
    });
    /* ---------------------------------------------------------------------- */
    /*	Tabs Menu Major
    /* ---------------------------------------------------------------------- */
    var $tabscontainer = $("#wrapper");

    $tabscontainer.easytabs({
        animate			: true,
        updateHash		: true,
        transitionIn	: 'slideDown',
        transitionOut	: 'slideUp',
        animationSpeed	: 600,
        tabActiveClass	: 'active',
        tabs: 'li.tab'
    });
     /*    Progressbar load swich tabs     */
    $tabscontainer.bind('easytabs:midTransition', function() {
        $(".progressbar > span").each(function() {
            var bar = $(this);
            var level = $(this).attr('level');
            bar.width(0);
            bar.animate({
                width: level+'%'
            }, 800);
        });
    /* This script used only to demonstrate blog page. hide blog page - show blog content when switch tabs */
    $tabscontainer.bind('easytabs:after', function() {
        $(".blog-footer").show();
        $(".blog-content").show();
        $("#blog .content > h2").show();
        $("#blog-post").hide();
    });
    /* End */
    /* ---------------------------------------------------------------------- */
    /*	Google Maps
    /* ---------------------------------------------------------------------- */
    var $map 				= $('#map'),
        $blog               = $('#blog'),
        $tabContactClass 	= ('contacts'),
        $address 			= $("#contact-address").html();

        $tabscontainer.bind('easytabs:after', function(evt,tab,panel) {
            if ( tab.hasClass($tabContactClass) ) {
                $map.gMap({
                    address: $address,
                    zoom: 16,
                    markers: [
                        { 'address' : $address }
                    ]
                });
            }
        });
    });
    /* ---------------------------------------------------------------------- */
    /*	Documents Page
    /* ---------------------------------------------------------------------- */
    $("#documents > .content").easytabs({
        animate			: true,
        updateHash		: true,
        transitionIn	: 'slideDown',
        transitionOut	: 'slideUp',
        animationSpeed	: 600,
        tabActiveClass	: 'active'
    });

    $("#pictures").find('img').adipoli({
        'startEffect' 	: 'transparent',
        'hoverEffect' 	: 'boxRandom',
        'imageOpacity' 	: 0.5,
        'animSpeed' 	: 100
    });
    /* ---------------------------------------------------------------------- */
    /*	ProgressBar Show/Hide Description
    /* ---------------------------------------------------------------------- */
    /* functie wordt boven gedeclared, fix voor de ajax requests */
    setup_cv_blokken();
    /* ---------------------------------------------------------------------- */
    /*	Block Show/Hide Description
    /* ---------------------------------------------------------------------- */
    $(".hidden").each(function(){
        $(this).each(function(){
            $(this).find(".block-content").css('display','none');
        });
    });

    $(".showing").each(function(){
        $(this).each(function(){
            $(this).find(".block-content").css('display','block');
        });
    });

    /* ---------------------------------------------------------------------- */
    /*	Blog
    /* ---------------------------------------------------------------------- */
   /* var $blogcontainer = $("#blog > .content-inner");

    $blogcontainer.easytabs({
        animate			: true,
        updateHash		: true,
        transitionIn	: 'slideDown',
        transitionOut	: 'slideUp',
        animationSpeed	: 600,
        tabActiveClass	: 'active',
        tabs: "> div.right-sidebar > div#categories > div.block-content > ul > li",
        defaultTab: "li.last"
    });

    $blogcontainer.find('img').adipoli({
        'startEffect' 	: 'transparent',
        'hoverEffect' 	: 'boxRandom',
        'imageOpacity' 	: 0.5,
        'animSpeed' 	: 100
    });
    /* This script used only to demonstrate blog page. hide blog content - show blog page */
    /*$("a.blog-post").click(function(){
        $(".blog-footer").hide();
        $("#blog .content > h2").hide();
        $(".blog-content").slideUp(600);
        $("#blog-post").slideDown(600);
    });
    /* back link. hide blog page - show blog content */
    /*$("a.back").click(function(){
        $(".blog-content").slideDown(600);
        $("#blog-post").slideUp(600);
        $(".blog-footer").show();
        $("#blog .content > h2").show();
    });




    /* ---------------------------------------------------------------------- */
    /*	Comment blog Form
     /* ---------------------------------------------------------------------- */

    // Needed variables
    var $commentform 	= $('#comment'),
        $success		= 'Thank you! Your comment has been sent.';

    $commentform.submit(function(){
        $.ajax({
            type: "POST",
            url: "php/comment.php",
            data: $(this).serialize(),
            success: function(msg)
            {
                if(msg == 'SEND'){
                    response = '<div class="status-success">'+ $success +'</div>';
                }
                else{
                    response = '<div class="status-error">'+ msg +'</div>';
                }
                // Hide any previous response text
                $(".status-error,.status-success").remove();
                // Show response message
                $commentform.prepend(response);
            }
        });
        return false;
    });

     /* ---------------------------------------------------------------------- */
    /*	Contact Form
    /* ---------------------------------------------------------------------- */

    // Needed variables
    var $contactform 	= $('#contact'),
        $success		= 'Uw bericht is succesvol verzonden!';
    $contactform.submit(function(){
        $.ajax({
            type: "POST",
            url: $contactform.attr("action"),
            data: $(this).serialize(),
            success: function(msg)
            {
                if(msg == 'SEND'){
                    response = '<div class="status-success">'+ $success +'</div>';
                }
                else{
                    response = '<div class="status-error">'+ msg +'</div>';
                }
                // Hide any previous response text
                $(".status-error,.status-success").remove();
                // Show response message
                $contactform.prepend(response);
            }
        });
        return false;
    });


        /* End */
});
