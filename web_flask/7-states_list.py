#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route("/")
def index():
    """/: display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


@app.route("/c/<string:text>")
def ctext(text):
    """/c/<text>: display 'C ' followed by the value of the text variable
    (replaceing '_' with a space)"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<string:text>")
def pythontext(text="is cool"):
    """/python/<text>: display “Python ”, followed by the value of
    the text variable (replaceing '_' with a space)
    Default value: “is cool”"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:num>")
def number(num):
    """/number/<n>: display a number only if n is an integer"""
    return f"{num} is a number"


@app.route("/number_template/<int:num>")
def number_template(num):
    """/number_template/<n>: display a HTML page only if n is an integer"""
    return render_template("5-number.html", value=num)


@app.route("/number_odd_or_even/<int:num>")
def odd_or_even(num):
    """/number_odd_or_even/<n>: display a HTML page only if n is an integer"""
    if num & 1:
        data = f"{num} is odd"
    else:
        data = f"{num} is even"
    return render_template("6-number_odd_or_even.html", value=data)


@app.route("/states_list")
def states_list():
    """/states_list: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
