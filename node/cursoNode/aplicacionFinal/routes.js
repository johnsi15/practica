var peticion = require('./models');

exports.index = function(req, res){
	peticion('/agenda/_design/personas/_view/todas', function(resp){
		res.render('index', {todos:resp.rows});
	});
};

exports.detalle = function(req, res){
	peticion('/agenda/'+req.params.id, function(resp){
		res.render('detalle', {persona:resp});
	});
};