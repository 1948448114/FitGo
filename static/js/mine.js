    $(function(){
        $('.banner').unslider({arrows: true,
            delay:1000000,
            keys: true,
            fluid: true,
            dots: true
        });
        $('.unslider-arrow').click(function() {
        var fn = this.className.split(' ')[1];

        //  Either do unslider.data('unslider').next() or .prev() depending on the className
        unslider.data('unslider')[fn]();
        });
    });
