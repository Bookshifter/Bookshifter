from flask import render_template, make_response, session, url_for
from app.books import bp, api
from flask import current_app
from flask_jwt_extended import jwt_required, get_jwt_identity


@bp.route('/books', methods=['GET', 'POST'])
def books():
    if not session['token']:
        return url_for('authentication.login')
    backend_url = current_app.config.get('BACKEND_API_URL')
    books = api.get_api_books(f'{backend_url}books/all')
    response = make_response(render_template('/books/books.html', backend_url=backend_url, books=books))
    return response