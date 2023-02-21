const search = document.querySelector("#search");
search.addEventListener("focus", (event)=> {
    console.log('119191')
    search.removeAttribute('placeholder')
    search.style.padding = "0px 20px 0px 50px"
    let button = document.querySelector(".search-form");
        button.classList.toggle("icon");
    let body = document.querySelector("body");
});

search.addEventListener("blur", (event)=> {
    search.setAttribute('placeholder', 'Procure pelo nome ou tipo do produto')
    search.style.padding = "0px 20px"
    let button = document.querySelector(".search-form");
        button.classList.toggle("icon");
});


const cep = document.querySelector("#id_cep");
cep.addEventListener("blur", (event)=> {
    fetch(`https://viacep.com.br/ws/${cep.value}/json/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        estado_value = data.uf
        cidade_value = data.localidade
        bairro_value = data.bairro
        logradouro_value = data.logradouro

        document.querySelector("#id_state").value = estado_value ? estado_value : '';
        document.querySelector("#id_city").value = cidade_value ? estado_value : '';
        document.querySelector("#id_district").value = bairro_value ? bairro_value : '';
        document.querySelector("#id_address").value = logradouro_value ? bairro_value : '';

    })
    .catch(error => console.error(error));
});

