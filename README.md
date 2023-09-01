# Cookbook Recipes 

---
## Description
Cookbook Recipes is a Back end web application that allows users to store and easily access cooking recipes. It contains recipe cards that include fields such asdescription of the recipe, ingredients, preparation steps, cooking time, and many more. A CRUD function is coded which means the user
can create, locate, display, edit, and delete records. The website has three pages. the homepage, which has a carousel slide of recipes, The recipe page where all recipes are stored and the new recipe page where the user can create any recipe they desire. Once the recipe is created, a recipe card is stored on the recipe page. 

---
## User Experience UX

### User's goal

 * The website's purpose is to allow the user to find share update and delete recipes. 


### Site owner's goal 

* Promote a brand of cooking tools.

---
## Design
   ### Colour Scheme
    * The background colour for the front end application is #8d6e63 (brown lighten-1)
    * Top navbar is #212121  (grey darken-4)
    * Footer is #757575 (grey darken-1)
---
## Features
  * Responsive on all device sizes 

  * Interactive elements
  ---
  ## Technologies Used 
  ### Languages Used
   * HTML5
   * CSS3
   * JavaScript
   * Python+Flask
   * PostgreSQL
---
## Frameworks
 * Materialize 1.0- Materialize is a modern responsive CSS framework based on Materialize Design which was used for this project mainly for
   the website's responsiveness. 
---
## Wireframes 
![New Wireframe 1](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/0e202e17-0472-41c5-86cb-353694c3c958)
![New Wireframe 2](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/977d8344-80c4-4224-a424-f72ebe5076a9)
![New Wireframe 3](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/b9b7f2c8-ad10-474b-b848-f18e561b8e51)
![New Wireframe 4](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/6880ab71-1385-4e96-93ee-4299f45fbfab)
![New Wireframe 5](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/15271c07-62b8-49d6-8281-8a1fed8ef921)
![New Wireframe 6](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/9096820d-63ed-453e-9e9d-37ff4573155f)
![New Wireframe 7](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/eb6a691c-9093-4a84-bc1d-4fbe62c626c7)
![New Wireframe 8](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/7e8e54e4-0215-4f9f-a4a4-2235031a4e8a)
![New Wireframe 9](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/513e4beb-ac3f-4780-9b14-e3e2d78bb5a3)
![New Wireframe 10](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/787ef0d3-e120-4d0a-847f-fba184abb742)
![New Wireframe 11](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/9bdeeed6-deed-451c-9c7d-4a2e5b91d837)
![New Wireframe 12](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/d3d476fd-d0a7-4ec5-8669-cb531e5887c1)

---
## Relationship Diagram (SQL)
![drawSQL-recipe-diagram-export-2023-08-16](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/affc501c-67e3-442a-8442-b1f5eb7baff6)

---
## Testing 
### Manual testing

### CI Python Linter

All Python codes were tested using CI Python Linter here are screenshots of the results
![init_py file testing results ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/f3adbc61-bfd2-4477-b259-bd19d6564fa4)
![routes file test results 2 ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/8aed67c7-d035-44a3-b17f-6a3397756a1c)
![routes file test results 1](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/55ed35ed-ffe6-4aaf-9967-316a6138d1d1)
![models file testing results ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/18b4c82c-cfdd-4272-b7d9-7eb15f5a7d11)
![run py file test results ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/a52f1c7b-7323-4a26-a140-56ba03ed6e7f)

### Lighthouse Performance
The website's responsiveness and performance was tested using Lighthouse. The website overall perfomance averages around 97-98 screenshots
are provided below. 
![Home page lighthouse status](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/a504b2ca-f3b4-4c46-ada7-ddf3c30ff9ed)
![Recipe Page lighthouse status ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/5bd8bb84-c360-49d3-9ca4-a09dd1800d01)
![New Recipe page lighthouse status](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/0554b464-5f8d-439a-ab98-2242e9ca6519)

### Testing User Expeerience UX
### User Goal

* The website's purpose is to allow the user to find share update and delete recipes. 

For the user to add a recipe they will need to click on the recipe tab on the navigation bar. They will be direct to the recipe page where the will see a add recipe button.

![recipe page (add recipe button)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/f0cb2895-aa4f-415d-8ad8-f7685ec10581)

The user will be required to fill out a recipe form.

![Recipe Form ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/e256e2ef-f7dd-4505-8997-eb6c799beea0)

Once the recipe form is filled the user can click on the submit button.

![Submit Recipe button ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/79c1e02a-f8b8-4b1d-bb28-214cd7402b3f)

Then the user will be redirected back to the recipe page showing the all recipe details the user applied on the form. Here is an example on how it would look

![Recipe record added to recipe page](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/fb948d9f-b484-4ed9-9292-d36b336dcd9e)

At the very end of the recipe record the user will see the edit and delete button. 

![Edit   Delete buttons ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/6dbff3d0-0729-4645-91b7-75117c049d24)

If the user wants to update or change any records they've made then they can click on the edit button it will direct them to the edit recipe page.

![Edit Recipe page](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/012c1bb7-26dc-4a6a-b888-cd2d8e89c241)

Once they've made ammendments the record will be updated and the user will find their new details on the same recipe page. 

![Recipe edit example ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/3e8813d1-4dc3-4815-93bd-2aa78e65d741)

If the user wants to delete any recipes they've made in the past then they can do this by clicking on the delete button. A modal message will popup to inform the user that if they chose to delete the recipe then they won't be able to retrive the deleted record. The user has two options, they can cancel the request meaning that the recipe will still be available for the user to view. If the user still wishes to delete the recipe they can click the delete button once again then the recipe will be deleted. 

![Delete recipe example](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/d42ea296-7f46-4f10-9326-4dd378b1eb20)

---

## Deployment 
The whole purpose for this project is to build back end application for the user to manipulate data. Gitpod only assigns to front end applications so we need to deploy the website via Heroku which operates back end applications. 

 To deploy this project you'll need to:
 1.Go to Heroku and navigate to the Deploy tab
 1.In the deployment method section, select "Connect to GitHub" 
 1.Search for your repo and click Connect  1.Click Enable Automatic Deploys 
 1.In the Manual deploy , select Deploy Branch
 1.Click on the "more" (dropdown) button and select "Run Console"
 1.Type python3 into the console and click Run
 1.Once the app is up and running so click on the "Open app"

---
## Credits

