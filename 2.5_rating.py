# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

my_rating = [7, 5, 3, 3, 2]
item = None
print(my_rating)

while item != 100:
    item = int(input('Введите новый элемент рейтинга от 0 до 9, или введите 100 для выхода: '))
    if item < 0 or item > 9:
        print('Недопустимое значение')
        continue
    # если item не встречается в списке
    item_check = item in my_rating
    if not item_check:
        if item > my_rating[0]:
            my_rating.insert(0, item)
        elif item < my_rating[-1]:
            my_rating.append(item)
        else:
            for key, val in enumerate(my_rating):
                if item > val:
                    my_rating.insert(key, item)
                    break
    # если item уже встречается в списке
    else:
        new_index = my_rating.index(item) + my_rating.count(item)
        my_rating.insert(new_index, item)

    # выводим список и возвращаемся к вводу
    print(my_rating)
