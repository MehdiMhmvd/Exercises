from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") ## geting from address bar
def index():
	return render_template("index.html")

@app.route("/user/<name>") ## geting from address bar
def user(name):
	return render_template("user.html", username=name)

@app.route("/result")
def result():
	return render_template("result.html")

@app.route("/book")
def book():
	return render_template("book.html")

@app.route("/teacher")
def teacher():
	return render_template("pictureelement.html")

if __name__ == "__main__":
	app.run(debug = True)