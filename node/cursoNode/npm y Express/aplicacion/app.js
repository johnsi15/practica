/* Variables */
var express = require('express'),
	routes = require('./routes'),
	app = express(),
	server = require('http').createServer(app),
	io = require('socket.io').listen(server);

server.listen(8080);

/* Configuracion */
app.configure(function(){
	app.set('view engine', 'ejs');
	app.set('views', __dirname+'/views') // C:/Users/Samuel BR/Desktop/NodeJS/aplicacion/views
	app.use(express.bodyParser());
	app.use('/static', express.static(__dirname+'/public'));
});

/* Rutas */
// POST - GET - PUT - DELETE - OPTIONS - HEAD
app.get('/', routes.index);
app.post('/nuevo', routes.nuevo);

/* Socket.IO */
io.sockets.on('connection', function(socket){
	socket.on('nuevo', function(twit){
		io.sockets.emit('insertar twit', twit);
	});
});