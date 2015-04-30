$(document).ready(function(){	
	$('.moderaptor form').submit(function() {
		var id = $(this).attr('id');
		$(this).ajaxSubmit({
			dataType: 'json',
			success: function(data, responseCode) {
				$('#'+id).html(data.message).fadeOut(3000);
			}
		});
        return false; 
    });
	$('.moderaptor_toggle').click(function(){		
		$(this).parent().next('form').toggle('slow');
	});
});

