function changeVisibility(element) {
    var menuCix = document.getElementById('menu-cix'); // MENU DE ASN
    var checkCixListed = document.getElementById('check-cix-listed'); // INPUT DE ASN
    var formContactCix = document.getElementById('form-contact-cix'); // FORM DE CONTATO
    var inputs = formContactCix.querySelectorAll('input'); // TODOS OS INPUTS DO FORMULÁRIO DA PRIMEIRA ABA
    // Menu de ADM checkado
    if (element.name == "is_cix_provider") {
        if (element.checked) {
            // is_cix_provider checkado
            menuCix.removeAttribute('hidden', ''); // mostrar menu cix
            // Adiciona os requireds para que seja obrigatório o campo
            inputs.forEach( function xyz(e) {
                if (e.name != 'customer_cix_contact_phone_ramal') e.setAttribute('required','');
            } );
        }
        else if (!element.checked) {
            // is_cix_provider descheckado
            checkCixListed.checked = false; // descheck na listagem
            menuCix.setAttribute('hidden', ''); // esconde menu cix
            formContactCix.setAttribute('hidden', ''); // esconde form cix
            // Remove os requireds para que o form não seja enviaod
            inputs.forEach( function xyz(e) {
                if (e.name != 'customer_cix_contact_phone_ramal') e.removeAttribute('required','');
            } );
        }
    } else if (element.name == 'is_cix_provider_listed') {
        if (element.checked) {
            formContactCix.removeAttribute('hidden', '') // mostrar form cix
            inputs.forEach( function xyz(e) {
                if (e.name != 'customer_cix_contact_phone_ramal') e.setAttribute('required','');
            } );
        }
        else if (!element.checked) {
            formContactCix.setAttribute('hidden', '') // esconde form cix
            inputs.forEach( function xyz(e) {
                if (e.name != 'customer_cix_contact_phone_ramal') e.removeAttribute('required','');
            } );
        }
    }
}