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
    response = make_response(render_template('/books/books.html', backend_url=backend_url, books=books))
    response.headers['Authorization'] = f"Bearer {session['token']}"
    return response