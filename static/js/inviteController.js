$(document).ready(function() {
    // init();
    NewInvitation();
});

function NewInvitation(){
    $("#NewButton").click(function(event) {
        var fit_location = $("#create_fit_location").val();
        console.log(fit_location);
        var fit_item = $("#create_fit_item").val();
        console.log(fit_item);
        var gender = $("#create_gender").val();
        console.log(gender);
        var duration = $("#create_duration").val();
        var start_time=$("#create_invite_start_time").val();
        console.log(start_time);
        console.log(duration);
        var tag = $("#create_invite_tag").val();
        console.log(tag);
        var moreInfo = $("#create_invite_more").val();
        console.log(moreInfo);
        jQuery.ajax({
          url: '/invite',
          type: 'POST',
          dataType: 'json',
          data: {
                'start_time':start_time,
                'duration':duration,
                'fit_location':fit_location,
                'fit_item':fit_item,
                'user_tag':tag,
                'gender':gender,
                'remark':moreInfo
          },
          success: function(data, textStatus, xhr) {
            alert(data['code']);
          },
          error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
          }
        });
        
    });
}