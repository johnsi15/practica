var http = require("http");
var url = require("url");
var fs = require("fs");

  console.log("Servidor ON");
function iniciar(enrutar,manejador){
	function arrancarServer(requiere, response){
		var ruta = url.parse(requiere.url).pathname;
		var contenido = enrutar(manejador,ruta);

		var registro = fs.createWriteStream("registro.txt",{"flags":"a"});
		registro.write(ruta + "\n");

		response.writeHead(200,{"Content-Type":"text/html"});
		response.write(contenido);
		response.end();
		
		console.log("Peticion yeah!");
	}
	http.createServer(arrancarServer).listen(3000);
}

exports.iniciar = iniciar;
