a = int(input('Сколько км пробежал спортсмен в 1-й день тренировок? - '))
b = int(input('К какому ежедневному результату стремится спортсмен? - '))
days = 1

while a < b:
    a = a + a * 0.1
    days += 1

print(f'Результат достигнут на {days} день тренировок')
