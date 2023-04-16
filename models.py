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
    courses = db.relationship('Courses', backref='user_login', lazy=True)
    
    def set_password(self, password):
        ''' Para hashear la contraseña del usuario '''
        self.password = generate_password_hash(password)
    
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

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(256), nullable=False)
    user_login_id = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=False)
    
    def save(self):
        ''' Para guardar o actualizar un curso '''
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        ''' Para eliminar un curso '''
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Courses.query.all()
    
    @staticmethod
    def get_by_id(id):
        ''' Consulta curso por id '''
        return Courses.query.get(id)