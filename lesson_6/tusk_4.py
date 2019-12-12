'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"машина {self.name} поехала прямо")

    def stop(self):
        print(f"машина {self.name} остановилась")

    def turn(self, direction):
        print(f"машина {self.name} повернула на {direction}")

    def show_speed(self):
        print(f'скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 60:
            print(f'скорость {self.speed}')
        else:
            print(f'!!!ACHTUNG!!!! скорость {self.speed} !!ACHTUNG!!!!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed <= 40:
            print(f'скорость {self.speed}')
        else:
            print(f'!!!ACHTUNG!!!! скорость {self.speed} !!ACHTUNG!!!!')


# я не знаю чего с ней делать наверно это для будущий разработки
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


if __name__ == '__main__':
    # в скобках будет вот так, потому-что я замучался смотреть порядок
    bug = TownCar(speed=30, color="Бежевый", name="bug", is_police=False)
    cat = WorkCar(speed=60, color="зеленый", name="СAT", is_police=False)
    bugatti_chiron = PoliceCar(speed=30, color="Кораловый", name="Bugatti Chiron", is_police=True)
    grand_cherokee = TownCar(speed=90, color="Черный", name="Большой Индеец", is_police=False)
    dog = WorkCar(speed=130, color="Фиолетовый", name="DOG", is_police=True)

    # доступ к атрибутам, выведите результат.
    # наверно не самый хороший способ делать вот такой кортеж, но все же у меня он будет
    for i in (bug, cat, grand_cherokee, dog,):
        print(i.speed)
        print(i.color)
        print(i.name)
        print(i.is_police)
        if i != dog:
            print("\nдругая машина")

    # Выполните вызов методов и также покажите результат.
    for i in (bug, cat, grand_cherokee, dog,):
        i.go()
        i.turn("право")
        i.show_speed()
        i.go()
        i.turn("лево")
        i.go()
        i.stop()
        if i != dog:
            print("\nдругая машина")

