def open_file(file):
    with open(file) as f:
        return f.read()


def prepare_book():
    cook_book = {}
    file = open_file('recipe.txt')
    text = file.split('\n\n')
    for i in range(len(text)):
        new_text = str(text[i]).split('\n')
        key = new_text[0]
        count_line = new_text[1]
        value = []
        for j in range(int(count_line)):
            ingridient_name = new_text[2+j].split('|')
            ingridients = {'ingredient_name': ingridient_name[0], 'quantity': ingridient_name[1],
                           'measure': ingridient_name[2]}
            value.append(ingridients)
        cook_book[key] = value
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    book = prepare_book()
    dict_ = {}
    for item in list(dishes):
        recipe = book.get(item)
        for i in recipe:
            if i.get('ingredient_name') not in dict_:
                dict2 = dict()
                dict_[i.get('ingredient_name')] = dict2
                dict2['measure'] = i.get('measure')
                dict2['quantity'] = int(i.get('quantity')) * person_count
            else:
                temp = dict_[i.get('ingredient_name')]['quantity']
                dict2 = dict()
                dict_[i.get('ingredient_name')] = dict2
                dict2['measure'] = i.get('measure')
                dict2['quantity'] = int(i.get('quantity')) * person_count + temp
    return dict_
