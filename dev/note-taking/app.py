import os 
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

loginm = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"noter.db")
db = SQLAlchemy(app)

loginm.init_app(app)
loginm.session_protection="strong"
loginm.login_view = "login"




@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


class User (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Note (db.Model):

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	content = db.Column(db.Text)
	last_modified = db.Column(db.Date)





if __name__ == "__main__":
	app.run(debug = True)