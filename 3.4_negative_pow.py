def negative_pow(arg_1, arg_2):
    neg_pow = 1 / (pow(arg_1, abs(arg_2)))
    return neg_pow


def negative_pow_2(arg_1, arg_2):
    neg_pow = 1
    for i in range(abs(arg_2)):
        neg_pow = neg_pow * arg_1
    return (1 / neg_pow)


num_1 = abs(float(input('Введите основание степени - положительное число: ')))
num_2 = int(input('Введите показатель степени - целое отрицательное число: '))
print(f'{num_1} в степени {num_2} = {negative_pow(num_1, num_2)}')
print(f'{num_1} в степени {num_2} = {negative_pow_2(num_1, num_2)}')
