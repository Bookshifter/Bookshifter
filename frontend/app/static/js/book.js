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

async function addBook(params) {
    const isbn = parseInt(document.getElementById('isbn-new-book').value);
    if (!isbn) {
        alert('Insira o ISBN do livro');
        return false;
    }
    const apiUrl = `${params['url']}books/isbn:${isbn}`;
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            const data = await response.text();
            console.log(data);
            alert('Livro adicionado com sucesso!');
            window.location.reload();
        } else {
            throw new Error('Erro na solicitação do servidor');
        }
    } catch (error) {
        console.error(error);
        alert('Ops, houve um erro com a solicitação, tente novamente mais tarde!');
    }
}
