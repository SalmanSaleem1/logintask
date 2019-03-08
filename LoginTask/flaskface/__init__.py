from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flaskface.config import BaseConfig


app = Flask(__name__, template_folder='template')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)


login = LoginManager(app)
login.login_view = 'user.login'
login.login_message_category = 'info'


from flaskface.user.Routes import user
from flaskface.post.Routes import post
from flaskface.main.Routes import main
from flaskface.error.CustomeError import errors

app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(main)
app.register_blueprint(errors)

