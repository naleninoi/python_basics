# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, поехал')

    def stop(self):
        print(f'Автомобиль {self.name}, цвет {self.color}, остановился')

    def turn(self, direction):
        print(f'Автомобиль повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 60:
            print('Вы превышаете разрешенную скорость (60 км/ч)')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 40:
            print('Вы превышаете разрешенную скорость (40 км/ч)')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car_1 = TownCar(80, 'красный', 'Лада Ларгус')
car_1.go()
car_1.turn('вправо')
car_1.show_speed()
car_1.stop()
print('Это автомобиль полиции? {}\n'.format(car_1.is_police))

car_2 = SportCar(120, 'желтый', 'Порше Кайен')
car_2.go()
car_2.turn('влево')
car_2.show_speed()
car_2.stop()
print('Это автомобиль полиции? {}\n'.format(car_2.is_police))

car_3 = WorkCar(60, 'серый', 'УАЗ-452')
car_3.go()
car_3.turn('вправо')
car_3.show_speed()
car_3.stop()
print('Это автомобиль полиции? {}\n'.format(car_3.is_police))

car_4 = PoliceCar(80, 'синий', 'Форд Фокус')
car_4.go()
car_4.turn('влево')
car_4.show_speed()
car_4.stop()
print('Это автомобиль полиции? {}\n'.format(car_4.is_police))
