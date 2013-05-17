$(document).ready(function() {
    $('#click_me').submit(function (event) {
	event.preventDefault();
	
	
	$.ajax({
		url:'.',
		type:'POST',
		dataType: 'json',
		async: false,
		csrfmiddlewaretoken: '{{ csrf_token }}',
		data: {code: getCode()},
		success: function(json){ resultViewer(json)}
	});
	return false;
	});
});



function resultViewer(json){
	$('.well').html('<h1>'+json['result']+'</h1>');
	$('.well').append('<br><hr><a href=".">Try again</a> <a href="../../../">Choose the task</a>');
	}


function getCode(){
	var code = '';
	$('#sortable1 > li > pre').each(function(i){
		code += $(this).html();
		code +='\n';
	});
	return code;
}


 $(function() {
	$( "#sortable1, #sortable2" ).sortable().disableSelection();
	var $tabs = $( "#tabs" ).tabs();
	var $tab_items = $( "ul:first li", $tabs ).droppable({
		accept: ".connectedSortable li",
		hoverClass: "ui-state-hover",
		drop: function( event, ui ) {
			var $item = $( this );
			var $list = $( $item.find( "a" ).attr( "href" ) ).find( ".connectedSortable" );
			ui.draggable.hide( "norma", function() {
				$tabs.tabs( "option", "active", $tab_items.index( $item ) );
				$( this ).appendTo( $list ).show( "slow" );
			});
		}
	});
});
