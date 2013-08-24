var io = require('socket.io').listen(8080);

io.sockets.on('connection', function(socket){
	/* WebSockets Nativo */
	// socket.on('message', function(mensaje){
	// 	socket.send(mensaje);
	// });
	
	/* WebSockets Socket.IO */
	socket.on('mensaje desde cliente', function(mensaje){
		io.sockets.emit('mensaje desde servidor', mensaje);
	});
});