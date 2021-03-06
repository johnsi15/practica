var express = require('express'),
	routes = require('./routes'),
	app = express();

app.listen(8080);

app.configure(function(){
	app.set('view engine', 'ejs');
	app.set('views', __dirname+'/views');
	app.use('/static', express.static(__dirname+'/public'));
	app.use(express.bodyParser());
});

/*Rutas */ 
app.get('/', routes.index);

app.get('/agregar', routes.agregar);
app.post('/agregar', routes.add);

app.post('/delete/:id', routes.delete);

app.get('/editar/:id', routes.editar);
app.post('/editar/:id', routes.edit);