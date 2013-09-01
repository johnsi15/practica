var websocket = io.connect();

websocket.on('insertar twit', function(twit){
	document.getElementById('twits').innerHTML +='<p>'+twit+'</p>';
});

document.getElementById('formulario').addEventListener('submit', function(e){
	e.preventDefault();
	websocket.emit('nuevo', this.twit.value);
	this.submit();
});