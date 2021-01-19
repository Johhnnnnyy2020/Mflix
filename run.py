import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Barbershop'
app.config["MONGO_URI"] = "mongodb+srv://Netflix:Netflix@cluster0.7n1lg.mongodb.net/sample_mflix?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_movies')
def get_movies():
    return render_template("index.html", movies=mongo.db.movies.find())


app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), 
        debug=False)