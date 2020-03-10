# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

# импорт из файла в список
firms_dict = []
with open('file5_7.txt', encoding='utf-8') as f_input:
    for line in f_input:
        firms_dict.append(line.rstrip().split())

# формирование словаря с прибылями/убытками, подсчет средней прибыли
firms = {}
total_profit = 0
profit_firms = 0
for firm in firms_dict:
    key = firm[0]
    profit = int(firm[2]) - int(firm[3])
    firms[key] = profit
    # в подсчет средней прибыли включаются только доходы
    if profit > 0:
        total_profit += profit
        profit_firms += 1
av_profit = total_profit / profit_firms
print(f'Всего организаций {len(firms_dict)}, из них прибыльных {profit_firms}, средняя прибыль {av_profit}')

# экспорт в JSON
average_profit = {'Средняя прибыль': av_profit}
export_list = [firms, average_profit]
print(export_list)
with open('file5_7exp.json', 'w', encoding='utf-8') as output_json:
    json.dump(export_list, output_json)
print(f'успешный экспорт в файл {output_json.name}')
