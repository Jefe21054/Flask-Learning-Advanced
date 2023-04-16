from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from forms import AddCourseForm
from models import Courses

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
        professor = request.form['professor']
        title = request.form['title']
        description = request.form['description']
        url = request.form['url']
        course = Courses(professor=professor, title=title, description=description, url=url, user_login_id=current_user.id)
        course.save()
        return redirect(url_for("dashboard"))
    return render_template("add_course.html", form=form)

@app.route("/dashboard/courses")
@login_required
def courses():
    courses = Courses.get_all()
    return render_template("courses.html", courses=courses)

@app.route("/dashboard/course/delete/<id>")
@login_required
def delete_course(id=None):
    course = Courses.get_by_id(id)
    course.delete()
    return redirect(url_for('courses'))

@app.route("/dashboard/course/update/<id>", methods=["GET", "POST"])
@login_required
def update_course(id=None):
    course = Courses.get_by_id(id)
    form = AddCourseForm(obj=course)
    if form.validate_on_submit():
        course.professor = request.form['professor']
        course.title = request.form['title']
        course.description = request.form['description']
        course.url = request.form['url']
        course.save()
        return redirect(url_for('courses'))
    return render_template('add_course.html', form=form)