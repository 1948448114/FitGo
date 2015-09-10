$(document).ready(function(){
	function init(){
		$("#menu .home").removeClass("home");
        $($("#menu .bar").get(2)).addClass("home");
        $('#reservationtime').daterangepicker({
                    timePicker: true,
                    timePickerIncrement: 30,
                    format: 'MM/DD/YYYY h:mm A'
                  }, function(start, end, label) {
                    console.log(start.toISOString(), end.toISOString(), label);
                  });
}
		init();
});
function restConfirm(){
	var radio_value=$('#orest input[name="ifrest"]:checked').val();
	if(radio_value=="disagree"){
		$('#yesShow').show();
	}
	else if(radio_value==null){
		alert("Please Choose one!")
	}
	else{
		$('#yesShow').hide();
		$('#myTab li:eq(2) a').tab('show')};
}




























