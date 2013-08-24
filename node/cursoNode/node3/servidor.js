var http = require("http");
var url = require("url");
var fs = require("fs");

  console.log("Servidor ON");
function iniciar(enrutar,manejador){
	function arrancarServer(requiere, response){
		var ruta = url.parse(requiere.url).pathname;
		console.log(ruta);

		if(ruta == "/"){
			ruta ="index.html";
		}

		//var contenido = enrutar(manejador,ruta,response);

		var index = fs.readFileSync("www/"+ruta);

		var registro = fs.createWriteStream("registro.txt",{"flags":"a"});
		registro.write(ruta + "\n");

		response.writeHead(200,{"Content-Type":"text/html"});
		response.write(index);
		response.end();
		
		console.log("Peticion yeah!");
	}
	http.createServer(arrancarServer).listen(3000);
}

exports.iniciar = iniciar;
