# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
# заполняем список
while True:
    item = input('Добавьте новый элемент списка (000 - для выхода): ')
    if item != '000':
        my_list.append(item)
        print(my_list)
    else:
        break
# меняем местами нечетные и четные элементы списка
list_range = len(my_list)
for item in range(1, list_range, 2):
    my_list[item - 1], my_list[item] = my_list[item], my_list[item - 1]

print(my_list)
