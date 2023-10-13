from flask import render_template
from app.books import bp
from flask import current_app

@bp.route('/books')
def books():
    return render_template('/books/books.html')