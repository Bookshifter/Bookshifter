function openDropdown() {
    var dropdownTrigger = document.getElementById("trigger-search");
    if (dropdownTrigger) {
        dropdownTrigger.classList.add("active");
    }
}

function searchAndUpdateDropdown(url) {
    var searchValue = document.getElementById("search-bar").value;
    var loader = document.getElementById("loader");
    var search_loader = document.getElementById("search-loader");

    search_loader.style.display = "none"
    loader.style.display = "block"

    // Faça a chamada à API usando fetch
    // Substitua 'valor' na URL pelo valor digitado pelo usuário (searchValue)
    if (url.includes('host.docker.internal')) {
        url = url.replace("host.docker.internal", "localhost")
    }

    var apiUrl = url + "asn/list_all_asns_ix_filtered/?filter=" + searchValue;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                search_loader.style.display = ""
                loader.style.display = "none"
                throw new Error('Erro ao chamar a API do cadastro');
            }
            return response.json();
        })
        .then(data => {
            // Adicione os novos valores ao dropdown
            if (data.length == 0) {
                alert("Nenhum ASN encontrado.")
                search_loader.style.display = ""
                loader.style.display = "none"
                
            } else {
                // Limpe o conteúdo atual do dropdown
                var dropdown = document.getElementById("filter-list");
                dropdown.innerHTML = "";
                // Caso haja elementos em data, adicione-os ao dropdown
                data.forEach(item => {
                    var li = document.createElement("li");
                    var anchor = document.createElement("a");
                    anchor.textContent = item.organization_name;item.organization_name;
                    li.setAttribute("onclick", `selectAsnIx(${item.number})`);
                    li.appendChild(anchor);
                    dropdown.appendChild(li);
                    search_loader.style.display = ""
                    loader.style.display = "none"
                    openDropdown();
                    
                });
            }
        })
        .catch(error => {
            console.error("Erro ao chamar a API do cadastro: " + error);
        });
}