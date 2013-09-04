// nano - couch - souch librerias
var http = require('http');

module.exports = function(ruta, callback){
	var options = {
		host: 'localhost',
		port: 5984,
		path: ruta,
		method: 'GET'
	};
	var resultado = '';
	var req = http.request(options, function(res){
		res.setEncoding('utf8');
		res.on('data', function(inf){
			resultado += inf;
		});
		res.on('end', function(){
			callback(JSON.parse(resultado));
		})
	});
	req.end();
};