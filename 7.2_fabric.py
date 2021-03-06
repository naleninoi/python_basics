# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
# для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric(self):
        print(f'Расход ткани на изделие: {self.name}')


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def fabric(self):
        super().fabric()
        return round((self.size / 6.5 + 0.5), 2)


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def fabric(self):
        super().fabric()
        return round((self.height * 2 + 0.3), 2)


item_1 = Coat('Пальто мужское', 180)
print(item_1.fabric)
item_2 = Suit('Костюм спортивный', 54)
print(item_2.fabric)
print(item_1.fabric + item_2.fabric)
