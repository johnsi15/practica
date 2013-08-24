function inicio(respuesta){
	console.log("Hola soy inicio");
	respuesta.writeHead(200,{"content-type":"text/html"});
	respuesta.write("<h1>Bienvenido al menu de Inicio<h1>")
	respuesta.end();
}

function hola(respuesta){
	console.log("Hola soy hola");
	respuesta.writeHead(200,{"content-type":"text/html"});
	respuesta.write("<h1>Hola estas probando una peticion con node js :D<h1>")
	respuesta.end();
}

function favicon(respuesta){
	console.log("Se ha pedido el favicon");
	respuesta.writeHead(200,{"content-type":"text/html"});
	respuesta.write("")
	respuesta.end();
}

exports.inicio = inicio;
exports.hola = hola;
exports.favicon = favicon;