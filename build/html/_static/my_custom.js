/* $(document).ready(function(){
    let div_logo = document.getElementsByClassName("wy-side-nav-search")[0];
    let a_logo = div_logo.getElementsByTagName("a");
    a_logo[0].href = "http://192.168.20.241:8090/index";
    a_logo[0].target = "_blank";
}); */

$(document).ready(function() {
    $(".wy-side-nav-search a:first").attr("href", "http://192.168.20.241:8090/index");
    $(".wy-side-nav-search a:first").attr("target", "_blank");
});