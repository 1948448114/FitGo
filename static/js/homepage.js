$(function(){
    $('.carousel').carousel({
    interval: 2000000
    })
    });

function toTop(){
    $("body").animate({scrollTop:0}, 500);
}