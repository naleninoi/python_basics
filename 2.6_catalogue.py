# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

# формируем структуру каталога (добавляем названия категорий в список)
key_list = []
while True:
    key = input('Добавьте новую характеристику товара (или exit для выхода): ').capitalize()
    if key != 'Exit':
        key_list.append(key)
    else:
        break

# добавляем характеристики в пустой каталог (словарь)
index = {}
for key in key_list:
    index.setdefault(key)

# добавляем товары в каталог, для каждого товара запрашиваем значения харакетиристик
# на выходе получаем список товаров (кортежей). Каждый кортеж включает в себя номер товара и его характеристики (словарь)
catalogue = []
check = True
number = 1
while check != 'Н':
    print(f'Позиция №{number}')
    for key, val in index.items():
        index[key] = input(f'Введите значение характеристики "{key}": ')
    position = (number, index.copy())
    catalogue.append(position)
    number += 1
    check = input('Все параметры для этого товара заполнены. Продолжить? Д/Н ').upper()

# вывод на экран полного каталога товаров из списка
print('*' * 50)
print('КАТАЛОГ ТОВАРОВ')
for item in catalogue:
    print(item)

# формирование каталога значений (словарь)
# список характеристик берем из списка key_list, сформированного в начале работы
# делаем итерацию по списку характеристик товаров (ключей словаря)
# далее перебираем каталог товаров, из каждой позиции берем вторую часть (словарь), и по характеристике товара выбираем значение.
# полученное значение добавляем в список. Когда все товары просмотрены, список значений характеристики и саму характеристику
# добавляем в каталог значений - {key: (val_1, val_2...)}
analytics = {}
for key in key_list:
    new_list = []
    for item in catalogue:
        new_line = item[1]
        new_val = new_line.get(key)
        new_list.append(new_val)
    analytics[key] = new_list

# вывод на экран каталога значений
print('*' * 50)
print('СВОДНАЯ ВЕДОМОСТЬ ПО ПОЗИЦИЯМ')
for key, val in analytics.items():
    print(key, val)
