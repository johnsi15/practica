var express = require("express");//mandamos a traer los archivos de express
var app = express();//aca creamos el servicio o servidor

app.get('/', function(req, res){//con esto cuando estamos en localhost:3000 nos manda el mensaje
	res.send('Hello World desde Express mi primer servidor desde express');
});

app.get('/usuario', function(req, res){//esto es otro llamado en localhost:3000/usuario
	res.send('Registrar Usuario');
});

app.listen(3000);