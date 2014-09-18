/*
	Name: cvCard
	Description: Responsive HTML5 vCard Template
	Version: 1.0
	Author: pixelwars
*/



/* global variables */
var classicLayout = false;
var portfolioKeyword;
var $container, $blog_container;


(function ($) {
	
	
	/* DOCUMENT LOAD */
	$(function() {
		
		
		// ------------------------------
		// remove click delay on touch devices
		FastClick.attach(document.body);
		// ------------------------------
		
		
		// ------------------------------
		// start loader
		NProgress.start();
		// ------------------------------
		
		
		// ------------------------------
		// Rotating Words
		var rotate_words = $('.rotate-words');
		if(rotate_words.length && Modernizr.csstransforms) {
			rotate_words.find('span').eq(0).addClass('active');
			setInterval(function(){
				next_word_index = rotate_words.find('.active').next().length ? rotate_words.find('.active').next().index() : 0;
				rotate_words.find('.active').addClass('rotate-out').removeClass('rotate-in active');
				rotate_words.find('span').eq(next_word_index).addClass('rotate-in active').removeClass('rotate-out');
			},3000);
		}
		// ------------------------------
		
		
		// ------------------------------
		/* LATEST TWEETS WIDGET
		  * ### HOW TO CREATE A VALID ID TO USE: ###
		  * Go to www.twitter.com and sign in as normal, go to your settings page.
		  * Go to "Widgets" on the left hand side.
		  * Create a new widget for what you need eg "user timeline" or "search" etc. 
		  * Feel free to check "exclude replies" if you dont want replies in results.
		  * Now go back to settings page, and then go back to widgets page, you should
		  * see the widget you just created. Click edit.
		  * Now look at the URL in your web browser, you will see a long number like this:
		  * 345735908357048478
		  * Use this as your ID below instead!
		  */
		var latest_tweets = $('#latest-tweets');
		if(latest_tweets.length) {
			twitterFetcher.fetch(latest_tweets.attr("data-twitterId"), '', latest_tweets.attr("data-tweet-count"), true, false, true, '', false, handleTweets);
		}
		function handleTweets(tweets){
		  var x = tweets.length;
		  var n = 0;
		  var html = '<ul>';
		  while(n < x) {
			html += '<li>' + tweets[n] + '</li>';
			n++;
		  }
		  html += '</ul>';
		  latest_tweets.html(html);
		}	
		// ------------------------------  
		
		
		// ------------------------------
		// SETUP
		setup();
		// ------------------------------
		
		
		// ------------------------------
		// FILL SKILL BARS
		fillBars();
		// ------------------------------
		
		
		// ------------------------------
		/* TOOLTIPS */
		$('.tooltip').each(function(index, element) {
        	$(this).tooltipster({
			position: $(this).attr('data-tooltip-pos'),
			fixedWidth : 300,
			offsetX : 8,
			animation : "grow",
			delay : 50
			});
	 
        });	
		// ------------------------------
		
		
		
		
		
	});	

	
	// WINDOW ONLOAD
	window.onload = function() {
		
		NProgress.done();
	
	};
	// WINDOW ONLOAD	
	
	
	
	// ------------------------------
	// ------------------------------
		// FUNCTIONS
	// ------------------------------
	// ------------------------------
	
	
	// ------------------------------
	// INITIALIZE
	var inAnimation, outAnimation;
	function initialize() {
		inAnimation = $('html').attr('data-inAnimation');
		outAnimation = $('html').attr('data-outAnimation');
	}
	// ------------------------------
	
	
	// ------------------------------
	// SETUP : plugins
	function setup() {

		// ------------------------------
		// CODE PRETTIFY
		// Compatibity
		$('pre').each(function() {
			var cl = $(this).attr('class');
			if(cl) {
				$(this).attr('class', cl.replace('brush: ', 'prettyprint lang-'));
			}
		});

		if($('.prettyprint').length) {
			window.prettyPrint && prettyPrint();
		}
		// ------------------------------
		
		
		
		// ------------------------------
		// TABS
		$('.tabs').each(function() {
			if(!$(this).find('.tab-titles li a.active').length) {
				$(this).find('.tab-titles li:first-child a').addClass('active');
				$(this).find('.tab-content > div:first-child').show();
			} else {
				$(this).find('.tab-content > div').eq($(this).find('.tab-titles li a.active').parent().index()).show();	
			}
		});
		
		$('.tabs .tab-titles li a').click(function() {
			if($(this).hasClass('active')) { return; }
			$(this).parent().siblings().find('a').removeClass('active');
			$(this).addClass('active');
			$(this).parents('.tabs').find('.tab-content > div').hide().eq($(this).parent().index()).show();
			return false;
		});
		// ------------------------------
		
		
		// ------------------------------
		// TOGGLES
		var toggleSpeed = 300;
		$('.toggle h4.active + .toggle-content').show();
	
		$('.toggle h4').click(function() {
			if($(this).hasClass('active')) { 
				$(this).removeClass('active');
				$(this).next('.toggle-content').stop(true,true).slideUp(toggleSpeed);
			} else {
				
				$(this).addClass('active');
				$(this).next('.toggle-content').stop(true,true).slideDown(toggleSpeed);
				
				//accordion
				if($(this).parents('.toggle-group').hasClass('accordion')) {
					$(this).parent().siblings().find('h4').removeClass('active');
					$(this).parent().siblings().find('.toggle-content').stop(true,true).slideUp(toggleSpeed);
				}
				
			}
			return false;
		});
		// ------------------------------
		
			
	}
	// ------------------------------
	
	
		
	// ------------------------------
	// FILL PROGRESS BARS
	function fillBars() {
		$('.bar').each(function() {
			 var bar = $(this);
			 bar.find('.progress').css('width', bar.attr('data-percent') + '%' );
			});
	}	
	// ------------------------------	
	
	
	// ------------------------------
	// AJAX LOADER
	function showLoader() {
		NProgress.start();
	}
	function hideLoader() {
		NProgress.done();
	}
	// ------------------------------
	
	
	
	


})(jQuery);