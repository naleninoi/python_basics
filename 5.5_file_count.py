# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('file5_5.txt', 'w', encoding='utf-8') as my_file:
    line = ''
    for i in range(0, 11):
        line += str(randint(0, 100)) + ' '
    print(line, file=my_file)

with open('file5_5.txt', encoding='utf-8') as my_file:
    content = my_file.read()
    my_dict = list(map(int, content.split()))
    print(f'Сумма чисел в файле {sum(my_dict)}')
