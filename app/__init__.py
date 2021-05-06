from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

