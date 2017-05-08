
function calltemp(t,status){
	if (status == "success") {
		temp = parseFloat(t).toFixed(2);
		g.refresh(temp);
		setTimeout(gettemp, 1000);
	}
}

function callcarb(c, status){
	if (status == "success"){
		carb = parseFloat(c).toFixed(2);
		k.refresh(carb);
		setTimeout(getcarb, 1000);
	}
}

function callvit(v, status){
	if (status == "success"){
		vit = parseFloat(v).toFixed(2);
		l.refresh(vit);
		setTimeout(getvit, 1000);
	}
}

function gettemp(){
	$.get('/temp', calltemp);
}

function getcarb(){
	$.get('/carb', callcarb);
}

function getvit(){
	$.get('/vit', callvit);
}