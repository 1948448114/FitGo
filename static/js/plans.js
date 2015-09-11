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
        $('#btnPaopao').click(function(event) {
        	$('#btnPaopao').popover('show');
        });
        $("#firstTab").click(function(event) {
        	event.preventDefault();
  			$(this).tab('show');
        });
}
		init();
});






























