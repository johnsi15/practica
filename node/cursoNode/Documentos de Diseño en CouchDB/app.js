var express = require('express'),
	app = express(),
	routes = require('./routes');

app.listen(8080);

app.configure(function(){
	app.set('view engine', 'ejs');
	app.set('views', __dirname+'/views')
});

app.get('/', routes.index);
app.get('/detalle/:id', routes.detalle);