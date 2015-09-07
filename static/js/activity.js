$(document).ready(function() {
   
    function init() {
        $('#hide-new').click(function(event) {
            $("#after-show").toggle('slow/4000/fast');
        });

        $("#menu .home").removeClass("home");
        $($("#menu .bar").get(4)).addClass("home");
        $('#Start-Time').datepicker('hide');
        $('#Start-Time').datepicker({
            format: 'mm-dd-yyyy'
        });

        $('#End-Time').datepicker('hide');
        $('#End-Time').datepicker({
            format: 'mm-dd-yyyy'
        });
        $('#Start-Time-Search').datepicker('hide');
        $('#Start-Time-Search').datepicker({
            format: 'mm-dd-yyyy'
        });
        $('#below').click(function(event) {
            $('#after-show').hide('slow/400/fast');
        });
        $("#toSearch").click(function(event) {
        	$('#toSearch').hide();
        	$('#searchText').show('slow/400/fast');
        });
        // $('#below').click(function(event) {
        //    $('#searchText').hide(); 
        //    $('#toSearch').show();
        // });
        $("div:not(.specialFliter)")
    };

    init();
});


// function submitAct() {
//     alert($("#options").val());
//     jQuery.ajax({
//       url: '/activity/create',
//       type: 'POST',
//       dataType: 'json',
//       data: {
//         'uid': {{user.uid}},
//         'activity_title':$("#newActivity").val(),
//         'start_time':$("#Start-Time").val(),
//         'end_time':$("#End-Time").val(),
//         'location':$("#options").val(),
//         'details':$("#activity_detail").val()
//   },
//       complete: function(xhr, textStatus) {
//       },
//       success: function(data, textStatus, xhr) {
//         alert(data)
//       },
//       error: function(xhr, textStatus, errorThrown) {
//       }
//     });
    
//     $("#after-show").hide('slow/400/fast');
// };

// function toNew() {
//     $('#after-show').show();
//     $("body").animate({
//         scrollTop: 0
//     }, 500);
// };


// var flag=1;
// $('#hide-new').click(function(event) {
// if(flag%2==1){
// $('#after-show').show('slow/400/fast');
// flag++;
// }
// else{
// $('#after-show').hide('slow/400/fast');
// flag++;
// }
// });


// $('#hide-new').click(function(event) {
// 	'#hide'
// 	if($flag!=1){
// 		$('#after-show').hide('slow/400/fast');
// 		$('#hide-new').removeClass('showthis');
// 	}
// 	else{
// 		$('#after-show').show('slow/400/fast');
// 		$('#hide-new').addClass('showthis');
// 	}
// });



// });