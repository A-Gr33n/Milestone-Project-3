# Cookbook Recipes 

![Cookbook recipes responsiveness](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/9542105a-4054-4f13-853a-ddaa9f44e511) 

Click on this link to access the live site : https://cookbookrecipes-6b93722518a5.herokuapp.com/

---
## Description
Cookbook Recipes is a backend web application built upon a robust relational database, designed to empower users with effortless recipe management. It features recipe cards with comprehensive information, including recipe descriptions, ingredients, preparation steps, cooking times, and more. The application incorporates a full CRUD (Create, Read, Update, Delete) functionality, enabling users to effortlessly create, retrieve, display, edit, and delete recipe records. The website comprises three key pages: the homepage, which showcases a captivating carousel of recipes and provides convenient access to both adding and viewing recipes; the recipe page, where all created recipes are stored and can be edited or deleted; and finally, the new recipe page, where users can easily input their recipe details and create their own culinary masterpieces.

---
## User Experience UX

### User Stories
1. As a first-time visitor, I want clear and intuitive navigation and user interfaces that make it easy for me to interact with and enjoy the website's features.
2. As a first-time vistor I want to create recipes and would like to know where the recipes are stored.
3. As a first-time visitor, I want to view detailed recipe pages with clear instructions, ingredient lists, and images to help me decide which recipe to try.
4. As a first-time and returning user, I want to edit and update my created recipes whenever I discover improvements or variations.
5. As a first-time visitor and returning user, I want to easily delete any recipes I've created that I no longer wish to keep on the website.

### User's purpose

The user's purpose in using this recipe app is to streamline and enhance their culinary experience. With the ability to create, read, update, and delete records, this app empowers them to effortlessly manage their collection of recipes. Whether they're an amateur cook looking to experiment with new dishes or a seasoned chef seeking to organize their culinary creations, this app offers a user-friendly platform for all their recipe needs. By allowing them to create new recipes, access existing ones, make adjustments based on personal preferences or ingredient availability, and remove outdated or unused recipes, this app is a versatile tool that ensures they can easily curate their own personalized cookbook, making cooking and meal planning a seamless and enjoyable process.
 

---
## Design
   ### Colour Scheme
   * A background colour of --stripe: #cfd8dc; mainly BLUE color. , bg: #e1e1e1 a grey color tone;
   * Top navbar is colour #212121 (grey darken-4) with white text
   * Footer is colour #212121 (grey darken-4)   with white text
   * Form on add recipe page is colour #e3f2fd (blue lighten-5) with black text
   * Card is colour #212121 (grey darken-4) with white text and contains the edit button #2962ff  (btn blue accent-4) 
    and delete button (btn red)
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
This is the current setup of the relationship diagram used to build the relationship ids for the application.
![drawSQL-recipe-diagram-export-2023-09-23](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/e9c0ac21-efd0-4a8c-94d5-37bb5943c916)

This setup would be used for future developments to present additional features.   
![drawSQL-recipe-diagram-export-2023-08-16](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/affc501c-67e3-442a-8442-b1f5eb7baff6)

---
## Testing 
### Manual testing

### CI Python Linter

All Python codes were tested using CI Python Linter here are screenshots of the error results
![init_ py file indention error](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/3da1f661-90e1-417f-877f-4ac105854e5e)
![models file testing results ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/62ea8ea1-8ff6-4d06-8be2-0ccd0c06c531)
![routes file test results 1](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/004d4e78-4986-48ef-873f-5ae519d29c19)
![routes file test results 2 ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/cd2bc847-86ce-4b81-af9d-f2b39779e9ed)
![run py file test results ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/3a0a0530-aeeb-4a94-af98-20d2cf690e3e)


These are the screenshots that show resolved errors
![init py no errors](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/ddf78471-48a1-49a1-956f-6116a7a10fa5)
![run py no errors found ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/e567d3fc-c65d-4f14-8001-21aaedc010eb)
![models (modified) ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/86cc4b3a-8e2d-4e3a-91dd-651e1e25edf8)
![routes file no errors](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/0e6b3146-2dfd-44d2-889e-882cfab6bb1e)


