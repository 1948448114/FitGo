var times=0;
//加载的js
$(document).ready(function() {
    init();


    
    



    getAllState();
    
});

//初始化函数
function init(){

}

function getAllState(){
    jQuery.ajax({
      url: '/discover/discover_page',
      type: 'POST',
      data: {
        'times': times},
      success: function(data, textStatus, xhr) {
        console.log("two");
        $("#discover_state_all").html(data);

        other();
        friendtState();
        AllStatezhan();
        times=times+1;

      },
      error: function(xhr, textStatus, errorThrown) {
        //called when there is an error
      }
    });
};

function AllStatezhan() {
    var opened = false;
    $('#discover_state_all > div.uc-container').each(function(i) {
        var $item = $(this),
            direction;
        switch (i % 12) {
            case 0:
                direction = ['right', 'bottom'];
                break;
            case 1:
                direction = ['right', 'bottom'];
                break;
            case 2:
                direction = ['left', 'bottom'];
                break;
            case 3:
                direction = ['left', 'bottom'];
                break;
            case 4:
                direction = ['top', 'right'];
                break;
            case 5:
                direction = ['bottom', 'right'];
                break;
            case 6:
                direction = ['top', 'left'];
                break;
            case 7:
                direction = ['bottom', 'left'];
                break;
            case 8:
                direction = ['right', 'top'];
                break;
            case 9:
                direction = ['right', 'top'];
                break;
            case 10:
                direction = ['left', 'top'];
                break;
            case 11:
                direction = ['left', 'top'];
                break;
        }
        var pfold = $item.pfold({
            folddirection: direction,
            speed: 200,
            onEndFolding: function() {
                opened = false;
            },
            centered: true
        });
        $item.find('span.icon-eye').on('click', function() {
            if (!opened) {
                opened = true;
                pfold.unfold();
            }
        }).end().find('span.icon-cancel').on('click', function() {
            pfold.fold();
        });
    });
};

function friendtState() {
    // say we want to have only one item opened at one moment
    var opened = false;
    $('#discover_state_friend > div.uc-container').each(function(i) {
        var $item1 = $(this),
            direction;
        switch (i % 8) {
            case 0:
                direction = ['right', 'bottom'];
                break;
            case 1:
                direction = ['right', 'bottom'];
                break;
            case 2:
                direction = ['left', 'bottom'];
                break;
            case 3:
                direction = ['left', 'bottom'];
                break;
            case 4:
                direction = ['right', 'top'];
                break;
            case 5:
                direction = ['right', 'top'];
                break;
            case 6:
                direction = ['left', 'top'];
                break;
            case 7:
                direction = ['left', 'top'];
                break;
        }
        var pfold = $item1.pfold({
            folddirection: direction,
            speed: 300,
            onEndFolding: function() {
                opened = false;
            },
            // centered : true
        });
        $item1.find('span.icon-eye').on('click', function() {
            if (!opened) {
                opened = true;
                pfold.unfold();
            }
        }).end().find('span.icon-cancel').on('click', function() {
            pfold.fold();
        });
    });
};
function other() {
    // say we want to have only one item opened at one moment
    var opened = false;
    $('#discover_state_list > div.uc-container').each(function(i) {
        var $item1 = $(this),
            direction;
        switch (i % 4) {
            case 0:
                direction = ['right', 'bottom'];
                break;
            case 1:
                direction = ['right', 'bottom'];
                break;
            case 2:
                direction = ['left', 'bottom'];
                break;
            case 3:
                direction = ['left', 'bottom'];
                break;
        }
        var pfold = $item1.pfold({
            folddirection: direction,
            speed: 600,
            onEndFolding: function() {
                opened = false;
            },
            // centered : true
        });
        $item1.find('span.icon-eye').on('click', function() {
            if (!opened) {
                opened = true;
                pfold.unfold();
            }
        }).end().find('span.icon-cancel').on('click', function() {
            pfold.fold();
        });
    });
};
$(function() {

    var a = new sHover("friend_item", "friend_cover");
    a.set({
        slideSpeed: 5,
        opacityChange: true,
        opacity: 80
    });
});
$(function() {
    $(".icon-camera").click(function(event) {
        /* Act on the event */
        $("#warp").show('slow/400/fast');
        $("#discover_png").hide('slow/400/fast');
        $(".container_friend").hide();
        $("#friend_state").hide();
        $("#search_state_list").hide();
        $(".find_friend").hide();
    });


    $("#share_btn").click(function(event) {
        /* Act on the event */
        $(".create_state").show('slow/400/fast');
        $(".find_friend").hide('slow/400/fast');
        $(".container_friend").hide();
        $("#friend_state").hide();
        $("#search_state_list").hide();
    });


    $("#find_friend_btn").click(function(event) {
        /* Act on the event */
        $(".create_state").hide();
        $(".find_friend").hide();
        $(".container_friend").show();
        $("#search_state_list").hide();
        $("#friend_state").hide();
    });


    $("#submit_state_btn").click(function(event) {
        /* Act on the event */
        $(".create_state").hide();
        $(".find_friend").hide();
        $("#friend_state").show();
        $(".container_friend").hide();
        $("#search_state_list").hide();
        window.location.reload();
    });


    $("#find_btn").click(function(event) {
        /* Act on the event */
        $(".find_friend").show('slow/400/fast');
        $(".create_state").hide('slow/400/fast');
        $("#friend_state").hide();
        $("#search_state_list").hide();
        $(".create_state").hide();
    });


    $("#search_state_btn").click(function(event) {
        /* Act on the event */
        $("#search_state_list").show();
        $(".create_state").hide();
        $(".container_friend").hide();
        $(".find_friend").hide();
        $("#friend_state").hide();
    });



    $(".icon-spinner").click(function(event) {
        /* Act on the event */
        console.log('here');
        getAllState();
        // window.location.reload();
    });
});
$(function() {
    $("#menu .home").removeClass("home");
    $($("#menu .bar").get(1)).addClass("home");
});


