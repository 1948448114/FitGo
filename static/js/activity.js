$(function() {
$("#menu .home").removeClass("home");
$($("#menu .bar").get(4)).addClass("home");
});

$(function(){
$('#Start-Time').datepicker('hide');
$('#Start-Time').datepicker({format: 'mm-dd-yyyy'});
$('#End-Time').datepicker('hide');
$('#End-Time').datepicker({format: 'mm-dd-yyyy'});
});
function submitAct(){
$("#after-show").hide('slow/400/fast');
}
function toNew(){
$('#after-show').show();
$("body").animate({scrollTop:0}, 500);
}

// var flag=1;
$(function(){
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
$('#hide-new').click(function(event) {
	$("#after-show").toggle('slow/400000000/fast');
});
});

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

$(function(){
$('#below').click(function(event) {
$('#after-show').hide('slow/400/fast');
});
});

// });