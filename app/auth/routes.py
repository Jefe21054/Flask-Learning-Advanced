from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms import LoginForm, SignupForm
from models import User

@app.route("/")
def index():
    return redirect(url_for('signin'))

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = SignupForm()
    if form.validate_on_submit() and request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname=firstname, lastname=lastname, email=email)
        user.set_password(password)
        user.save()
        return redirect(url_for("signin"))
    return render_template("signup.html", form=form)

@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = User.get_by_email(email)
        if user is not None and user.verify_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template("signin.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('signin'))

# Cargar usuarios
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))