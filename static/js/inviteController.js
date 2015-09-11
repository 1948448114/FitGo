$(document).ready(function() {
    // init();
    NewInvitation();
    $("#create_invite_information_message").hide();
    $(".wrong_message").hide();
    $("#search_btn").click(function(event) {
        search();
    });
});

function NewInvitation(){
    $("#NewButton").click(function(event) {
        var fit_location = $("#create_fit_location").val();
        if(fit_location=='Location'){fit_location='';}

        var fit_item = $("#create_fit_item").val();
        if(fit_item=='Fit Item'){fit_item='';}

        var gender = $("#create_gender").val();
        if(gender=='Gender'){gender='';}

        var duration = $("#create_duration").val();
        if(duration=='Duration'){duration='';}
        var start_time=$("#create_invite_start_time").val();
        var tag = $("#create_invite_tag").val();
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
            if(data['code']==200){
                $("#create_invite_information_message").attr('class','alert alert-success showing');
                $("#create_invite_information_message").html('Success');
                $("#create_invite_information_message").show();
                setTimeout(function() {
                    $("#create_invite_information_message").hide();
                    },1000);
            }else{
                $("#create_invite_information_message").html(data['content']);
                $("#create_invite_information_message").show();
            }
          },
          error: function(xhr, textStatus, errorThrown) {
            $("#create_invite_information_message").html('Network Error!');
            $("#create_invite_information_message").show();
          }
        });
        
    });
}


function search(){
    var tag=$("#search_invite_tag").val();
    var fit_location = $("#fit_location").val()
    if(fit_location=='Location'){fit_location='';}
    var fit_item=$("#fit_item").val();
    if(fit_item=='Fit Item'){fit_item='';}
    var gender = $("#gender").val();
    if(gender=="Gender"){gender='';}
    var start_time = $("#search_invite_start_time").val();
    jQuery.ajax({
      url: '/invite/search',
      type: 'POST',
      dataType: 'json',
      data: {
           'start_time':start_time,
           'fit_location':fit_location,
           'fit_item':fit_item,
           'user_tag':tag,
           'gender':gender
      },
      success: function(data, textStatus, xhr) {
        
      },
      error: function(xhr, textStatus, errorThrown) {
      }
    });
    
}