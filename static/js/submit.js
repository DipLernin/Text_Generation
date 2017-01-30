$(function(){
	$('#btnsubmit').click(function(){
		var model = $('#model').val();
        var temp = $('#temp').val();
		console.log(model)
		console.log(temp)
		$.getJSON( "http://127.0.0.1:5000/hello", function( data ) {

				console.log(data)
        		$("#output").html(data.result);

    		
    	});

	});
});