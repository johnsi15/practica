function enrutar(manejador,ruta){
	console.log("voy a enrutar "+ ruta);
	if(typeof manejador[ruta] === 'function'){
		return manejador[ruta]();
	}else{
		console.log("No existe esa funcion para esa ruta");
	}
}

exports.enrutar = enrutar;