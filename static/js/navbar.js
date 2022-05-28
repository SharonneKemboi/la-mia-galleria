$(window).scroll(() => {
    if ($(document).scrollTop() > 450) {
        $("nav").addClass("shrink")

    } else  {
        $("nav").removeClass("shrink")
    }
})