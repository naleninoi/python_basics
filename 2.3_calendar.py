# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

calend_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',
               'осень', 'осень', 'осень', 'зима']
calend_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
               7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
while True:
    month = int(input('Введите номер месяца от 1 до 12: '))
    if month < 1 or month > 12:
        print('В нашем календаре только 12 месяцев')
    else:
        break
print(f'Месяц №{month} - {calend_dict.get(month)}. Время года - {calend_list[month - 1]}')
