function inicio(){
	console.log("Hola soy inicio");
	return "<h1>Bienvenido al menu de Inicio<h1>";
}

function hola(){
	console.log("Hola soy hola");
	return "Hola estas probando una peticion con node js :D";
}

function favicon(){
	console.log("Se ha pedido el favicon");
	return "";
}

exports.inicio = inicio;
exports.hola = hola;
exports.favicon = favicon;