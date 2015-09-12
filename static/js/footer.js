$(document).ready(function() {
                if($("meta[name=toTop]").attr("content")=="true"){
                $("<div id='toTop'><img src='/static/images/top1.png'></div>").appendTo('body');
                $("#toTop").css({
                    width: '50px',
                    height: '50px',
                    bottom:'10px',
                    right:'15px',
                    position:'fixed',
                    cursor:'pointer',
                    zIndex:'999999',
                });
                if($(this).scrollTop()==0){
                        $("#toTop").hide();
                    }
                $(window).scroll(function(event) {
                    if($(this).scrollTop()==0){
                        $("#toTop").hide();
                    }
                    if($(this).scrollTop()!=0){
                        $("#toTop").show();
                    }
                }); 
                    $("#toTop").click(function(event) {
                                $("html,body").animate({
                                    scrollTop:"0px"},
                                    666)
                            });
                }
    var uid="";
    $(".dropdown_close").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide('slow/400/fast');
        $("#signup_dropdown").hide('slow/400/fast');
        $("#login_div").hide('slow/400/fast');
        $("#find_password_dropdown").hide('slow/400/fast');
        $("#find_password_new_pwd").hide('slow/400/fast');
    });
    $(".forgot-password").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide('slow/400/fast');
        $("#signup_dropdown").hide('slow/400/fast');
        $("#login_div").hide('slow/400/fast');
        $("#find_password_dropdown").show('slow/400/fast');
    });
    $("#check_btn").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide('slow/400/fast');
        $("#signup_dropdown").hide('slow/400/fast');
        $("#login_div").hide('slow/400/fast');
        $("#find_password_new_pwd").show('slow/400/fast');
    });
    $("#login").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide('slow/400/fast');
        $("#signup_dropdown").hide('slow/400/fast');
        $("#login_div").show('slow/400/fast');
        $("#find_password_dropdown").hide('slow/400/fast');
        $("#find_password_new_pwd").hide('slow/400/fast');
        $("#login_message").hide('slow/400/fast');
        $("#sign_up_message").hide('slow/400/fast');
        $("#change_password_message").hide('slow/400/fast');
        $("#find_message").hide('slow/400/fast');
        $("#verify_message").hide('slow/400/fast');
    });
    $("#sign_up_btn").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide('slow/400/fast');
        $("#signup_dropdown").show('slow/400/fast');
        $("#login_div").hide('slow/400/fast');
        $("#find_password_dropdown").hide('slow/400/fast');
    });
// 验证
    $("#verify").click(function(event) {
        /* Act on the event */
        jQuery.ajax({
          url: '/auth/register/verify',
          type: 'POST',
          dataType: 'json',
          data: {
            'info_email': $("#info_email_signup").val(),
            'student_card':$("#student_card_signup").val(),
            'student_id':$("#student_id_signup").val()   
        },
          success: function(data, textStatus, xhr) {
            if(data['code'] == 200){
                $("#login_div").hide();
                $("#verify_dropdown").show();
                $("#signup_dropdown").hide();
                $("#find_password_dropdown").hide();
                uid=data['content']['uid'];
            }
            else{
                $("#verify_message").html(data['content']);
                $("#verify_message").show();
            }
          },
          error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
            $("#verify_message").html("Network error!");
          }
        });
        
        
    });

//注册
$("#signup_btn").click(function(event) {
    if($("#password_signup").val().length<6){
        $("#sign_up_message").html("password is too short");
        $("#sign_up_message").show();
    }
    else if($("#password_signup").val()!=$("#password_confirm").val()){
        $("#sign_up_message").html("Confirm password is not the same as password");
        $("#sign_up_message").show();
    }
    else{
    jQuery.ajax({
      url: '/auth/register',
      type: 'POST',
      dataType: 'json',
      data: {
        'uid': uid,
        'name':$("#name_signup").val(),
        'password':$("#password_signup").val()
        },
      success: function(data, textStatus, xhr) {
        //called when successful
        if (data['code'] == 200) {
            location.href = "/";
        } else {
             $("#sign_up_message").html(data['content']);
             $("#sign_up_message").show();
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        $("#sign_up_message").html("Network error!");
      }
    });
}
    
});

// 登录
    $("#login_btn").click(function() {
        if ($("#password_login").val().length < 6) {
            $("#login_message").html("password is too short");
            $("#login_message").show();
        } else {
            var is_remember = 0;
            if ($("#login_check").is(':checked')) {
                is_remember = 1;
            }
            jQuery.ajax({
                url: '/auth/login',
                type: 'POST',
                dataType: "json",
                data: {
                    'info_email': $("#info_email_login").val(),
                    'user_password': $("#password_login").val(),
                    'code': $("#code_login").val(),
                    'is_remember': is_remember
                },
                success: function(data, textStatus, xhr) {
                    if (data['code'] == 200) {
                        location.href = "/";
                    } else {
                        $("#login_message").html(data['content']);
                        $("#login_message").show();
                    }
                },
                error: function(xhr, textStatus, errorThrown) {
                    $("#login_message").html("Network error!");
                }
            });
        }
    });
// 登出
    $("#logout").click(function(event) {
        /* Act on the event */
        jQuery.ajax({
          url: '/auth/logout',
          method: 'DELETE',
          complete: function(xhr, textStatus) {
            //called when complete
          },
          success: function(data, textStatus, xhr) {
            var date = new Date(); 
            date.setTime(date.getTime() - 10000); 
            document.cookie = "username=null; expires=" + date.toGMTString();
            location.href="/";
            //called when successful
          },
          error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
          }
        });
        
    });
});