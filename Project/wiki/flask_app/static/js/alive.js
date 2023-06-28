const rickList = document.getElementById("rick-list");
const loadMoreButton = document.getElementById("load-more");
let nextPage = 1;

loadMoreButton.addEventListener("click", fetchCharacters);

function fetchCharacters() {
    const rickApi = `https://rickandmortyapi.com/api/character/?page=${nextPage}&name&status=alive`;

    fetch(rickApi)
        .then(response => response.json())
        .then(data => {
            data.results.forEach(character => {
                const characterCard = createCard(character);
                rickList.appendChild(characterCard);
            });

            nextPage++;
        })
        .catch(err => console.log(err));
}


fetchCharacters();

function createCard(character) {
    const characterCard = document.createElement("div");
    characterCard.className = "characterCard";
    characterCard.innerHTML = `
    <img class="pic" src="${character.image}" >
    <h2>${character.name}</h2>
    <p>Status: ${character.status}</p>
    <p>Species: ${character.species}</p>
  `;

    return characterCard;
}





