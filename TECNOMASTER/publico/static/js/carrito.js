const cantidad = document.querySelector(".cantidad_producto");
const total_compra = document.querySelector(".total_compra");
const precio = document.querySelector(".precio_producto_carrito");

console.log(precio.textContent)

cantidad.addEventListener('change', (e)=>{
    const total = e.target.value
    precio2 = total*precio.value
    total_compra.value = precio2
});