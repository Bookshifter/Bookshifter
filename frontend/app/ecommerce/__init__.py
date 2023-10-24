from flask import Blueprint

bp = Blueprint('ecommerce', __name__)

from app.ecommerce import routes