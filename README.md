# MY COOK-BOOK WEBSITE

This website is a simple recipe site that displays 4 types of cuisines (with one being a generalised one), on seperate pages. It allows users to add their own recipes, edit and delete them. Created recipes are displayed on a seperate page for easy access.
## UX
 
This site was created in the most simplistic manner, in order for the user to navigate through it with ease. This website is ideal for users that want all the information they need about a recipe on a singular page, rather than the site taking the user to a seperate page to view more information about a particular recipe.
 


In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

##### Navigation Bar
- Materialize navbar was used here, links to all sections of the website on the right. Responsive, has a hamburger menu on smaller devices.
 
 ##### Cuisine links
 - Materialize cards were using. Have an image displaying the recipe, expands on click, alternatively can using the materialize icon (arrow pointing down). Shows Recipe name(dish name), ingredients (tags), and preparation instructions. Can click icon on top right to expand, reverts to the initial image display. A handy figure that allows the user to stay on the page without going back and forth on tabs to view other recipes from the same Cuisine.
 
 ###### Create Recipe
 - Materialize form used. Data for Cuisine type, Dish name, Image link (Url link to the image should be pasted in the input text), Instructions is sent to the database. The result is displayed on the "My Recipe" page.
 
 ###### My Recipe
 - Same layout as the Cuisine Links. The stand out feature is the ability to add tags in the ingredients sections.
 

### Features Left to Implement
- Chip data from the ingredients tags to be saved after reload. Still looking for ways to achieve this.

## Technologies Used

###### HTML5
###### CSS
###### [Materialize 0.100.2](http://archives.materializecss.com/0.100.2/)
- For easy layout and styling. Icons used in the project are from the materialize icons library.
###### [JQuery 3.2.1](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js)
- The project uses **JQuery** to simplify DOM manipulation.
###### Python
- This Project uses Flask as a framework. Using jinja templates, to reduce the amount of HTML code.

## Testing

The project has been tested on the following devices:
  - OnePlus 3t
  - OnePlus 6t
  - Huawei P smart
  - Xiaomi Redmi 8
  - Samsung S9
  - Iphone 6s
  - Iphone X
  - HP i3
  - HP i5
  - Apple MacBook air (2018)
  
Testing on the above devices was almost flawless. All buttons and form fields were responsive and fully functional. The Form on the #Create Recipe# page works as intended, data is stored in mongo.db atlas and redirected to the #My Recipe# page. The submitted recipe displays as intended. When the expand icon(on the right top corner of the recipe image) is clicked, the Dish name, Ingredients and Instructions are displayed. The User can then enter individual ingredients in the form field provided. Data is dispalyed in chips, which unfortunately is not sent to the database. So the data is lost when page is refreshed. Still looking for ways to fix this issue. Nonetheless, this seemed a neat way to enter the ingredients.
The Edit and Delete buttons work as intended. On hover the delete button displays a tooltip warning the user that the action is irreversible.

Overall the site is quite responsive on both small and large devices. Materialize makes the transition quite smooth. 
 
## Deployment

This site is deployed on Heroku.
The following code was used to achieve this:
```
heroku login
git init
git add .
git commit -m 'first commit message'
heroku git:remote -a flask-pymongo-yum-recipe
git push heroku master
```

Use Git to clone flask-pymongo-yum-recipe's source code to your local machine.
```
heroku git:clone -a flask-pymongo-yum-recipe
cd flask-pymongo-yum-recipe
```

## Credits

### Content
- All the recipe ingredients and instructions were copied from [Bon Appetit](https://www.bonappetit.com/recipes).

### Media
- The Background image on the site was taken from a background images [Google](https://www.google.com/) search.
- All other images and recipes were copied from [Bon Appetit](https://www.bonappetit.com/recipes).

### Acknowledgements

- I received inspiration for this project from the code institute>task-manager>mini project. used the code from that particular project as a guide. 


