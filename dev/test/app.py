from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") ## geting from address bar
def index():
	return render_template("index.html")

@app.route("/user/<name>") ## geting from address bar
def user(name):
	return render_template("user.html", username=name)


if __name__ == "__main__":
	app.run(debug = True)