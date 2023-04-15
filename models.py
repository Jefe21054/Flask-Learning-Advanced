from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

class User(db.Model, UserMixin):
    ''' Clase Usuario que hereda de User Mixin para
    tener auth de usuarios de manera fácil'''
    __tablename__ = "user_login"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    def verify_password(self,password):
        ''' Para verificar la contraseña del usuario '''
        return check_password_hash(self.password,password)
    
    def save(self):
        ''' Para guardar un nuevo usuario '''
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_email(email):
        ''' Consulta usuario por email '''
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_by_id(user_id):
        ''' Consulta usuario por id '''
        return User.query.get(user_id)