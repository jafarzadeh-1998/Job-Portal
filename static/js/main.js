
$(document).ready(function(){
			$("#testimonial-slider").owlCarousel({
				items:1,
				itemsDesktop:[1000,1],
				itemsDesktopSmall:[979,1],
				itemsTablet:[768,1],
				pagination: true,
				autoPlay:false
			});
        });	

$("#checkbox-2").click(function(){
    $('.jobseeker-signup').attr("style" ,"display :none;");
    $('.company-signup').attr("style" ,"display :block;");
});

$("#checkbox-1").click(function(){
    $('.jobseeker-signup').attr("style" ,"display :block;");
    $('.company-signup').attr("style" ,"display :none;");
});