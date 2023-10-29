from flask import render_template, redirect, url_for, session, flash
from app.ecommerce import bp
from flask import current_app
from app.authentication import functions as auth

@bp.route('/')
def index():
  print(session)
  return render_template('/ecommerce/index.html')

@bp.route('/about')
def about():
  return render_template('/ecommerce/about.html')

@bp.route('/cart')
def cart():
  return render_template('/ecommerce/cart.html')

@bp.route('/checkout')
def checkout():
  return render_template('/ecommerce/checkout.html')

@bp.route('/contact')
def contact():
  return render_template('/ecommerce/contact.html')

@bp.route('/summary')
def summary():
  return render_template('/ecommerce/summary.html')

@bp.route('/shop')
def shop():
  return render_template('/ecommerce/shop.html')

@bp.route('/single-news')
def single_news():
  return render_template('/ecommerce/single-news.html')

@bp.route('/single-product')
def single_product():
  return render_template('/ecommerce/single-product.html')

@bp.route('/error-page')
def error_page():
  return render_template('/ecommerce/error-page.html')