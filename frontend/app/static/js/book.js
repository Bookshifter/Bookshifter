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
    const isbn = document.getElementById('isbn-new-book').value;
    const fatecId = parseInt(document.getElementById('fatec-new-book').value);
    const bookState = document.getElementById('book-state').value;
    if (!isbn) {
        alert('Insira o ISBN do livro.');
        return false;
    } else if (isbn.toString().length != 13 && isbn.toString().length != 10) {
        alert('O ISBN deve ser válido, com 10 ou 13 dígitos.');
        return false;
    } else if (!fatecId) {
        alert('Selecioe uma Fatec.')
        return false;
    }

    const apiUrl = `${params['url']}books/?isbn=${isbn}&fatecId=${fatecId}`;
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                bookState: bookState
            })
        });
        if (response.ok) {
            const data = await response.text();
            console.log(data);
            alert('Livro adicionado com sucesso!');
            window.location.reload();
        } else {
            throw new Error('Erro na solicitação do servidor.');
        }
    } catch (error) {
        console.error(error);
        alert('Ops, houve um erro com a solicitação, tente novamente mais tarde!');
    }
}
