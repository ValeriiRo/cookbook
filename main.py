from pprint import pprint
file = open("recipes.txt", "r", encoding="UTF-8")
cook_book = {}
food_name = file.readline().strip()
while food_name != '':
    cook_book.setdefault(food_name,[])
    quantity_ingredient = int(file.readline().strip())
    for quantity in range(quantity_ingredient):
        ingredient = file.readline().strip().split('|')
        cook_book[food_name] += [{'ingredient_name': ingredient[0],'quantity': int(ingredient[1]), 'measure': ingredient[2]}]
    file.readline()
    food_name = file.readline().strip()
pprint(cook_book)
########################################################################################################################
def accept_list():
    dishes = input('Введитеназвание блюд через запятую: ').split(',')
    for dish in dishes:
        if cook_book.get(dish) != None:
            continue
        else:
            print('Введено не коректное название блюда!')
            return
    return dishes

def correct_number():
    try:
        person_count = int(input('Введите колисемтао персон: '))
        return person_count
    except ValueError:
        print('Неверное значение!')

person_count = None
dishes = None
while dishes == None:
    dishes = accept_list()
while person_count == None:
    person_count = correct_number()

get_shop_list_by_dishes = (dishes, person_count)
list_by_dishes = {}
for dish in get_shop_list_by_dishes[0]:
    dish = ''.join(dish)
    for purchase in cook_book[dish]:
        list_by_dishes.setdefault(purchase['ingredient_name'],{'measure': purchase['measure'], 'quantity': 0})
        list_by_dishes[purchase['ingredient_name']]['quantity'] += purchase['quantity'] * person_count
pprint(list_by_dishes)