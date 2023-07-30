from flask import render_template
from taskmanager import app, db
from taskmanager.models import Recipe

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recipes")
def recipes():
    return render_template("recipes.html")