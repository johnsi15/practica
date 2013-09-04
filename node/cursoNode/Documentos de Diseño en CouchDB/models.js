// nano - couch - souch
var http = require('http');

module.exports = function(ruta, callback){
	var options = {
		host: 'localhost',
		port: 5984,
		path: ruta,
		method: 'GET'
	};
	var resultados = '';
	var req = http.request(options, function(res){
		res.setEncoding('utf8');
		res.on('data', function(inf){
			resultados += inf;
		});
		res.on('end', function(){
			callback(JSON.parse(resultados)); // results.rows.item
		});
	});
	req.end();
};