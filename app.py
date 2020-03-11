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
    return render_template("recipes.html")
    

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", cuisines=mongo.db.cuisines.find())
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe'))    

@app.route('/update_cuisine', methods=["POST"])
def update_cuisine():
    cuisines = mongo.db.cuisines
    cuisines.update(
    {
        'cuisine_name':request.form.get('cuisine_name')
    })
    return redirect(url_for('get_recipe'))   
    
@app.route('/update_french', methods=["POST"])
def update_french():
    french = mongo.db.french_cuisine
    french.update(
    {
        'dish_name':request.form.get('dish_name'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
    })
    return redirect(url_for('french_cuisine'))  
    
    
@app.route('/update_italian', methods=["POST"])
def update_italian():
    italian = mongo.db.italian_cuisine
    italian.update(
    {
        'dish_name':request.form.get('dish_name'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
    })
    return redirect(url_for('italian_cuisine'))


@app.route('/update_mexican', methods=["POST"])
def update_mexican():
    mexican = mongo.db.mexican_cuisine
    mexican.update(
    {
        'dish_name':request.form.get('dish_name'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
    })
    return redirect(url_for('mexican_cuisine'))   
    

@app.route('/update_other', methods=["POST"])
def update_other():
    other = mongo.db.other
    other.update(
    {
        'dish_name':request.form.get('dish_name'),
        'image':request.form.get('image'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions'),
    })
    return redirect(url_for('other_cuisine'))

    
    
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
    

@app.route('/my_recipe')
def my_recipe():
    return render_template("myrecipe.html", recipes=mongo.db.recipes.find())
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

