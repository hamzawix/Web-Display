

function getdata(){
	$.getJSON('/data', function calldata(d){
		var t = parseFloat(d.t).toFixed(2);
		var c = parseFloat(d.c).toFixed(2);
		var v = parseInt(d.v).toFixed(2);
		console.log(t);
		g.refresh(t);
		k.refresh(c);
		$("#speed").focus();
		$("#speed").val(v);
		$("#speed").submit();
		setTimeout(getdata, 1000);
	});
}
