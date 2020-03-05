# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
from sys import argv
from itertools import count

script_name, start = argv
for number in count(int(2)):
    if number % 100 == 0:
        print(number)
        check = input('Continue? (Y/N): ').upper()
        if check == 'Y':
            continue
        else:
            break
    print(number)
