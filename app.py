from flask import Flask, render_template, request, redirect, url_for
from models import User, db_user, get_user 
from forms import LoginForm, SignupForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"


@app.route("/")
def index():
    return redirect(url_for('signin'))

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignupForm()
    if form.validate_on_submit() and request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        db_user.append(user)
        print(db_user)
        return redirect(url_for("signin"))
    return render_template("signup.html", form=form)


@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = get_user(email)
        print(user)
        # return render_template("signin.html")
    return render_template("signin.html", form=form)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
