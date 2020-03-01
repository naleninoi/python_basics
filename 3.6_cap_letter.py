def int_func(words):
    cap_word = words.title()
    return cap_word


my_string = input('Введите несколько слов, разделенных пробелами: ')
print(int_func((my_string)))
