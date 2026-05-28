import  {productos} from "./productos.js"

const contenedor= document.getElementById("contenedor-productos");

productos.forEach(producto  => {
    contenedor.innerHTML += `
    <div class="card">
     <img class=card-img" src="${producto.img}" alt="">
     <h2 class=card-h2">${producto.nombre}</h2>
     <p class=card-p">${producto.precio}</p>
     <button class="comprar" onclick="verdetalle(${producto.id})">comprar</button>
    </div>
    `
} )
window.verDetalle = (id) => {
    window.location.href =  `detalle_producto.html?id=${id}`; 
}
