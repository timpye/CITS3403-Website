from app import app
from flask import Flask, render_template, flash, redirect, url_for, session, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.forms import RegistrationForm
from flask_login import logout_user
from flask_login import login_required
from app.models import User, Result
from werkzeug.urls import url_parse
from sqlalchemy import func, extract
from datetime import datetime




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
    
q1 = Question(1, "(1). Which one of these isn't part of a computer?", "a. CPU", "b. GPU", "c. Monitor", "d. RAM", 3)
q2 = Question(2, "(2). What does GPU stand for?", "a. Graphics Processing Unit", "b. Good Power Unit", "c. Graphical Powering Unit", "d. General Processing Unit", 1)
q3 = Question(3, "(3). What isn't a Power Supply Certification?", "a. Gold", "b. Bronze", "c. Copper", "d. Platinum", 3)
q4 = Question(4, "(4). What does RAM stand for?", "a. Rise Against Machines", "b. Roast And Mash", "c. Restructed Acessability Module", "d. Random Access Memory", 4)
q5 = Question(5, "(5). Which of these is the fastest type of SSD", "a. SATA", "b. SSHD", "c. NVMe", "d. Printer", 3)
q6 = Question(6, "(6). What do you need to apply to a CPU before putting it on?", "a. Tooth Paste", "b. Compound Paste", "c. Thermal Paste", "d. Nothing", 3)
q7 = Question(7, "(7). What do you call the slots that you put the RAM into?", "a. DAMM slots", "b. DIMM slots", "c. JIMM slots", "d. DDMM slots", 2)

q_list = [q1, q2, q3, q4, q5, q6, q7]


class Question2:
    q_id = -1
    question= ""
    op1= ""
    op2= ""
    op3= ""
    op4= ""
    op5= ""
    correctop1 = -1
    correctop2 = -1
    correctop3 = -1

    def __init__(self, q_id, question, op1, op2, op3, op4, op5, correctop1, correctop2, correctop3):
        self.q_id = q_id
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.op5 = op5
        self.correctop1 = correctop1
        self.correctop2 = correctop2
        self.correctop3 = correctop3

    def get_correctop1(self):
        if self.correctop1 == 1:
            return self.op1
        elif self.correctop1 == 2:
            return self.op2
        elif self.correctop1 == 3:
            return self.op3
        elif self.correctop1 == 4:
            return self.op4
        elif self.correctop1 == 5:
            return self.op5
        
    def get_correctop2(self):
        if self.correctop2 == 1:
            return self.op1
        elif self.correctop2 == 2:
            return self.op2
        elif self.correctop2 == 3:
            return self.op3
        elif self.correctop2 == 4:
            return self.op4
        elif self.correctop2 == 5:
            return self.op5

    def get_correctop3(self):   
        if self.correctop3 == 1:
            return self.op1
        elif self.correctop3 == 2:
            return self.op2
        elif self.correctop3 == 3:
            return self.op3
        elif self.correctop3 == 4:
            return self.op4
        elif self.correctop3 == 5:
            return self.op5

q8 = Question2(8, "(8). Check all the peripherals used with a PC.", "a. Keyboard", "b. Mouse", "c. Solid State Drive", "d. Printer", "e. Memory", 1, 2, 4)
q9 = Question2(9, "(9). Check all the applications of a GPU.", "a. Crypto Mining", "b. Shiny Graphics", "c. Deep Learning", "d. Store Files", "e. Running the OS", 1, 2, 3)
q10 = Question2(10, "(10). Check all the important considerations in terms of performance when picking components for a PC.", "a. Processor Speed", "b. RGB lighting", "c. Video Memory", "d. RAM Speed", "e. Storage Capacity", 1, 3, 4)

q2_list = [q8, q9, q10]


@login_required
@app.route('/quiz')
def quiz():
    return render_template('quiz.html', title = 'Quiz', q_list = q_list, q2_list = q2_list)

@login_required
@app.route("/submission", methods=['POST', 'GET'])
def submit():
    score = 0
    question_number = 0
    question_list = [False,False,False,False,False,False,False,False,False,False]
    for question in q_list:

        qid = str(question.q_id)
        selected_option = request.form[qid]
        correctop = question.get_correctop()
        if selected_option == correctop:
            question_list[question_number] = True
            score = score + 1
        else:
            question_list[question_number] = False
        question_number += 1

    for question in q2_list:
        qid = str(question.q_id)
        selected_option = request.form[qid]
        correctop1 = question.get_correctop1()
        correctop2 = question.get_correctop2()
        correctop3 = question.get_correctop3()
        if selected_option == correctop1:
            score = score + 1
            question_list[question_number] = True
        elif selected_option == correctop2:
            score = score + 2
            question_list[question_number] = True
        elif selected_option == correctop3:
            score = score + 3
            question_list[question_number] = True
        question_number += 1
    
    #print(question_list)
    result = Result(user_id=current_user.get_id(),date_created=datetime.today())
    result.add_results(question_list, score)
    db.session.add(result)
    db.session.commit()

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
    user_results = []
    for result in db.session.query(Result.num_correct).join(User).filter(User.id==(current_user.get_id())):
        user_results.append(result[0])
    
    every_result = []
    for result, name in db.session.query(Result.num_correct, User.username).filter(User.id==Result.user_id).all():
        every_result.append((result, name))
    
    average_mark = '{:.2f}'.format(db.session.query(func.avg(Result.num_correct).label("average"))[0][0]) #indexs to get at a tuple inside a list

    today = (datetime.today().year, datetime.today().month, datetime.today().day)
    
    
    quizzes_today = db.session.query(Result.date_created).filter(
        extract('month', Result.date_created) == datetime.today().month,
        extract('year', Result.date_created) == datetime.today().year).count()

    score_today = db.session.query(func.avg(Result.num_correct)).filter(
        extract('month', Result.date_created) == datetime.today().month,
        extract('year', Result.date_created) == datetime.today().year,
        extract('day', Result.date_created) == datetime.today().day).count()
        
    total_users = db.session.query(User).count()
    print("Total Users: ", total_users)
    print("Quizzes taken today: ",quizzes_today)
    print("Average:",average_mark)
    return render_template('stats.html', title = 'Statistics', user_results = user_results,
    every_result = every_result, average_mark = average_mark, total_users = total_users, 
    quizzes_today = quizzes_today, score_today = score_today)

@app.route('/content')
def content():
    return render_template('content.html', title = 'Content')

@app.route('/cpu')
def cpu():
    return render_template('cpu.html', title='CPU (Central Processing Unit')

@app.route('/motherboard')
def motherboard():
    return render_template('motherboard.html', title='Motherboard')

@app.route('/gpu')
def gpu():
    return render_template('gpu.html', title='GPU (Graphical Processing Unit)')

@app.route('/ram')
def ram():
    return render_template('ram.html', title='RAM')

@app.route('/feedback')
def feedback():
    q1_data = []
    q2_data = []
    answers = []
    i = 3

    for column in Result.__table__.columns:
        answers.append(db.session.query(column).filter(current_user.get_id()==Result.user_id).first())
    #print(answers)

    for q in q_list:
        q1_data.append((q.q_id, q.question, q.get_correctop(), answers[i][0]))
        i+=1      
    #print(q_data)

    for q in q2_list:
        q2_data.append((q.q_id, q.question, (q.get_correctop1(), q.get_correctop2(), q.get_correctop3()), answers[i]))
        i += 1
    print(q1_data,q2_data)
    return render_template('feedback.html', title = 'Feedback', q1_data = q1_data, q2_data = q2_data)

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




