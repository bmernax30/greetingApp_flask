from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'another_very_secret_and_unique_key'

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")
    request.form['name_input']
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)