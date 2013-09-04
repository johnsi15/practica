var http = require('http');

var options = {
	host: 'localhost',
	port: 5984,
	method: 'POST',
	path: '/ejemplo',
	headers: {
		"Content-Type":"application/json"
	}
};

var resultado = '';
var req = http.request(options, function(res){
	res.on('data', function(data){
		resultado += data;
	});
	res.on('end', function(){
		console.log(resultado);
	});
});

var data = {
	nombre:"Hola Mundo",
	info: "mas",
	numero: 7854
};

req.write(JSON.stringify(data));//convertimos el objeto data en JSON con JSON.stringify
req.end();