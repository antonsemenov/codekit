$(document).ready(function() {
    $('#click_me').submit(function (event) {
	event.preventDefault();
	$.ajax({
		type:'POST',
		url:'/task/python/1/',
		dataType: 'json',
		csrfmiddlewaretoken: '{{ csrf_token }}',
		data: {lang: "python", code: getCode()},
		success: function(json){
			alert(json['pi']);
		}
		
	});
	return false;
	});
});


function getCode(){
	var code = '';
	$('#sortable1 > li').each(function(i){
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
			ui.draggable.hide( "slow", function() {
				$tabs.tabs( "option", "active", $tab_items.index( $item ) );
				$( this ).appendTo( $list ).show( "slow" );
			});
		}
	});
});
