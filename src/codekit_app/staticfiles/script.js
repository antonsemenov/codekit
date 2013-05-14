<script type="text/javascript">
        $('html').ajaxSend(function(event, xhr, settings) {
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

        });
</script>



$(document).ready(function() {
    $('#click_me').submit(function (event) {
	event.preventDefault();
	$.ajax({
	
		type:'POST',
		url:'/task/python/1/',
		dataType: 'json',
		csrfmiddlewaretoken: '{{ csrf_token }}',
		data: 'hello2',
		success: function(json){
			alert(json.message);
		}
	});
	return false;
	});
});



 $(function() {
	$( "#sortable1, #sortable2" ).sortable().disableSelection();
	var $tabs = $( "#tabs" ).tabs();
	var $tab_items = $( "ul:first li", $tabs ).droppable({
		accept: ".connectedSortable li",
		hoverClass: "ui-state-hover",
		drop: function( event, ui ) {
			var $item = $( this );
			var $list = $( $item.find( "a" ).attr( "href" ) ).find( ".connectedSortable" );
			ui.draggable.hide( "slow", function() {
				$tabs.tabs( "option", "active", $tab_items.index( $item ) );
				$( this ).appendTo( $list ).show( "slow" );
			});
		}
	});
});
