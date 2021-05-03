from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))

    return render_template('login.html', title='Login', form=form)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title = 'Quiz')

@app.route('/stats')
def stats():
    return render_template('stats.html', title = 'Statistics')

@app.route('/content.html')
def content():
    return render_template('content.html', title = 'Content')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title = 'Feedback')

