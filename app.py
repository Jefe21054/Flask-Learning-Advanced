from flask import Flask, render_template, request, redirect, url_for

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
        return redirect(url_for("signin"))
    return render_template("signup.html", form=form)


@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        return render_template("signin.html")
    return render_template("signin.html", form=form)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
