from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

class User(UserMixin):
    ''' Clase Usuario que hereda de User Mixin para
    tener auth de usuarios de manera fácil'''
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    def verify_password(self,password):
        ''' Para verificar la contraseña del usuario '''
        return check_password_hash(self.password,password)