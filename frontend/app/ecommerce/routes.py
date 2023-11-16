from flask import render_template, session, request
from app.ecommerce import bp
from flask import current_app
from app.authentication import functions as auth
from app.books import api as books_api
import ast, random

@bp.route('/')
def index():
  backend_url = current_app.config.get('BACKEND_API_URL')
  books_url = backend_url + 'books/all'
  params = {
   'method': 'GET',
   'url': books_url,
  }
  response = books_api.api_books(params)
  our_library = ast.literal_eval(response)
  if len(our_library) >= 3:
        random_books = random.sample(our_library, 3)
  return render_template('/ecommerce/index.html', page="index", our_library=random_books)

@bp.route('/about')
def about():
  return render_template('/ecommerce/about.html', page="about")

@bp.route('/cart')
def cart():
  return render_template('/ecommerce/cart.html')

@bp.route('/checkout')
def checkout():
  return render_template('/ecommerce/checkout.html')

@bp.route('/contact')
def contact():
  return render_template('/ecommerce/contact.html', page="contact")

@bp.route('/summary')
def summary():
  return render_template('/ecommerce/summary.html', page="summary")

@bp.route('/shop')
def shop():
  return render_template('/ecommerce/shop.html', page="shop")

@bp.route('/search')
def search():
  query = request.args.get('query')
  backend_url = current_app.config.get('BACKEND_API_URL')
  search_url = backend_url + 'books/search?query=' + query
  params = {
    'method': 'GET',
    'url': search_url,
    'token': session['token'] if 'token' in session else None
  }
  response = books_api.api_books(params)
  if type(response) != dict:
    response = ast.literal_eval(response)
    
  return render_template('/ecommerce/search.html', page="shop", books=response)

@bp.route('/single-news')
def single_news():
  return render_template('/ecommerce/single-news.html')

@bp.route('/book/<book_id>')
def book(book_id):
  backend_url = current_app.config.get('BACKEND_API_URL')
  book_url = backend_url + f'books/{book_id}' 
  params = {
    'method': 'GET',
    'url': book_url,
    'token': session['token'] if 'token' in session else None
  }
  response = books_api.api_books(params)
  if type(response) != dict:
    response = eval(response)    
  return render_template('/ecommerce/product.html', book=response)

@bp.route('/error-page')
def error_page():
  return render_template('/ecommerce/error-page.html')