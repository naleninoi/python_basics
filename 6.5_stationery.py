class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title='pen'):
        self.title = title

    def draw(self):
        print('ЖЫ ШЫ пишы с буквой "и"')


class Pencil(Stationery):
    def __init__(self, title='pencil'):
        self.title = title

    def draw(self):
        print('очередной чертеж выполнен')


class Handle(Stationery):
    def __init__(self, title='handle'):
        self.title = title

    def draw(self):
        print('ярче значит лучше')


item_1 = Pen()
print(item_1.title)
item_1.draw()

item_2 = Pencil()
print(item_2.title)
item_2.draw()

item_3 = Handle()
print(item_3.title)
item_3.draw()
