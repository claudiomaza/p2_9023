// Configurar portafolio
const projectName = "portfolio";
localStorage.setItem("my_personal_portfolio", "Personal Portfolio");

// Función para obtener datos del perfil de GitHub
(function() {
  const url = "https://api.github.com/users/carlosandresalzate";
  const nombre = document.getElementsByClassName("navbar-brand");
  
  fetch(url)
    .then((resp) => resp.json())
    .then((data) => {
      nombre[0].textContent = data.name;
    })
    .catch((error) => console.error("Error al cargar los datos: ", error));
})();
