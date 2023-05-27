
/*se define la interactividad del sitio publico*/
const checkbox = document.querySelector("#btn-menu");
const html = document.querySelector("html");

checkbox.addEventListener("click", (e)=>{
    if (checkbox.checked) {
        html.classList.add("quitar-scroll");
    }
    else{
        html.classList.remove("quitar-scroll");
    }
    
});

const hamburger = document.querySelector(".hamburger");