
$(document).ready(function(){
	$('div.title').fadeIn(2000).removeClass('hidden');
	$('div.button').fadeIn(2000).removeClass('hidden');
	$("#start").click(function(){
		$('div.gauge').fadeIn(1500).removeClass('hidden');
		$('div.chart').fadeIn(1500).removeClass('hidden');
	});
});

function getdata(){
	$.getJSON('/data', function calldata(d){
		var t = parseFloat(d.t).toFixed(2);
		var c = parseFloat(d.c).toFixed(2);
		var v = parseInt(d.v).toFixed(2);
		g.refresh(t);
		k.refresh(c);
		$("#speed").focus();
		$("#speed").val(v);
		$("#speed").submit();
		setTimeout(getdata, 1000);
	});
}
