from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '842fead82ff117427acfd504'

#----------------------------Email authentication------------------------
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jeevanbabu190@gmail.com'
app.config['MAIL_PASSWORD'] = 'jeevanbabukannan'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False



#--------------------Email end---------------------------------

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "login_page"  #login_required decorator will send the user to the page that is given here
login_manager.login_message_category = 'info'

from market import route


with app.app_context():
    db.create_all()


