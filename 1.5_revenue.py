revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))

if revenue > costs:
    profit = revenue - costs
    print(f'Прибыль организации составила {profit} $')
    print('Рентабельность выручки составила %4.1f процентов' % (profit / revenue * 100))
    employees = int(input('Для расчета удельной прибыли введите количество сотрудников в организации: '))
    print('Удельная прибыль составила %8.2f $' % (profit / employees))

elif revenue == costs:
    print('Сумма доходов равна сумме расходов.')

else:
    print(f'Убытки организации составили {revenue - costs}$')
