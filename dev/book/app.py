from flask import Flask, render_template
from flask_bootstrap import Bootstrap

comments = ["home","menu"]

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/user/<name>')
def user(name):
	print(name)
	return render_template('user.html', name=name ,comments = comments)



if __name__ == "__main__":
	app.run(debug=True)