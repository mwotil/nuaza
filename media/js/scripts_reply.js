
$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});


function addReplyReview(){
	// build an object of review data to submit
	var reply = { 
	reply: jQuery("#id_reply").val(),
	rate_objective: jQuery("input[name='rate_objective']:checked").val(),
	rate_complete: jQuery("input[name='rate_complete']:checked").val(),
	review: jQuery("#id_review").val(),
	user: jQuery("#id_user").val() };

	// make request, process response
	jQuery.post("/reply/review/add/", reply,
		function(response){
			jQuery("#reply_errors").empty();
			// evaluate the "success" parameter
			if(response.success == "True"){
				// disable the submit button to prevent duplicates
				jQuery("#submit_reply").attr('disabled','disabled');
				// if this is first review, get rid of "no reviews" text
				jQuery("#no_replies").empty();
				// add the new review to the reviews section
				jQuery("#replies").prepend(response.html).slideDown();
				// get the newly added review and style it with color 
				new_reply = jQuery("#replies").children(":first");
				new_reply.addClass('new_reply');
				// hide the review form
				jQuery("#reply_form").slideToggle();
			}
			else{
				// add the error text to the review_errors div
				jQuery("#reply_errors").append(response.html);
			}
		}, "json");	
}


// toggles visibility of "write review" link
// and the review form.
function slideToggleReplyForm(){
	jQuery("#reply_form").slideToggle();
	jQuery("#add_reply").slideToggle();
}


function slideToggleReplies(){
	jQuery("#replies").slideToggle();
}



function prepareDocument(){
	//prepare product review form


	jQuery("#ul.subnav").parent().append("<span></span>"); 
	jQuery("#ul.topnav li span").click(function() {
		jQuery(this).parent().find("ul.subnav").slideDown('fast').show();
		jQuery(this).parent().hover(function() {
		}, function(){
			$(this).parent().find("ul.subnav").slideUp('slow'); 
		});
		}).hover(function() {
			jQuery(this).addClass("subhover");
		}, function(){
			jQuery(this).removeClass("subhover"); 
	});
	jQuery("#submit_reply").click(addReplyReview);
	jQuery("#reply_form").addClass('hidden');
	jQuery("#add_reply").click(slideToggleReplyForm);
	jQuery("#add_reply").addClass('visible');
	jQuery("#cancel_reply").click(slideToggleReplyForm);
	jQuery("#reply_review").click(slideToggleReplies);
	//tagging functionality
	jQuery("#add_tag").click(addTag);
	jQuery("#id_tag").keypress(function(event){
		if (event.keyCode == 13 && jQuery("#id_tag").val().length > 2){
			addTag();
			event.preventDefault();
		}
	});
	statusBox();
}

jQuery(document).ready(prepareDocument);
