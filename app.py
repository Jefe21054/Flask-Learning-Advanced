from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User, db_user, get_user
from forms import LoginForm, SignupForm, AddCourseForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

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
        user = User(id=len(db_user) + 1,firstname=firstname, lastname=lastname, email=email, password=password)
        db_user.append(user)
        return redirect(url_for("signin"))
    return render_template("signup.html", form=form)


@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = get_user(email)
        if user is not None and user.verify_password(password):
            print(user.password)
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template("signin.html", form=form)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/dashboard/user/account")
@login_required
def user_account():
    return render_template("user_account.html")

@app.route("/dashboard/courses/add", methods=["GET", "POST"])
@login_required
def add_courses():
    form = AddCourseForm()
    if form.validate_on_submit():
        return redirect(url_for("dashboard"))
    return render_template("add_course.html", form=form)

@app.route("/dashboard/courses")
@login_required
def courses():
    courses = [{"professor": "Kevin Guzmán", 
                "title": "Fundamentos de Flask",
                "description": "Es un curso donde aprenderemos conceptos básicos del desarrollo utilizando la excelente herramienta de FLASK",
                "url": "https://ed.team/cursos/flask"}, 
                {"professor": "Diego Adrian Barra Paredes", 
                "title": "Curso: React Hooks con TypeScript",
                "description": "A menudo cuando escribes componentes dentro de las clases, te encuentras que con el tiempo se vuelven complejos, difíciles de organizar, y la lógica de estado entre los componentes no la puedes reutilizar.",
                "url": "https://ed.team/cursos/react-hooks"}]
    return render_template("courses.html", courses=courses)

@app.route("/dashboard/course/delete/<id>")
@login_required
def delete_course(id=None):
    return f"Deleted Course with id {id}"

@app.route("/dashboard/course/update/<id>")
@login_required
def update_course(id=None):
    return f"Updated Course with id {id}"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('signin'))

# Cargar usuarios
@login_manager.user_loader
def load_user(user_id):
    for user in db_user:
        if user.id == int(user_id):
            return user
        else:
            return None
