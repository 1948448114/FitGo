$(document).ready(function(){


    var user_uid = $("#forothers_uid").val();
    function init(){
        $('#to-plans').click(function(event) {
            $("html,body").animate({scrollTop:$("#myplans").offset().top},800);
        });
        $('#to-states').click(function(event) {
            $("html,body").animate({scrollTop:$("#mystates").offset().top},800);
        });
        $(".tabFocus a").click(function(event) {
            $('.a-active').removeClass('a-active');
            $(event.target).addClass('a-active');
        });
        $("#menu .home").removeClass("home");
        $($("#menu .bar").get(2)).addClass("home");
}

    getPlan(user_uid);
    getInfo(user_uid)
});


function getPlan(user_uid){
    jQuery.ajax({
      url: '/plans/detail',
      type: 'GET',
      data:{
        'uid':user_uid
      },
      success: function(data, textStatus, xhr) {
        console.log(data);
        $("#myTab_plan_show").html(data);
      },
      error: function(xhr, textStatus, errorThrown) {
        
      }
    });
    
};






    























