$(function(){



    function getHot(){
    jQuery.ajax({
      url: '/hot',
      type: 'GET',
      dataType: 'json',
      success: function(data, textStatus, xhr) {
        if(data['code']==200){
          console.log(data['content']['topics'][0]['topic_title'])
          $("#state_one h4").html(data['content']['topics'][0]['topic_title']);
          $("#state_one .content").html(data['content']['topics'][0]['topic_content']);
          $("#state_one .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['topics'][0]['topic_time']);

          $("#state_two h4").html(data['content']['topics'][1]['topic_title']);
          $("#state_two .content").html(data['content']['topics'][1]['topic_content']);
          $("#state_two .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['topics'][1]['topic_time']);

          $("#state_three h4").html(data['content']['topics'][2]['topic_title']);
          $("#state_three .content").html(data['content']['topics'][2]['topic_content']);
          $("#state_three .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['topics'][2]['topic_time']);

          $("#activity_one h4").html(data['content']['act'][0]['title']);
          $("#activity_one .content").html(data['content']['act'][0]['detail']);
          $("#activity_one .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['act'][0]['start']+'&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['act'][0]['act_location']);

          $("#invite_one h4").html(data['content']['invite'][0]['fit_item']);
          $("#invite_one .content").html(data['content']['invite'][0]['remark']);
          $("#invite_one .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['invite'][0]['start_time']+'&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['invite'][0]['location']);

          $("#invite_two h4").html(data['content']['invite'][1]['fit_item']);
          $("#invite_two .content").html(data['content']['invite'][1]['remark']);
          $("#invite_two .time").html('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['invite'][1]['start_time']+'&nbsp;&nbsp;&nbsp;&nbsp;'+data['content']['invite'][1]['location']);

        }
      },
      error: function(xhr, textStatus, errorThrown) {
        //called when there is an error
      }
    });
    
};


getHot();


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
