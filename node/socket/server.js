var io = require('socket.io').listen(80);

io.sockets.on('connection', function (socket) {
  socket.emit('news', { hello: 'Hola mundo como estamos' });
  socket.on('evento', function (data) {
    console.log(data);
  });
});