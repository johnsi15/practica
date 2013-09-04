var express = require('express'),
	routes = require('./routes'),
	app = express();

app.listen(8080);

app.configure(function(){
	app.set('view engine', 'ejs');
	app.set('views', __dirname+'/views');
});

app.get('/', routes.index);
app.get('/detalle/:id', routes.detalle);//con :id se pasa el id del valor como parametro