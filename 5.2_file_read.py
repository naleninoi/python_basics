# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('file5_2.txt', encoding='utf-8') as my_file:
    content = my_file.readlines()
    print(f'Всего в файле {len(content)} строк.')
    for num, line in enumerate(content):
        print(f'строка {num + 1} - количество слов {line.count(" ") + 1}')
