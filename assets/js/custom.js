// Ejemplo: Mostrar un mensaje en la consola al cargar la página
console.log("Bienvenido a la documentación de ATLANTYDE");

// Ejemplo: Agregar funcionalidad para resaltar el menú activo
document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".md-nav__link");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });
});