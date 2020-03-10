# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translate = ['Один', 'Два', 'Три', 'Четыре']

file_input = open('file5_4in.txt', encoding='utf-8')
file_output = open('file5_4out.txt', 'x', encoding='utf-8')

english = file_input.readlines()
print(english)

for num, line in enumerate(english):
    new_line = translate[num] + line[-5:-1]
    print(new_line, file=file_output)

file_input.close()
file_output.close()
