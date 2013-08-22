var server = require("./servidor");
var enrutador = require("./enrutador");
var peticiones = require("./peticiones");

var manejador = {}
manejador["/"] = peticiones.inicio;
manejador["/hola"] = peticiones.hola;
manejador["/favicon.ico"] = peticiones.favicon;

server.iniciar(enrutador.enrutar, manejador);