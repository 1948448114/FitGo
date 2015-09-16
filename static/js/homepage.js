$(function(){
    $('.carousel').carousel({
    interval: 2000000
    })
    $('#moredown').mouseover(function(event) {
            $('.absoluteul').show();
        });
    var flag=false;
    $('#moredown').mouseout(function(event) {

    	setTimeout(hide,2000);
    });
    $('.absoluteul').mouseover(function(event) {
    	flag=true;
    	$('#morecolor').removeClass('bar');
    	$('#morecolor').addClass('more-color');
    });
    $('.absoluteul').mouseout(function(event) {
    	$('.absoluteul').hide();
    	flag=false;
    	$('#morecolor').removeClass('more-color');
    	$('#morecolor').addClass('bar');
    });
    $('#move-to-contact').click(function(event) {
    	$('html,body').animate({scrollTop:$('#startfooter').offset().top}, 800);
    });
    function hide(){
    	if(!flag){
    		$('.absoluteul').hide();
    	}
    }

    });

function toTop(){
    $("body").animate({scrollTop:0}, 500);
}
