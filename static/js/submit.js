$(function(){
	$('#btnsubmit').click(function(){
        $('#btnsubmit').prop('disabled', true);
		var model_name = $('#model').val();
        var warm_text = $('#warm').val();
        var count_char = $('#char').val();
        var number = $('#num').val();
        var temp = $('#temp').val();

        if (warm_text==='') warm_text='blabla';
        if (count_char==='') count_char='\\n';
        if (number==='') number='20';
        if (temp==='') temp='0.4';

        var port = '8889';
        var server = 'localhost';
		var uri = 'http://'+ server + ':' + port + '/models/';
		var params = model_name + '?' + 'num=' + number + '&cchar=' + count_char + '&temp=' + temp + '&warm=' + warm_text;
		var url = uri + params;
		console.log(url);

		$.getJSON( url, function( data ) {
						data.result = data.result.replace(/\n/g, '<br>')
						console.log(data.result)
        		        $("#output").html(data.result);
                        $('#btnsubmit').prop('disabled', false);
    	});


	});
});