### JS HINT 
JS Hint was used to test JavaScript codes and came up with these results shown below 
![js validator](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/d8548f0e-91dc-4665-ab1c-6ec39c4d0996) 

Here is the modified verison of JavaScript code. All errors of code couldn't be fixed due to the style of code materialize structures
its code.
![js validator (modified)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/a3685524-b791-45fa-ac85-ef300fe310e4)



### W3C Validation (HTML/CSS) 
All Html and CSS was tested using w3c validation and it came up with these errors shown below.
![Html validator 1 ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/4bdee8a7-d985-4e06-b9bc-d552c0e875cd)
![html validator 2](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/005a5ff7-30bc-431e-946e-476a3a08685c)
![CSS validator 3 ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/dd4fb4dd-57cc-43b3-b4da-5cd53063c34a) 

Here are screenshots of no errors found for both Html and CSS.
![No errors Html Validator ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/0d60fbfc-6c2e-4acf-86dd-5f3c7c8db347)
![Css validator no errors found ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/a8cb1508-fd82-4544-80b3-333e6a43610c)

### Audit Report 
Lighthouse audit was used test the Perfomance, Best practices, and Assessibility. The websites' overall report shows that the home page and 
add recipe page is 94-95 and the recipe page is 72.   

![Home page lighthouse status](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/976762c6-2ed9-40d1-8bc4-823b6dd074e3)

![recipe page lighthouse status](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/238163dc-444a-4b0e-a311-2b6a4c9030cc)

![New Recipe page lighthouse status](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/79e7e865-af41-47af-b079-9b933e2ddc56)

### Browser Testing
Here are screenshots to show that the app runs on more than one web browser. 
![Google chrome browser](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/14d3e566-9071-42b5-bd3a-65293cffbdb7)

![Brave Browser ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/7d31a456-2eec-46d3-830c-1cebdbbb7bf4)

![Firefox Browser](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/7086a6b6-4b31-4c89-9942-ab3213a131fc)

### Testing Responsiveness 
Here are screenshots showing the app's responsiveness on how it would be on phone and tablet devices.

![ipad, tablet responsiveness](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/40444ee1-cc93-4177-b94d-1bad0872214a) 

![Phone responsiveness ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/d755a1ee-cbd6-4c0e-b1a9-98192baa1d9b)


### Testing User Expeerience UX
1. As a first-time visitor, I want clear and intuitive navigation and user interfaces that make it easy for me to interact with and enjoy the website's features.

On the homepage, users will immediately notice a 'Add Recipe' button , designed to seamlessly guide them to the'Add Recipe' page. Additionally, there's a 'View Recipe' button that allows the user to access and view recipes on the recipe page. Furthermore  a  navigation bar adorns the top of the screen, presenting users with three convenient links: one to return to the homepage, another to explore the recipe page, and the third to access the 'Add Recipe' page. The frontend application boasts an eye-catching and vibrant design, featuring an inviting array of colors and a captivating carousel of recipes that perfectly encapsulates the essence of the application.

![Home page (user interactions)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/b8c00c38-2f7b-4412-b65d-e5b8f0bbba40)


![Navbar (user interactions)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/7b59ca71-15cc-48de-96e0-494163fcf8f4) 

2. As a first-time vistor I want to create recipes and would like to know where the recipes are stored.

The user will have the ability to create recipes on the 'Add recipe' page. A form is provided for the user to fill out the recipe's details.

![New Recipe page (user interaction)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/dd03abe1-484a-4a8f-b10f-5f834b7852e1) 


Once the form is filled out the user can click on the "submit recipe" button below. 

![Submit Recipe button ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/def448f2-b254-4de7-a2c5-c23af2d9e3cc)

A recipe record will be stored on the recipe page for the user to view. 

![new recipe record created ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/78f6bfa8-d710-4f7f-8c5f-f1ee200262df)

3. As a first-time visitor, I want to view detailed recipe pages with clear descriptions, ingredient lists, and images to help me decide which recipe to try.

Here's  a clear example shown below of what the detailed recipe would look like once the recipe is created. Cards are made for the user showing the recipes description, ingredient list and images 
for the user to read.

