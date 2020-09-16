var $ = jQuery.noConflict();

$(document).ready(function() {

$('html').attr('id', 'js'); // Enabled Javascript Detection

if($("a[rel=external]")){
	$("a[rel=external]").click(function() {
		window.open(this.href);  
		return false;
	});
}

if ($('#home_slider_box').length) {
	$('#home_slider').cycle({ 
		fx      :   'fade',
		timeout :   5000,
		next	:   '#slider_next', 
		prev	:   '#slider_prev',
		pager	:	'#slider_nav' 
	});
}

if ($('#int_slider_box').length) {
	$('#int_slider').cycle({ 
		fx      :   'fade',
		timeout :   5000,
		next	:   '#slider_next', 
		prev	:   '#slider_prev',
		pager	:	'#slider_nav' 
	});
}

if ($('.book_card').length) {
	$('.book_card').fancybox({
		maxWidth	: 470,
		maxHeight	: 600,
		fitToView	: false,
		width		: 470
	});
}

if ($('.activate_card').length) {
	$('.activate_card').fancybox({
		maxWidth	: 470,
		maxHeight	: 600,
		fitToView	: false,
		width		: 470
	});
}





$('#tabs_header a').click(function() {
	var currentTabClass = $(this).parent('li').attr('class');
	var currentTab = $(this).attr('href');
	$('#tabs_header').removeClass('red blue');
	$('#tabs_header').addClass(currentTabClass);
	$('#tabs_box div.entry-content').hide();
	$(currentTab).show();
	return false;
});

$('.autoclear').autoClear();

$('#tabs a').click(function() {
	$('#tabs li').removeClass('active');
	$(this).parent('li').addClass('active');
	var currentTab = $(this).attr('href');
	$('.partner-description div').hide();
	$(currentTab).show();
	return false;
});

$(".btn_comments").click(function(){
	$(".comments_form").slideToggle("slow");
	$(this).toggleClass("active");
	return false;
});


});

(function($) {
    $.fn.autoClear = function () {
        $(this).each(function() {
            $(this).data("autoclear", $(this).attr("value"));
        });
        $(this)
            .bind('focus', function() {   
                if ($(this).attr("value") == $(this).data("autoclear")) {
                    $(this).attr("value", "").addClass('autoclear-normalcolor');
                }
            })
            .bind('blur', function() {  
                if ($(this).attr("value") == "") {
                    $(this).attr("value", $(this).data("autoclear")).removeClass('autoclear-normalcolor');
                }
            });
        return $(this);
    }
})(jQuery)

$.fn.equalHeights = function() { 
	var currentTallest = 0; 
	$(this).each(function(){ 
		if ($(this).height() > currentTallest) { currentTallest = $(this).height(); }
	}); 
	$(this).parent().parent().css({'height': currentTallest}); 
	$(this).parent().css({'height': currentTallest});  
	$(this).css({'height': currentTallest});  
	return this; 
}; 