words_list = (input('Введите несколько слов, разделенных пробелами: ')).split(' ')
for num, word in enumerate(words_list):
    print(num, word[:9])
