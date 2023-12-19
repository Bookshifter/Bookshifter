from flask import render_template, make_response, session, url_for, flash, redirect, request
from app.books import bp, api
from flask import current_app
from app.authentication import functions as auth


@bp.route('/shelf/books', methods=['GET', 'POST'])
def books():
    session_active = auth.verify_session(session)
    if not session_active:
        return redirect(url_for('authentication.login'))
    print(session['token'])
    backend_url = current_app.config.get('BACKEND_API_URL')
    key_google = current_app.config.get('KEY_API_GOOGLE')
    if request.method == 'POST':
        form = dict(request.form)
        if 'add-book' in request.form:
            url = backend_url + f"books/?isbn={form['isbn']}&fatecId={form['fatec']}"
            params = {
                'data': {
                    'bookState': form['state']
                    }, 
                'token' : session['token'],
                'method': 'POST',
                'url': url
            }
            response = api.api_books(params)
            if 'error' in response:
                print(response)
                flash(response['error'], 'danger')
                return redirect(url_for('books.books'))
            else:
                flash('Livro cadastrado com sucesso!', 'success')
                return redirect(url_for('books.books'))
        elif 'delete-book' in request.form:
            url = backend_url + f"books/{form['book_id']}"
            params = {
                'token' : session['token'],
                'method': 'DELETE',
                'url': url
            }
            response = api.api_books(params)
            if 'error' in response:
                flash(response['error'], 'danger')
                return redirect(url_for('books.books'))
            else:
                flash('Livro apagado com sucesso!', 'success')
                return redirect(url_for('books.books'))
        
    user_data = api.get_api_books({"url":f"{backend_url}users/books?email={session['username']}", "token": session['token']})
    fatecs = api.get_api_books({'url':f'{backend_url}fatecs', 'token': session['token']})
    response = make_response(render_template('/books/books.html', backend_url=backend_url, user_data=user_data, fatecs=fatecs, key_google=key_google))
    return response