![Recipe Page (example)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/66c5f82d-e587-48d5-adb8-70c97e500e5a)

4. As a first-time and returning user, I want to edit and update my created recipes whenever I discover improvements or variations.

The user will have the ability to edit update a recipe by clicking on edit button below.  

![Edit   Delete buttons ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/775f3335-af0f-4e5c-9342-7eae36d76a53)

They will directed to the "edit recipe page". A form will be provided for the user to fill out updated details. 

![Edit Recipe page](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/99508490-c697-4e99-bbd9-20f7cc8724c8) 

When the form is filled out the user can click on the 'edit recipe' button below. 

![Editing Process (part 2)](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/8e3d951d-b7f3-47a0-820e-bea1761d2a55)

The recipe will be stored in the recipe page showing the updated record.

![Edit update](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/5cf38128-759b-4cc5-a51a-aa91fac93907)


5. As a first-time visitor and returning user, I want to easily delete any recipes I've created that I no longer wish to keep on the website.

If the user wants to delete any recipes they've made in the past then they can do this by clicking on the delete button.

![Edit   Delete buttons ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/0de1381e-ab4d-4adb-a5ae-b2d096e74358) 

A modal message will popup to inform the user that if they chose to delete the recipe then they won't be able to retrive the deleted record. The user has two options, they can cancel the request meaning that the recipe will still be available for the user to view. If the user still wants to delete the recipe they can click the delete button once again then the recipe will be deleted. 

![Delete option](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/38e8d5be-92a1-4aa2-9737-fa4d18c62421)  

Then the recipe will disappear as shown in this example. 

![Recipe deleted example ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/71077de0-69cd-4fef-bb69-1b97611c2fd8)

---

## Deployment 
The whole purpose for this project is to build a back end application for the user to manipulate data. Gitpod only assigns to front end applications so we need to deploy the website via Heroku which operates back end applications. 

 To deploy this project you'll need to:
 
  1. Go to Heroku and navigate to the Deploy tab
  2. In the deployment method section, select "Connect to GitHub" 
  3. Search for this repo by typing Milestone Project 3 and click Connect
  4. Click Enable Automatic Deploys 
  5. In the Manual deploy , leave the branch on main and select Deploy Branch
  6. Click on the "more" (dropdown) button and select "Run Console"
  7. Type python3 into the console and click Run
  8. A terminal will show up in the terminal type in the command "from taskmanager import db" then "db.create_all()"
  9. Exit the Python terminal, by typing "exit()" and hitting enter, and close the console. 
  10. Once the app is up and running, click on the "Open app" then the app will run.

## DEBUG MODE 
Before deployment Debug mode was turn off by setting it to false to ensure that no errors will appear when opening the app. Here
is a screenshot to show that Debug mode is turned off. 

![Debug Mode turn off ](https://github.com/A-Gr33n/Milestone-Project-3/assets/120597058/027c272d-fb4c-433e-b268-a6e74934fa85)

---
## Credits
 ### Code
 /*Credit:code for setting background color and pattern https://css-tricks.com/a-few-background-patterns-sites/
   
 <p>  body {</p>
 <p>   --stripe: #cfd8dc;</p>
 <p>  --bg: #e1e1e1; </p>

  <p> background: linear-gradient(135deg, var(--bg) 25%, transparent 25%) -50px 0,</p>
  <p> linear-gradient(225deg, var(--bg) 25%, transparent 25%) -50px 0,</p>
  <p> linear-gradient(315deg, var(--bg) 25%, transparent 25%),</p>
  <p> linear-gradient(45deg, var(--bg) 25%, transparent 25%);</p>
  <p> background-size: 100px 100px;</p>
  <p> background-color: var(--stripe);</p>
}

 ### Relational Database Walkthough
   The Relational Database walkthrough provided by codeinstitute was used to assist the database setup
   for this project.
 
 ### Frameworks 
 * Materialize 1.0
    - Materialize was majoritively used to build the design of application and to keep it responive
 
 ### Media
 
 * Pexels.com
    - Pexels.com provided free photos to create the carousel for the home page and the background image.

 

