function postCustomerphone(params) {
    var data = {}
    
    if (params['form'] == 'yes-inoc') {
        data = {
            "phone_ddd": "",
            "phone_number": document.getElementsByName('collapse_noc_inoc')[0]['value'] ,
            "phone_ramal": "",
            "phone_cc": "",
            "phone_noc": true,
            "customer_contact": params['id']
        }
    } else {
        data = {
            "phone_ddd": document.getElementsByName(`collapse_${params['form']}_ddd`)[0]['value'],
            "phone_number": document.getElementsByName(`collapse_${params['form']}_phone`)[0]['value'],
            "phone_ramal": document.getElementsByName(`collapse_${params['form']}_ramal`)[0]['value'],
            "phone_cc": document.getElementsByName(`collapse_${params['form']}_cc`)[0]['value'],
            "phone_noc": false,
            "customer_contact": params['id']
        }
    }

    if (params['url'].includes('host.docker.internal')) {
        params['url'] = params['url'].replace("host.docker.internal", "localhost")
    }
    var apiUrl = params['url'] + "customerphone-edit/"
    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        alert('Telefone adicionado com sucesso!');
        window.location.reload();
    })
    .catch(error => {
        alert('Erro ao enviar a solicitação POST: ', error);
    });
}

function deleteCustomerphone(params) {
    if (params['url'].includes('host.docker.internal')) {
        params['url'] = params['url'].replace("host.docker.internal", "localhost")
    }
    var conf = confirm('Tem certeza que quer apagar este telefone?');
    if (!conf) return

    apiUrl = params['url'] + `customerphone-edit/${params['id']}`
    fetch(apiUrl, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        alert('Telefone removido com sucesso!');
        window.location.reload();
    })
    .catch(error => {
        alert('Erro ao enviar a solicitação POST: ', error);
    });
}