var couchDB = require('souch');

var db = new couchDB('agenda',{
	user: '',
	passwd: ''
});

var producto = db.newDoc('producto');

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

exports.agregar = function(req, res){
	res.render('agregar');
};

exports.add = function(req, res){
	var post = req.body;
	if(post && post.nombre && post.precio){
		post.precio = parseInt(post.precio);
		//post.user = req.session.user;
		post.created = Date.parse(new Date());
		producto.post(post, function(result){
			if(result.ok){
				res.redirect('/');
			}else{
				res.send(500, 'Algo ha salido mal');
			}
		});
	}
};