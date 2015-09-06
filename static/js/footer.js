$(document).ready(function() {
    var uid="";
    $(".dropdown_close").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").hide();
        $("#find_password_dropdown").hide();
        $("#find_password_new_pwd").hide();
    });
    $(".forgot-password").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").hide();
        $("#find_password_dropdown").show();
    });
    $("#check_btn").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").hide();
        $("#find_password_new_pwd").show();
    });
    $("#login").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").show();
        $("#find_password_dropdown").hide();
        $("#find_password_new_pwd").hide();
        $("#login_message").hide();
        $("#sign_up_message").hide();
        $("#change_password_message").hide();
        $("#find_message").hide();
        $("#verify_message").hide();
    });
    $("#sign_up_btn").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").show();
        $("#login_div").hide();
        $("#find_password_dropdown").hide();
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
            location.href="/";
            //called when successful
          },
          error: function(xhr, textStatus, errorThrown) {
            //called when there is an error
          }
        });
        
    });
});