#!/usr/bin/python3
"""this will create the flask app to
do the web aplication for Airbnb clone"""

from flask import Flask
from flask.templating import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returs a string to see if it works"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbhb():
    """returns a string displaying HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """usign a varible in teh url"""
    value = text.replace("_", " ")
    return "C {}".format(escape(value))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def is_python(text="is_cool"):
    """put python as a cool string"""
    value = text.replace("_", " ")
    return "Python {}".format(escape(value))


@app.route("/number/<int:n>", strict_slashes=False)
def integer(n):
    """defines if it is a integer"""
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """render the first template html"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """indetificates if a number is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
