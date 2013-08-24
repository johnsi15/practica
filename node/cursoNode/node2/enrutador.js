function enrutar(manejador,ruta,respuesta){
	console.log("voy a enrutar "+ ruta);
	if(typeof manejador[ruta] === 'function'){
		manejador[ruta](respuesta);
	}else{
		console.log("No existe esa funcion para esa ruta");
	}
}

exports.enrutar = enrutar;