$(document).ready(function(){
    var plan={
            'content':{
                'target':'',
                'signature':'',
                'start_time':'',
                'end_time':'',
            }
        };
    plan['content']['1'] = '2';
    console.log(JSON.stringify(plan));
	function init(){
		$('#to-make').click(function(event) {
			$("html,body").animate({scrollTop:$("#newPlan").offset().top},500);
		});
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
        $('#reservation').daterangepicker(null, function(start, end, label) {
                    console.log(start.toISOString(), end.toISOString(), label);
                  });
         $('#reservationtime1').daterangepicker({
                    timePicker: true,
                    timePickerIncrement: 30,
                    format: 'MM/DD/YYYY h:mm A'
                  }, function(start, end, label) {
                    console.log(start.toISOString(), end.toISOString(), label);
                  });
        $('.restButton').each(function(index, el) {
        	$(this).bind('click',function(){
	        	var activeTab = $(event.target).val();
				console.log(activeTab);
				var nextTab=(parseInt(activeTab)+parseInt('1')).toString();
				console.log(nextTab);
				var radio_value=$('.radio'+activeTab+' input[name="ifrest"]:checked').val();
				console.log(radio_value);
				if(radio_value=="disagree"){
					$('.yesShow').show();
				}
				else if(radio_value==null){
				alert("Please Choose one!")
				}
				else{
					$('.yesShow').hide();
					$('#myTab a[href="#'+nextTab+'"]').tab('show');
	        		}
	        	});
        });

        $("#firstTab").click(function(event) {
        	event.preventDefault();
  			$(this).tab('show');
        });

        // $('#btnPaopao').click(function(event) {
        // 	$('#btnPaopao').popover('show');
        // });
}
		init();
        newPlan();
});
function newPlan(){
    $("#btnPaopao").click(function(event) {
        jQuery.ajax({
          url: '/plans',
          type: 'POST',
          dataType: 'json',
          data: {'plan': JSON.stringify(plan)},
          success: function(data, textStatus, xhr) {
            //called when successful
            if(data['code'] == 200){
                $("#btnPaopao").popover('show');
            }
            else{
                $("#btnPaopao").attr('data-content',data['content']);
                $("#btnPaopao").popover('show');
            }
          },
          error: function(xhr, textStatus, errorThrown) {
                $("#btnPaopao").attr('data-content','Network Error!');
                $("#btnPaopao").popover('show');
          }
        });
        
    });
}



                //  '1':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '2':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '3':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '4':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '5':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '6':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '7':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // }

























