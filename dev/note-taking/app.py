import os 
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,"noter.db")
db = SQLAlchemy(app)




@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True)