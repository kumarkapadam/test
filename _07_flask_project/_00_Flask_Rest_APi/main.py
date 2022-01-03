from flask import Flask,render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('templates/index.html')


@app.route("/login")
def login():
    return render_template('templates/login.html')


@app.route("/signup")
def signup():
    return render_template('templates/signup.html')

if __name__ == "__main__":
    app.run(debug=True)