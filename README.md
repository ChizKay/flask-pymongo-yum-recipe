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

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X


