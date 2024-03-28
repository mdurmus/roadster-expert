$(document).ready(function(){
    setTimeout(function(){
        $('#msg').alert('close');
    }, 2500);
});

$(document).ready(function(){
    $('#searchButton').click(function(){
        $('#staticBackdrop').modal('show');
    });

})

//Change Navbar color and background on scroll
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(document).scrollTop() > 20) {
            $(".navbar").addClass("nav-active");
            $(".nav-link").addClass("nav-active");
            $(".navbar-brand img").addClass("nav-active");
        } else {
            $(".navbar").removeClass("nav-active");
            $(".nav-link").removeClass("nav-active");
            $(".navbar-brand img").removeClass("nav-active");
        }
    });
});