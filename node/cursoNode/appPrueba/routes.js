var couchDB = require('souch');

var db = new couchDB('agenda',{
	user: '',
	passwd: ''
});

var productos = db.newDoc('productos');

exports.index = function(req, res){
	if(!req.query.q){
		var opciones = {
			descending: true
		};
		db.design('productos', { name:'todos', params:opciones }, function(resultados){
			res.render('index', {productos:resultados.rows});
		});
	}else{
		var opciones = {
			descending: true,
			startkey: '["?\u9999,{}"]'.format(req.query.q),
			endkey: '["?"]'.format(req.query.q)
		};
		db.desing('productos', { name:'todos', params:opciones },function(resultados){
			resultados.rows.unique();
			res.render('index', {productos:resultados.rows});
		});
	}
};