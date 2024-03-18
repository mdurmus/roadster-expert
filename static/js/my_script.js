// Add year on the footer copyright
$("#year").text(new Date().getFullYear());
//Parallax effect on scrool
$(window).scroll(function () {
    parallax();
});

function parallax() {
    var wScroll = $(window).scrollTop();
    $(".parallax").css("background-position",
        "center " + (wScroll * 0.60) + "px");
}

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

// Open search box panel
$(document).ready(function () {
    $("#search-box-button").click(function () {
        $("#search-box").addClass("active-box");
    });
});

// Close search box panel
$(document).ready(function () {
    $("#search-box .fa-times").click(function () {
        $("#search-box").removeClass("active-box");
    });
});

// Smooth scrolling to all links
$("a").on('click', function (e) {
    if (this.hash !== "") {
        // Prevent default anchor click behavior
        e.preventDefault();
        // Store hash
        var hash = this.hash;
        // Using jQuery's animate() method to add smooth page scroll
        $('html, body').animate({
            scrollTop: $(hash).offset().top
        }, 800);
    }
    // End if
});