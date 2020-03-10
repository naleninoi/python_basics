# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# отделяет цифры в начале строки от букв
def digit_split(line):
    for i, s in enumerate(line):
        if not s.isdigit():
            return line[:i]


# импорт из файла в список
lectures_dict = []
with open('file5_6.txt', encoding='utf-8') as f_input:
    for line in f_input:
        lectures_dict.append(line.rstrip().split())

# формирование словаря с названиями дисциплин, подсчет кол-ва часов
lectures = {}
for lecture in lectures_dict:
    hours = 0
    for i in range(1, 4):
        try:
            hour = int(digit_split(lecture[i]))
        except ValueError:
            hour = 0
        hours += hour
    key = lecture[0].replace(":", "")
    lectures[key] = hours

print(f'Общее количество часов по дисциплинам:\n{lectures}')
