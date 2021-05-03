from app import app
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

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

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')