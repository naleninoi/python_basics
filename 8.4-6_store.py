# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.

from abc import ABC


class Storage:
    count = 0
    departments = {'000': 'Склад', '001': 'Бухгалтерия', '002': 'Отдел проектирования', '003': 'Отдел логистики'}

    def __init__(self):
        self.storage_000 = []
        self.storage_001 = []
        self.storage_002 = []
        self.storage_003 = []

    def add(self, item):
        # приемка новой оргтехники на склад
        Storage.count += 1
        self.storage_000.append(item)
        print(f'Приемка на склад - успешно, общее кол-во единиц оргтехники на складе: {Storage.count}')

    def move(self, item):
        # перемещение оргтехники со склада
        dept = input(
            'Введите номер отдела для перемещения оргтехники: 001 - бухгалтерия, 002 - отдел проектирования, 003 - отдел строительства: ')
        if dept == '001':
            self.storage_001.append(item)
            self.storage_000.remove(item)
            print(f'Перемещение в бухгалтерию успешно, общее кол-во оргтехники в отделе: {len(self.storage_001)}')
        elif dept == '002':
            self.storage_002.append(item)
            self.storage_000.remove(item)
            print(
                f'Перемещение в отдел проектирования успешно, общее кол-во оргтехники в отделе: {len(self.storage_002)}')
        elif dept == '003':
            self.storage_003.append(item)
            self.storage_000.remove(item)
            print(
                f'Перемещение в отдел строительства успешно, общее кол-во оргтехники в отделе: {len(self.storage_003)}')
        else:
            print('Неверный номер отдела')

    def restore(self, item):
        # возврат оргтехники на склад
        if item in self.storage_001:
            self.storage_001.remove(item)
            self.storage_000.append(item)
            print(f'Перемещение успешно из бухгалтерии на склад, осталось оргтехники в отделе: {len(self.storage_001)}')
        elif item in self.storage_002:
            self.storage_002.remove(item)
            self.storage_000.append(item)
            print(
                f'Перемещение успешно из отдела проектирования на склад, осталось оргтехники в отделе: {len(self.storage_002)}')
        elif item in self.storage_003:
            self.storage_003.remove(item)
            self.storage_000.append(item)
            print(
                f'Перемещение успешно из отдела строительства на склад, осталось оргтехники в отделе: {len(self.storage_003)}')
        else:
            print('На балансе не числится')

    @property
    def report(self):
        # вывод полного отчета
        print(f'\nСКЛАД - количество оргтехники {len(self.storage_000)}')
        for item in self.storage_000:
            for key in (item.__dict__).values():
                print(key, end=2*'\t')
            print('\n')
        print(f'\nБУХГАЛТЕРИЯ - количество оргтехники {len(self.storage_001)}')
        for item in self.storage_001:
            for key in (item.__dict__).values():
                print(key, end=2*'\t')
            print('\n')
        print(f'\nОТДЕЛ ПРОЕКТИРОВАНИЯ - количество оргтехники {len(self.storage_002)}')
        for item in self.storage_002:
            for key in (item.__dict__).values():
                print(key, end=2*'\t')
            print('\n')
        print(f'\nОТДЕЛ СТРОИТЕЛЬСТВА - количество оргтехники {len(self.storage_003)}')
        for item in self.storage_003:
            for key in (item.__dict__).values():
                print(key, end=2*'\t')
            print('\n')


class Appliances(ABC):
    # общий класс Оргтехника
    def __init__(self, type, model, s_n, price):
        self.type = type
        self.model = model
        self.s_n = s_n
        self.price = price

    def __str__(self):
        return f'Тип: {self.type};\nМодель: {self.model};\nСерийный №: {s_n}\nЦена: {self.price}'


class Printer(Appliances):
    # класс Принтеры
    def __init__(self, model, s_n, price, print, type='Принтер'):
        super().__init__(type, model, s_n, price)
        self.print = print

    def __str__(self):
        return super().__str__() + f'\nТип печати: {self.print}.'


class Scanner(Appliances):
    # класс Сканеры
    def __init__(self, model, s_n, price, dpi, type='Принтер'):
        super().__init__(type, model, s_n, price)
        self.dpi = dpi

    def __str__(self):
        return super().__str__() + f'\nРазрешение: {self.dpi} dpi.'


class Copier(Appliances):
    # класс Копиры
    def __init__(self, model, s_n, price, size, type='МФУ'):
        super().__init__(type, model, s_n, price)
        self.size = size

    def __str__(self):
        return super().__str__() + f'\nМакс.формат бумаги: {self.size}.'


# создание склада
totalStore = Storage()

# создание единиц оргтехники
i_1 = Printer('Brother BW-200W', '1s1834812', 18920.15, 'ч/б')
i_2 = Scanner('Mustek A-600', '6ffd23221', 6548.75, '600')
i_3 = Copier('Kyocera J-675', '9vcvd334', 24569.12, 'A3')
i_4 = Printer('HP LaserJet 600', '13ww4r4vc', 19000.58, 'цвет')

# приемка оргтехники на склад
totalStore.add(i_1)
totalStore.add(i_2)
totalStore.add(i_3)
totalStore.add(i_4)

# перемещение оргтехники по отделам
totalStore.move(i_1)
totalStore.move(i_2)
totalStore.move(i_3)

# возврат оргтехники на склад
totalStore.restore(i_1)

# вывод отчета
totalStore.report
