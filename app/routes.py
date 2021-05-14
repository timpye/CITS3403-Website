from app import app
from flask import Flask, render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.forms import RegistrationForm
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from flask import request
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

class Question:
    q_id = -1
    question= ""
    op1= ""
    op2= ""
    op3= ""
    op4= ""
    correctop = -1

    def __init__(self, q_id, question, op1, op2, op3, op4, correctop):
        self.q_id = q_id
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.correctop = correctop

    def get_correctop(self):
        if self.correctop == 1:
            return self.op1
        elif self.correctop == 2:
            return self.op2
        elif self.correctop == 3:
            return self.op3
        elif self.correctop == 4:
            return self.op4
    
q1 = Question(1, "Which one of these isn't part of a computer?", "CPU", "GPU", "Monitor", "RAM", 3)
q2 = Question(2, "What does GPU stand for?", "Graphics Processing Unit", "Good Power Unit", "Graphical Powering Unit", "General Processing Unit", 1)
q3 = Question(3, "What isn't a Power Supply Certification?", "Gold", "Bronze", "Copper", "Platinum", 3)
q4 = Question(4, "What does RAM stand for?", "Rise Against Machines", "Roast And Mash", "Restructed Acessability Module", "Random Access Memory", 4)
q5 = Question(5, "Which one of these isn't a peripheral to a PC?", "Keyboard", "Mouse", "Solid State Drive", "Printer", 3)

q_list = [q1, q2, q3, q4, q5]

@login_required
@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title = 'Quiz', q_list = q_list)

@login_required
@app.route("/submission", methods=['POST', 'GET'])
def submit():
    score = 0
    for question in q_list:
        qid = str(question.q_id)
        selected_option = request.form[qid]
        correctop = question.get_correctop()
        if selected_option == correctop:
            score = score + 1
        
    message = ""
    if score < 3:
        message = "You scored " + str(score) + " /10. Bad"
    elif score < 5: 
        message = "You scored " + str(score) + " /10. Not so bad"
    elif score < 9:
        message = "You scored " + str(score) + " /10. Great"
    else:
        message = "You scored "+ str(score) + " /10. Amazing!"

    return render_template('submission.html', title = 'Submission', message = message)
        


@app.route('/stats')
def stats():
    return render_template('stats.html', title = 'Statistics')

@app.route('/content')
def content():
    return render_template('content.html', title = 'Content')

@app.route('/graphics_card')
def graphics_card():
    return render_template('graphics_card.html', title='Graphics Card')

@app.route('/ram')
def ram():
    return render_template('ram.html', title='RAM')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html', title = 'Feedback')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))




