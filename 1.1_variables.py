name = input('Как вас зовут?: ')
age = int(input('Сколько вам лет?: '))

# вычисляем время жизни в секундах
time = age * 365 * 24 * 60 * 60

print(f'А знаете, {name},  ведь {age} лет - это целых {time} секунд...')
