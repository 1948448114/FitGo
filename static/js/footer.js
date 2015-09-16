$(document).ready(function() {
    var uid="";
    if($("#user_state").val()=='0'){
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").fadeIn();
        $("#find_password_dropdown").hide();
        $("#find_password_new_pwd").hide();
        $("#login_message").hide();
        $("#sign_up_message").hide();
        $("#change_password_message").hide();
        $("#find_message").hide();
        $("#verify_message").hide();
    };
    if ($("meta[name=toTop]").attr("content") == "true") {
        $("<div id='toTop'><img id='toTopbtn' src='/static/images/top1.png'></div>").appendTo('body');
        $("#toTop").css({
            width: '50px',
            height: '50px',
            bottom: '10px',
            right: '10px',
            position: 'fixed',
            cursor: 'pointer',
            zIndex: '999999',
        });
        if ($(this).scrollTop() == 0) {
            $("#toTop").hide();
        }
        $(window).scroll(function(event) {
            if ($(this).scrollTop() == 0) {
                $("#toTop").hide();
            }
            if ($(this).scrollTop() != 0) {
                $("#toTop").show();
            }
        });
        $("#toTop").click(function(event) {
            $("html,body").animate({
                    scrollTop: "0px"
                },
                666)
        });
    }
    
    $("#code_img").attr("src",'/auth/code/'+Math.random());
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
        $("#find_password_dropdown").fadeIn();
    });
    $("#check_btn").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").hide();
        $("#find_password_new_pwd").fadeIn();
    });
    // $("#code_img").click(function(event) {
    //     /* change code */
    //     time=new time()
    //     codes = time.getTime()+Math.random()
    //     document.getElementById('code_img').src="/auth/code/"+codes;
    // )};
    $("#login").click(function(event) {
        /* Act on the event */
        $("#verify_dropdown").hide();
        $("#signup_dropdown").hide();
        $("#login_div").fadeIn();
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
        $("#signup_dropdown").fadeIn();
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
                'student_card': $("#student_card_signup").val(),
                'student_id': $("#student_id_signup").val()
            },
            success: function(data, textStatus, xhr) {
                if (data['code'] == 200) {
                    $("#login_div").hide();
                    $("#verify_dropdown").fadeIn();
                    $("#signup_dropdown").hide();
                    $("#find_password_dropdown").hide();
                    uid = data['content']['uid'];
                } else {
                    $("#verify_message").html(data['content']);
                    $("#verify_message").fadeIn();
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
        if ($("#password_signup").val().length < 6) {
            $("#sign_up_message").html("password is too short");
            $("#sign_up_message").fadeIn();
        } else if ($("#password_signup").val() != $("#password_confirm").val()) {
            $("#sign_up_message").html("Confirm password is not the same as password");
            $("#sign_up_message").fadeIn();
        } else {
            jQuery.ajax({
                url: '/auth/register',
                type: 'POST',
                dataType: 'json',
                data: {
                    'uid': uid,
                    'name': $("#name_signup").val(),
                    'password': $("#password_signup").val()
                },
                success: function(data, textStatus, xhr) {
                    //called when successful
                    if (data['code'] == 200) {
                        location.href = "/";
                    } else {
                        $("#sign_up_message").html(data['content']);
                        $("#sign_up_message").fadeIn();
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
            $("#login_message").fadeIn();
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
                    'code_random':$("#code_img").attr("src"),
                    'is_remember': is_remember
                },
                success: function(data, textStatus, xhr) {
                    if (data['code'] == 200) {
                        location.href = "/";
                    } else {
                        $("#login_message").html(data['content']);
                        $("#login_message").fadeIn();
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
                location.href = "/";
                //called when successful
            },
            error: function(xhr, textStatus, errorThrown) {
                //called when there is an error
            }
        });

    });

    //找回密码
    $("#find_password_btn").click(function(event) {
        var newPassword = $("#password_find_password").val();
        var passwordConfirm = $("#password_confirm_find_password").val();
        var email = $("#info_email_find_password").val();
        var card = $("#student_card_find_password").val();
       if(email.length<1||card.length<1||newPassword.length<1||passwordConfirm.length<1){
            $("#change_password_message").html('Something is Null!');
            $("#change_password_message").show();
        }
        else if (newPassword != passwordConfirm) {
            $("#change_password_message").html('You must input the same password');
            $("#change_password_message").show();
        } else {
            /* Act on the event */
            console.log('here')
           jQuery.ajax({
                url: '/auth/password',
                type: 'POST',
                dataType: 'json',
                data: {
                    'info_email': email,
                    'student_card': card,
                    'new_password':newPassword
                },
                success: function(data, textStatus, xhr) {
                    console.log(data)
                    if (data['code'] == 200) {
                        $("#change_password_message").html('Success');
                        $("#change_password_message").show();
                         setTimeout(function(){

                        $("#signup_dropdown").hide();
                        $("#login_div").fadeIn();
                        $("#find_password_dropdown").hide();
                        $("#find_password_new_pwd").hide();
                        $("#login_message").hide();
                        $("#sign_up_message").hide();
                        $("#change_password_message").hide();
                        $("#find_message").hide();
                        $("#verify_message").hide();
                    },1000);
                    } else {
                        $("#change_password_message").html(data['content']);
                        $("#change_password_message").show();
                    }
                    //called when successful
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log(textStatus)
                        $("#change_password_message").html('Network error!');
                        $("#change_password_message").show();
                }
            });
        }

});

});

