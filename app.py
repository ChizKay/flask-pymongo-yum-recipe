import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'my_recipe'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipes=mongo.db.recipes.find(), cuisines=mongo.db.cuisines.find())
    

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", cuisines=mongo.db.cuisines.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))    
    
    
@app.route('/french_cuisine')
def french_cuisine():
    return render_template("french.html", french=mongo.db.french_cuisine.find())
    
    
@app.route('/italian_cuisine')
def italian_cuisine():
    return render_template("italian.html", italian=mongo.db.italian_cuisine.find())
    
    
@app.route('/mexican_cuisine')
def mexican_cuisine():
    return render_template("mexican.html", mexican=mongo.db.mexican_cuisine.find())
    
    
@app.route('/other_cuisine')
def other_cuisine():
    return render_template("other.html", other=mongo.db.other.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

