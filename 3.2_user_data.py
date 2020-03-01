def user_data(name, surname, birth, city, email, phone):
    print(
        f'Данные о пользователе: {name} {surname}, {birth} год рождения, место проживания {city}, e-mail {email}, номер телефона {phone}.')


data_1 = input('Введите ваше имя: ')
data_2 = input('Введите вашу фамилию: ')
data_3 = input('Введите год вашего рождения: ')
data_4 = input('Введите город вашего проживания: ')
data_5 = input('Введите адрес e-mail: ')
data_6 = input('Введите номер телефона: ')

user_data(name=data_1, surname=data_2, birth=data_3, city=data_4, email=data_5, phone=data_6)
