function item_click(){
   
    var curIndex = 0,
        //记录当前已经添加active类的li的索引号
        //查找所有被点击的元素对象
        timeLine = document.getElementById("timeline"),
        clickArea = timeLine.getElementsByTagName("s"),
        //查找所有li元素对象
        timePoint = timeLine.getElementsByTagName("li");

    //为每个被点击的对象绑定单击事件
    for( var i = 0, len = clickArea.length; i < len; i++ ){
        (function( i ){
                clickArea[i].onclick = function(){
                //为被点击的时间点li添加active类
                timePoint[i].className = "active";
                //根据索引号变量的值，去除上一个li的active类
                timePoint[curIndex].className = "";
                //将索引号变量值更新为被点击的li的索引号
                curIndex = i;
            };
        })( i );
    }
 };

    $(document).ready(function() {


    $("#invite_new_btn").click(function(event) {
    /* Act on the event */
    
    $("#create_new_invite").show('slow/400/fast');
    $("#invite_more_detail").hide();
    $(".invite_block").hide();
    $("#invite_message_list").hide();
    $("#invite_message_all_list").hide();
    });

    $("#search_more_btn").click(function(event) {
    /* Act on the event */
    $(".invite_block").show();
    $("#invite_more_detail").show('slow/400/fast');
    $("#create_new_invite").hide();
    $("#invite_message_list").hide();
    $("#invite_message_all_list").hide();
    });


   $("#invite_message_btn").click(function(event) {
    /* Act on the event */
    $(".invite_block").hide();
    $("#invite_more_detail").hide();
    $("#create_new_invite").hide();
    $("#invite_message_list").fadeIn();
    $("#invite_message_all_list").hide();
    });

   $("#invite_message_all_btn").click(function(event) {
    /* Act on the event */
    $(".invite_block").hide();
    $("#invite_more_detail").hide();
    $("#create_new_invite").hide();
    $("#invite_message_all_list").fadeIn();
    $("#invite_message_list").hide();
    });



    
    $("#search_invite_start_time").datetimepicker({
    
    startView: 2,
    forceParse: 0,
    showMeridian: 1,
    autoclose: true,
    todayBtn: true,
    todayHighlight:true
    });
    $("#create_invite_start_time").datetimepicker({
    
    startView: 2,
    forceParse: 0,
    showMeridian: 1,
    autoclose: true,
    todayBtn: true,
    todayHighlight:true
    
    });
    $("#search_invite_time").datetimepicker({
    format: 'yyyy-mm-dd',
    minView:"month",
    todayHighlight:true,
    autoclose: true,
    todayBtn: true,
    });
    });
    $(function() {
    $("#menu .home").removeClass("home");
    $($("#menu .bar").get(3)).addClass("home");
    });
