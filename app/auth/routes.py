from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, SignupForm
from app.models import User

from . import auth_bp
from app import login_manager

@auth_bp.route("/")
def index():
    return redirect(url_for('auth.signin'))

@auth_bp.route("/signup", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = SignupForm()
    if form.validate_on_submit() and request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname=firstname, lastname=lastname, email=email)
        user.set_password(password)
        user.save()
        return redirect(url_for("auth.signin"))
    return render_template("auth/signup.html", form=form)

@auth_bp.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.get_by_email(email)
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
    return render_template("auth/signin.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))

# Cargar usuarios
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))