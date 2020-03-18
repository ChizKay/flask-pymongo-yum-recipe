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

# READ FUCTIONS
@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html")
    
    
@app.route('/my_recipe')
def my_recipe():
    return render_template("myrecipe.html",
                            recipes=mongo.db.recipes.find())    
    

@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", 
                            cuisines=mongo.db.cuisines.find())
                            
                            
@app.route('/italian_cuisine')
def italian_cuisine():
    return render_template("italian.html", italian=mongo.db.italian_cuisine.find())
    
    
@app.route('/mexican_cuisine')
def mexican_cuisine():
    return render_template("mexican.html", mexican=mongo.db.mexican_cuisine.find())
    
    
@app.route('/other_cuisine')
def other_cuisine():
    return render_template("other.html", other=mongo.db.other.find())
    
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('my_recipe'))    
    
# EDIT FUNCTION    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_cuisines = mongo.db.cuisines.find()
    return render_template('editrecipe.html', 
                            recipe=the_recipe, 
                            cuisine=all_cuisines)      

# UPDATE FUNCTION

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'cuisine_name':request.form.get('cuisine_name'),
        'dish_name':request.form.get('dish_name'),
        'image':request.form.get('image'),
        'instructions':request.form.get('instructions')
    })
    return redirect(url_for('my_recipe'))  
    
# DELETE FUNCTION

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('my_recipe'))

    
@app.route('/french_cuisine')
def french_cuisine():
    return render_template("french.html", french=mongo.db.french_cuisine.find())
    
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

