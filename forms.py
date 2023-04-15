from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Correo Electrónico:", validators=[DataRequired(message="Ingresa tu correo electrónico.")])
    password = PasswordField("Contraseña:", validators=[DataRequired(message="Ingresa tu contraseña.")])
    
class SignupForm(FlaskForm):
    firstname = StringField(render_kw={"placeholder": "Nombre" }, validators=[DataRequired(message="Ingresa tu nombre")])
    lastname = StringField(render_kw={"placeholder": "Apellido" }, validators=[DataRequired(message="Ingresa tu apellido")])
    email = EmailField(render_kw={"placeholder": "Correo Electrónico" }, validators=[DataRequired(message="Ingresa un email"), Email(message="Ingresa un email válido")])
    password = PasswordField(render_kw={"placeholder": "Contraseña" }, validators=[DataRequired(message="Ingresa tu contraseña")])

class AddCourseForm(FlaskForm):
    professor = StringField("Profesor:", validators=[DataRequired(message="Nombre del profesor")])
    title = StringField("Titulo:", validators=[DataRequired(message="Ingresa el título del curso")])
    description = TextAreaField("Descripción:", validators=[DataRequired(message="Ingresa la descripción")])
    link = StringField("Url del curso:", validators=[DataRequired(message="Ingresa la url del curso")])