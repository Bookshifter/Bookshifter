from flask import Blueprint

bp = Blueprint('tables', __name__)


from app.tables import routes
