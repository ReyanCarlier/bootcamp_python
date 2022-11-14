import sys
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        if (name is None or len(name) == 0):
            print("Incorrect Book name")
            sys.exit()
        self.name = name
        self.recipes_list = {
			"starter":[],
			"lunch":[],
			"dessert":[]
		}
        self.creation_date = datetime.now
        self.last_update = datetime.now
        
    def get_recipe_by_type(self, recipe_type):
        return self.recipe_list[recipe_type]
    
    def add_recipe(self, recipe):
        print(type(recipe))
        if (type(recipe) != Recipe):
            print("add_recipe: argument isn't a Recipe.")
            sys.exit()
        self.recipes_list[recipe.recipe_type].insert(0, recipe)
        self.last_update = datetime.now

    def get_recipe_by_name(self, _name):
        for val in self.recipes_list:
            for recipe in self.recipes_list[val]:
                if recipe.name == _name:
                    return recipe