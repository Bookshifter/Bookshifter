from flask import render_template, request, redirect, url_for
from app.index import bp
from flask import current_app   

@bp.route('/')
def index():
  return render_template('/index/index.html')