var models = require('./models');

exports.index = function(req, res){
	res.render('index', {title:'Aplicacion de ejemplo', twits:models.twits});
};

exports.nuevo = function(req, res){
	if(req.body && req.body.twit){
		models.twits.push(req.body.twit);
		res.redirect('/');
	}else{
		res.send(404, 'Not found!');
	}
};