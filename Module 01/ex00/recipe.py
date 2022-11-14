import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if (name is None or len(name) == 0):
            print("Incorrect name")
            sys.exit()
        self.name = name
        if (cooking_lvl is None or cooking_lvl < 1 or cooking_lvl > 5):
            print("Incorrect cooking_lvl")
            sys.exit()
        self.cooking_lvl = cooking_lvl
        if (cooking_time is None or cooking_time < 0):
            print("Incorrect cooking_time")
            sys.exit()
        self.cooking_time = cooking_time
        if (type(ingredients) != list or len(ingredients) == 0):
            print("Incorrect ingredients")
            sys.exit()
        self.ingredients = ingredients
        self.description = description
        if (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            self.recipe_type = recipe_type
        else:
            print("Incorrect recipe_type")
            sys.exit()
            
    def __str__(self):
        txt = "Name : " + self.name + "\nDescription : " + self.description + "\nType : " + self.recipe_type + "\nLevel : " + str(self.cooking_lvl) + "\nTime : " + str(self.cooking_time) + " minute(s)\nIngredients :\n"
        for	ingredient in self.ingredients:
            txt = txt + "- " + ingredient + "\n"
        
        return txt