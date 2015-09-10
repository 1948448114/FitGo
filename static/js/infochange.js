$(document).ready(function(){
	function init(){
		$('#changeKey').click(function(event) {
			$('#changePassword').toggle();
		});
		$('.planbtn').click(function(event) {
			$('#changePassword').hide('slow/400/fast');
		});
		$("#menu .home").removeClass("home");
        $($("#menu .bar").get(2)).addClass("home");
}
		init();
});
function moreTags(event){
	if(event.keyCode==13){
		var value=$('.inputTag').val();
		$('.inputTag').before('<span class="tag">'+value+'<span onclick="closeTag(event)" class="icon-remove" style="font-size:10px;color:#343a63"></span></span>');
		$('.inputTag').val("");
	}
}
function closeTag(event){
	// console.log(event.target);
    $(event.target).parent().remove();
}
