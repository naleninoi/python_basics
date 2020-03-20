# Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать
# у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class ListError(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    my_num = input('Введите целое число для заполнения списка (или stop для завершения): ')
    if my_num.lower() == 'stop':
        break
    else:
        try:
            if not my_num.isdigit():
                raise ListError('Список должен состоять только из целых чисел')
        except ListError as error_msg:
            print(error_msg)
        else:
            my_list.append(int(my_num))
            print(my_list)
print(f'Работа завершена, получен список:\n{my_list}')
