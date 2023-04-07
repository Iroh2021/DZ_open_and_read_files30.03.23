import os
from pprint import pprint
current = os.getcwd()
folder_name = 'DZ_open_and_read_files'
file_name = 'recipies_book.txt'
full_path = os.path.join(current, folder_name, file_name)
with open(file_name, 'rt', encoding='utf-8') as file:
    cook_book = {}
    for recipie in file:
        rec_name = recipie.strip()
        ingredients = []
        ing_count = int(file.readline().strip())
        for _ in range(ing_count):
            ingredient_name, quantity, measure =file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name':ingredient_name,
                'quantity':quantity,
                'measure':measure
            })
        file.readline()
        cook_book[rec_name] = ingredients
# "print" для проверки первой задачи
# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        if i in cook_book:
            for ingr in cook_book[i]:
                measure_and_quantity = {}
                if ingr['ingredient_name'] not in res:
                    measure_and_quantity['measure'] = ingr['measure']
                    measure_and_quantity['quantity'] = int(ingr['quantity']) * person_count
                    res[ingr['ingredient_name']] = measure_and_quantity
                else:
                    res[ingr['ingredient_name']]['quantity'] = res[ingr['ingredient_name']]['quantity'] + int(ingr['quantity']) * person_count
        else:
            print(f'Takogo bluda net v spiske')
    return res

# "print" для проверки второй задачи
# print(get_shop_list_by_dishes(['Омлет','Фахитос'], 2))

