function deleteCustomerphone(params) {
    var conf = confirm('Tem certeza que quer apagar?')
    console.log(conf)
    return
    apiUrl = params['url'] + ''
    fetch(apiUrl, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(id)
    })
    .then(response => {
        console.log(response.json());
        alert('Telefone adicionado com sucesso!');
        window.location.reload();
    })
    .catch(error => {
        console.error('Erro ao enviar a solicitação POST:', error);
    });
}