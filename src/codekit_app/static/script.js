$(document).ready(function() {
	alert('hello');
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


