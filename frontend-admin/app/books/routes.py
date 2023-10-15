from flask import render_template
from app.books import bp, api
from flask import current_app

@bp.route('/books')
def books():
    backend_url = current_app.config.get('BACKEND_API_URL')
    books = api.get_api_books(f'{backend_url}books/all')
    return render_template('/books/books.html',
                           backend_url=backend_url,
                           books=books)