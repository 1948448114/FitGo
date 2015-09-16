$(function(){
    $('.carousel').carousel({
    interval: 2000
    })
    $('#moredown').mouseover(function(event) {
            $('.absoluteul').show();
        });
    var flag=false;
    $('#moredown').mouseout(function(event) {

    	setTimeout(hide,4000);
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
    	$('html,body').animate({scrollTop:$('#startfooter').offset().top}, 1000);
    });
    $('#show-introduce').click(function(event) {
        $('.ag-content-customer-wrap').show();
        $('html,body').animate({scrollTop:$('.ag-content-customer-wrap').offset().top}, 500);
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
