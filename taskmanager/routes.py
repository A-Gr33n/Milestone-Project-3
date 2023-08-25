from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Recipe

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/recipes")
def recipes():
    recipes = list(Recipe.query.order_by(Recipe.recipe_name).all())
    return render_template("recipes.html", recipes=recipes)

@app.route("/search", methods=["GET"])
def search_recipes():
    query = request.args.get("query")
    

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    print(request)
    if request.method == "POST":
        recipe = Recipe(
            recipe_name = request.form.get("recipe_name"),
            recipe_description = request.form.get("recipe_description"),
            image_url = request.form.get("image_url"),
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html")

@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.recipe_description = request.form.get("recipe_description")
        recipe.image_url = request.form.get("image_url")
        db.session.commit()
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html", recipe=recipe)

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("recipes"))
