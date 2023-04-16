from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# app.config['SECRET_KEY'] = FLASK_SECRET
# 'postgresql://username:password@localhost:5432/edteamdb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/edteamdb'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
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