$(document).ready(function(){
    var plan={
            'content':{
                'target':'',
                'signature':'',
                'start_time':'',
                'end_time':'',
            }
        };
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
<<<<<<< HEAD
        $('#reservation').daterangepicker(null, function(start, end, label) {
                    console.log(start.toISOString(), end.toISOString(), label);
                  });
         $('#reservationtime1').daterangepicker({
=======
        $(".yesShow1").hide();
        $(".yesShow2").hide();
        $(".yesShow3").hide();
        $(".yesShow4").hide();
        $(".yesShow5").hide();
        $(".yesShow6").hide();
        $(".yesShow7").hide();
        $('.reservationtime').daterangepicker({
>>>>>>> origin/Front-end
                    timePicker: true,
                    timePickerIncrement: 30,
                    format: 'MM/DD/YYYY h:mm A'
                  }, function(start, end, label) {
                    console.log(start.toISOString(), end.toISOString(), label);
                  });



        $('.restButton').each(function(index, el) {
        	$(this).bind('click',function(){
	        	var activeTab = $(event.target).val();
				var nextTab=(parseInt(activeTab)+parseInt('1')).toString();
				var radio_value=$('.radio'+activeTab+' input[name="ifrest'+activeTab+'"]:checked').val();
				if(radio_value=="disagree"){
                    $('.yesShow'+activeTab).show();
				}
				else if(radio_value==null){
				alert("Please Choose one!")
				}
				else{
					$('.yesShow'+activeTab).hide();
					$('#myTab a[href="#'+nextTab+'"]').tab('show');
	        		}
	        	});
        });
        // $('#btnPaopao').click(function(event) {
        // 	$('#btnPaopao').popover('show');
        // });
<<<<<<< HEAD
}
		init();
        newPlan();
});
=======
};


>>>>>>> origin/Front-end
function newPlan(){
    $("#btnPaopao").click(function(event) {
            $(".pages .tab-pane").each(function(index, el) {
                var index1=index;
                value = $(this).find('input[name="ifrest' + index1+ '"]:checked').val();
                if (value == 'disagree') {
                    plan['content'][index1] = {
                        'selectValue': [],
                        'inputValue': []
                    }
                    $(this).find("select").each(function(index, el) {
                        plan['content'][index1]['selectValue'].push($(this).val());
                    });
                    $(this).find("input.userInput1").each(function(index, el) {
                        plan['content'][index1]['inputValue'].push($(this).val());
                    });
                    // $("#" + index + " select").each(function(index, el) {
                    //     plan['content'][activeTab]['selectValue'].push($(this).val());
                    // });
                    // $("#" + index + " input.userInput1").each(function(index, el) {
                    //     plan['content'][activeTab]['inputValue'].push($(this).val());
                    // });
                }

            });
        plan['content']['target'] = $("#Target").val();
        plan['content']['signature'] = $("#signature").val();
        plan['content']['start_time'] = $("#reservationtime").val();
        plan['content']['end_time'] = '';
        console.log(JSON.stringify(plan));
        // jQuery.ajax({
        //   url: '/plans',
        //   type: 'POST',
        //   dataType: 'json',
        //   data: {'plan': JSON.stringify(plan)},
        //   success: function(data, textStatus, xhr) {
        //     //called when successful
        //     if(data['code'] == 200){
        //         $("#btnPaopao").popover('show');
        //     }
        //     else{
        //         $("#btnPaopao").attr('data-content',data['content']);
        //         $("#btnPaopao").popover('show');
        //     }
        //   },
        //   error: function(xhr, textStatus, errorThrown) {
        //         $("#btnPaopao").attr('data-content','Network Error!');
        //         $("#btnPaopao").popover('show');
        //   }
        // });
        
    });
}


		init();
        newPlan();
});























