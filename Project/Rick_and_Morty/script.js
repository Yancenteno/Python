const rickApi = "https://rickandmortyapi.com/api/character/";
const rickName = document.querySelector("#rickName");
const cardContainer = document.querySelector('#card-group');

function cards() {
    event.preventDefault();

    fetch(rickApi + "?name=" + rickName.value)
        .then((response) => response.json())
        .then(data => {
            const character = data.results[0];
            if (character) {
                cardContainer.innerHTML =
                    `<div class="card">
                        <h2>${character.name}</h2>
                        <h4>Status: ${character.status}</h4>
                        <h4>Species: ${character.species}</h4>
                        <h4>Gender: ${character.gender}</h4>
                        <img src="${character.image}">
                    </div><br>`;
            }
        })
        .catch(err => console.log(err));
}


