from flask import Flask, session
from flask_session import Session
from config import Config
from datetime import timedelta

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SESSION_PERMANENT'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] = 300 # 5 minutes
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)

    from app.account import bp as account_bp
    app.register_blueprint(account_bp)
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)
    
    from app.charts import bp as charts_bp
    app.register_blueprint(charts_bp)
    
    from app.contacts import bp as contacts_bp
    app.register_blueprint(contacts_bp)
    
    from app.forms import bp as forms_bp
    app.register_blueprint(forms_bp)
    
    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)
    
    from app.pages import bp as pages_bp
    app.register_blueprint(pages_bp)
    
    from app.tables import bp as tables_bp
    app.register_blueprint(tables_bp)
    
    from app.ui import bp as ui_bp
    app.register_blueprint(ui_bp)

    from app.authentication import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.books import bp as books_bp
    app.register_blueprint(books_bp)
    
    from app.ecommerce import bp as ecommerce_bp
    app.register_blueprint(ecommerce_bp)
    
    return app