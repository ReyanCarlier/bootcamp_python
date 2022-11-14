from book import Book
from recipe import Recipe

def main():
    myBook = Book("mybook")
    firstRecipe = Recipe("Mud", 1, 0, ["Dirt", "Water"], "It's just... mud...", "dessert")
    secondRecipe = Recipe("Mud2", 1, 0, ["Dirt", "Water"], "It's just... mud...", "lunch")
    """print(str(firstRecipe))"""
    myBook.add_recipe(firstRecipe)
    myBook.add_recipe(secondRecipe)
    mudRecipe = myBook.get_recipe_by_name("Mud2")
    print(str(mudRecipe))
    
if __name__ == "__main__":
    main()