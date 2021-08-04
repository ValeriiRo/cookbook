from pprint import pprint
file = open("recipes.txt", "r", encoding="UTF-8")
cook_book = {}
food_name = file.readline().strip()
while food_name != '':
    cook_book.setdefault(food_name,[])
    quantity_ingredient = int(file.readline().strip())
    for quantity in range(quantity_ingredient):
        ingredient = file.readline().strip().split('|')
        cook_book[food_name] += [{'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}]
    file.readline()
    food_name = file.readline().strip()
pprint(cook_book)