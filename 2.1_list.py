my_list = [10, 33.3, 11j, 'this is a string', True, None,
           [100, 'wow', 'this is a list'], (200, 'hey', 'look', "it's a tuple"),
           {300, 400, 'this is a set'},
           {'key_1': 'this is', 'key_2': 'a dictionary'}]
for item in my_list:
    print (f'{item} - тип данных ---> {type(item)}')
