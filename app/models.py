from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    day_joined = db.Column(db.DateTime())
    

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    num_correct = db.Column(db.Integer)
    first_correct = db.Column(db.Boolean)
    second_correct = db.Column(db.Boolean)
    third_correct = db.Column(db.Boolean)
    fourth_correct = db.Column(db.Boolean)
    fifth_correct = db.Column(db.Boolean)
    sixth_correct = db.Column(db.Boolean)
    seventh_correct = db.Column(db.Boolean)
    eigth_correct = db.Column(db.Boolean)
    ninth_correct = db.Column(db.Boolean)
    tenth_correct = db.Column(db.Boolean) 
    date_created = db.Column(db.DateTime())

    def __repr__(self):
        return '<{}>'.format(self.num_correct)

    def add_results(self, results_list, score):
        self.num_correct = score
        num = 0
        first_correct = results_list[num]
        num += 1
        second_correct = results_list[num]
        num += 1
        third_correct = results_list[num]
        num += 1
        fourth_correct = results_list[num]
        num += 1
        fifth_correct = results_list[num]
        num += 1
        sixth_correct = results_list[num]
        num += 1
        seventh_correct = results_list[num]
        num += 1
        eigth_correct = results_list[num]
        num += 1
        ninth_correct = results_list[num]
        num += 1
        tenth_correct = results_list[num]
        num += 1