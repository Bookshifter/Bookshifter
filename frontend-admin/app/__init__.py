from flask import Flask, session
from flask_session import Session
from flask_jwt_extended import JWTManager
from config import Config

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    jwt.init_app(app)
    
    app.config['JWT_TOKEN_LOCATION'] = ['cookies'] # nova linha
    
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
    
    from app.index import bp as main_bp
    app.register_blueprint(main_bp)
    
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
    
    return app