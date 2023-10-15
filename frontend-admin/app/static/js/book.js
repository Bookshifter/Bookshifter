function deleteBook(params) {
    var conf = confirm('Tem certeza que quer apagar este livro?');
    if (!conf) return false
    apiUrl =  `${params['url']}books/${params['id']}`
    fetch(apiUrl, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        alert('Livro removido com sucesso!');
        window.location.reload();
    })
    .catch(error => {
        alert('Ops, houve um erro com a solicitação, tente novamente mais tarde!');
        console.error('Erro ao enviar a solicitação POST:', error);
    });
}