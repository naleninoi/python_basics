number = int(input('Введите целое положительное число: '))

i = 0
while number > 0:
    if (number % 10) > i:
        i = number % 10
    number = number // 10

print('Наибольшая цифра в числе - %d' % (i))
