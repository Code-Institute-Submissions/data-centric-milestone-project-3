import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('my_data_project')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)

username = mongo.db.users.find()

@app.route("/")
@app.route("/index")
def home():
    if 'username' in session:
        return "You are logged in as " + session['username']
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('user_management.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users=mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

    if existing_user == None:
        hashpash = bcrypt.hashpw(request.form[''])

    return ''


@app.route('/readrecipe')
def get_recipe():
    return render_template('readrecipe.html', 
    recipes=mongo.db.recipes.find())
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)