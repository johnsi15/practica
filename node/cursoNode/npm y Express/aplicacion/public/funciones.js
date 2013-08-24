var socket = io.connect();

socket.on('insertar twit', function(twit){
	document.getElementById('twits').innerHTML += '<p>'+twit+'</p>';
});

document.getElementById('formulario').addEventListener('submit', function(e){
	e.preventDefault();
	socket.emit('nuevo', this.twit.value);
	this.submit();
});