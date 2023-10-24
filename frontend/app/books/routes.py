from flask import render_template, make_response, session, url_for, flash, redirect
from app.books import bp, api
from flask import current_app
from app.authentication import functions as auth


@bp.route('/shelf/books', methods=['GET', 'POST'])
def books():
    session_active = auth.verify_session(session)
    if not session_active:
        return redirect(url_for('authentication.login'))
    backend_url = current_app.config.get('BACKEND_API_URL')
    books = api.get_api_books(f'{backend_url}books/all')
    # Resgatar fatecs via API
    fatecs = [
        {
            'id': 1,
            'name': 'Fatec Diadema'
        },
        {
            'id': 2,
            'name': 'Fatec Zona Leste'
        },{
            'id': 3,
            'name': 'Fatec Praia Grande'
        },{
            'id': 4,
            'name': 'Fatec Zona Sul'
        },{
            'id': 5,
            'name': 'Fatec Ferraz de Vasconcelos'
        }
    ]
    response = make_response(render_template('/books/books.html', backend_url=backend_url, books=books, fatecs=fatecs))
    response.headers['Authorization'] = f"Bearer {session['token']}"
    return response