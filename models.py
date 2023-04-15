from flask_login import UserMixin

db_user = []

class User(UserMixin):
    ''' Clase Usuario que hereda de User Mixin para
    tener auth de usuarios de manera fácil'''
    def __init__(self,id,firstname,lastname,email,password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def verify_password(self,password):
        ''' Para verificar la contraseña del usuario '''
        if self.password == password:
            return True
        else:
            return False
        
def get_user(email):
    for user in db_user:
        if user.email == email:
            return user
        else:
            return None