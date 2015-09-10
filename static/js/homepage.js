$(function(){
    $('.carousel').carousel({
    interval: 2000
    })
    });

function toTop(){
    $("body").animate({scrollTop:0}, 500);
}