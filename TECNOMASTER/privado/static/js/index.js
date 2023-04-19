/*se define la interactividad del sitio privado */


const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");


const btnAbrirModal = document.querySelector("#btn-abrir-modal");
const btnCerrarModal = document.querySelector("#btn-cerrar-modal");
const modal = document.querySelector("#modal");

const directorio = document.querySelector(".directorio");

btnAbrirModal.addEventListener("click", (event)=>{ 
    console.log("hola que ase");
    modal.showModal();
    
});

menuBtn.addEventListener("click", ()=>{
    sideMenu.style.display = "block";
});

closeBtn.addEventListener("click", ()=>{
    sideMenu.style.display = "none";
});

btnCerrarModal.addEventListener("click", ()=>{
    modal.close();
});

/*  */
















