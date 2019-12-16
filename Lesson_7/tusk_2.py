'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Площадь общая ткани : {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь такни для пальто {self.square_coat}'


class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма {self.square_jacket}'

coat = Coat(6, 4)
jacket = Jacket(8, 12)


print(coat)
print(coat.get_sq_full)
print('*'*10)
print(jacket)
print(jacket.get_sq_full)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())