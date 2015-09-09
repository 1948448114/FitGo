function refresh(){
    jQuery.ajax({
      url: '/activity',
      type: 'POST',
      dataType: 'json',
      data: {'length': 'value1'},
      success: function(data, textStatus, xhr) {
        if(data['code']=200){
            data_length = data['content'].length;
            divContent = $("#cd-timeline");
            for(var item=0;item<data_length;item++){
                var content=""
                divContent.append("")
            }
        }
        else{
            $("#error_message_content").val(data['content']);
            $("#error_message").show("slow");
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        $("#error_message_content").val("Network Error!")
        $("#error_message").show("slow");
      }
    });
    
}

$(document).ready(function() {
    function init() {
        $('#hide-new').click(function(event) {
            $("#after-show").toggle('slow/4000/fast');
        });

        $("#menu .home").removeClass("home");
        $($("#menu .bar").get(4)).addClass("home");
        $('#Start-Time').datepicker('hide');
        $('#Start-Time').datepicker({
            format: 'yyyy-mm-dd'
        });

        $('#End-Time').datepicker('hide');
        $('#End-Time').datepicker({
            format: 'yyyy-mm-dd'
        });
        $('#Start-Time-Search').datepicker('hide');
        $('#Start-Time-Search').datepicker({
            format: 'yyyy-mm-dd'
        });
        $('#below').click(function(event) {
            $('#after-show').hide('slow/400/fast');
        });
        $("#toSearch").click(function(event) {
            $('#toSearch').hide();
            $('#searchText').show('slow/400/fast');
            $('.confirmSearch').show('slow/400/fast');
        });

        $("#alertPaopao").click(function(event) {
            if (!$("#uid").attr('value')) {
                $('#alertPaopao').attr("data-content", "Login First!");
                $('#alertPaopao').popover('show');
                // $('#alertPaopao').popover(options);
            } else if ($("#newActivity").val().length < 1 || $("#Start-Time").val().length < 1 || $("#End-Time").val().length < 1 || $("#options").val().length < 1 || $("#activity_detail").val().length < 1) {
                $('#alertPaopao').attr("data-content", "Invalid input");
                $('#alertPaopao').popover('show');
            } else {

                $.ajax({
                    url: '/activity/create',
                    type: 'POST',
                    dataType: 'json',
                    data: {
                        'uid': $("#uid").attr('value'),
                        'act_title': $("#newActivity").val(),
                        'start_time': $("#Start-Time").val(),
                        'end_time': $("#End-Time").val(),
                        'location': $("#options").val(),
                        'details': $("#activity_detail").val()
                    },
                    success: function(data, textStatus, xhr) {
                        if (data['code'] == 200) {
                            $('#alertPaopao').attr("data-content", "Success!");
                            $('#alertPaopao').popover('show');
                            setTimeout(function(){$("#after-show").hide('slow/400/fast');},1000);
                        } else {
                            $('#alertPaopao').attr("data-content", data['content']);
                            $('#alertPaopao').popover('show');
                        }
                    },
                    error: function(xhr, textStatus, errorThrown) {
                        $('#alertPaopao').attr("data-content", "Network Error!");
                        $('#alertPaopao').popover('show');
                    }
                });
            }

        });
            $('#specialFliter').mouseout(function(event) {
                $('body').bind('click', function(event) {
                    $('#searchText').hide();
                    $('.confirmSearch').hide();
                    $('#toSearch').show();
                    // $('#after-show').hide();
                });
            });
            $('#specialFliter').mouseover(function(event) {
                $('body').unbind('click');
            });
            // $('#wholeNew').mouseout(function(event)){
            //     $('body').bind('click',function(event)){
            //         $('#after-show').show();
            //     }
            // }
            // $('#wholeNew').mouseover(function(event)){
            //     $('body').unbind('click');
            // }
            // $('#after-show').mouseover(function(event)){
            //     $('body').unbind('click');
            // }
        


        // $('#alertPaopao').attr("data-content", "Login First!");
       
    };
    init();
});
