from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'signin'
    
    # Blueprints
    from app.admin import admin_bp
    from app.auth import auth_bp
    
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    
    return app