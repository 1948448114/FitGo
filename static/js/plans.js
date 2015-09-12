$(document).ready(function() {
    var plan = {
        'content': {
            'target': '',
            'signature': '',
            'start_time': '',
            'end_time': '',
        }
    };

    function init() {
        $("#menu .home").removeClass("home");
        $($("#menu .bar").get(2)).addClass("home");
        $(".yesShow1").hide();
        $(".yesShow2").hide();
        $(".yesShow3").hide();
        $(".yesShow4").hide();
        $(".yesShow5").hide();
        $(".yesShow6").hide();
        $(".yesShow7").hide();
        $('.reservationtime').daterangepicker({
            timePicker: true,
            timePickerIncrement: 30,
            format: 'MM/DD/YYYY h:mm A'
        }, function(start, end, label) {
            console.log(start.toISOString(), end.toISOString(), label);
        });



        $('.restButton').each(function(index, el) {
            $(this).bind('click', function() {
                var activeTab = $(event.target).val();
                var nextTab = (parseInt(activeTab) + parseInt('1')).toString();
                var radio_value = $('.radio' + activeTab + ' input[name="ifrest' + activeTab + '"]:checked').val();
                if (radio_value == "disagree") {
                    $('.yesShow' + activeTab).show();
                } else if (radio_value == null) {
                    alert("Please Choose one!")
                } else {
                    $('.yesShow' + activeTab).hide();
                    $('#myTab a[href="#' + nextTab + '"]').tab('show');
                }
            });
        });
    };


    function newPlan() {
        $("#btnPaopao").click(function(event) {
            $(".pages .tab-pane").each(function(index, el) {
                var index1 = index;
                value = $(this).find('input[name="ifrest' + index1 + '"]:checked').val();
                if (value == 'disagree') {
                    plan['content'][index1] = {
                        'selectValue': [],
                        'inputValue': []
                    }
                    $(this).find("select").each(function(index, el) {
                        plan['content'][index1]['selectValue'].push($(this).val());
                    });
                    $(this).find("input.userInput1").each(function(index, el) {
                        plan['content'][index1]['inputValue'].push($(this).val());
                    });
                }

            });
            plan['content']['target'] = $("#Target").val();
            plan['content']['signature'] = $("#signature").val();
            plan['content']['start_time'] = $("#reservationtime").val();
            plan['content']['end_time'] = '';
            console.log(JSON.stringify(plan));
            jQuery.ajax({
                url: '/plans',
                type: 'POST',
                dataType: 'json',
                data: {
                    'plan': JSON.stringify(plan)
                },
                success: function(data, textStatus, xhr) {
                    //called when successful
                    if (data['code'] == 200) {
                        $("#btnPaopao").attr('data-content','Success');
                        $("#btnPaopao").popover('show');
                    } else {
                        $("#btnPaopao").attr('data-content', data['content']);
                        $("#btnPaopao").popover('show');
                    }
                },
                error: function(xhr, textStatus, errorThrown) {
                    $("#btnPaopao").attr('data-content', 'Network Error!');
                    $("#btnPaopao").popover('show');
                }
            });

        });
    }


    init();
    newPlan();
});






                //  '1':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '2':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '3':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '4':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '5':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '6':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // },
                // '7':{
                //     'oxygen':'',
                //     'noxygen':'',
                //     'lashen':''
                // }

























