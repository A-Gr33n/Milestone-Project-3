from cookbookapp import db


class Recipe(db.Model):
    # Custom Models
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=True)
    cook_time = db.Column(db.Text, nullable=True)
    prep_time = db.Column(db.Text, nullable=True)
    servings = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.Text, nullable=True) 
    image_url = db.Column(db.Text, nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - recipe: {1}".format(
            self.id, self.recipe_name, self.is_urgent
        )
