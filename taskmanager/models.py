from taskmanager import db

class Recipe(db.Model):
    # 
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - recipe: {1}".format(
            self.id, self.recipe_name, self.is_urgent
        )