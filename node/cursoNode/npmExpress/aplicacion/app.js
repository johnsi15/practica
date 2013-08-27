/* Variabes */
var express = require('express'),
	routes = require('./routes');
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io').listen(server);

server.listen(8080);

/* Configuraciones */
app.configure(function(){
	app.set('view engine', 'ejs');
	app.set('views', __dirname+'/views'); //C:\Users\LARED.COM\Documents\GitHub\practica\node\cursoNode\npmExpress\aplicacion\views
	//app.use(express.bodyParser());
	//app.use('/static', express.static(__dirname+'/public'));
});

/* Rutas */ /* POST - GET - PUT - DELETE - OPTIONS - HEAD */
app.get('/', routes.index);