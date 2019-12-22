'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
import datetime


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extractor(cls, data):
        data = data.split("-")
        for i in range(0, len(data)):
            data[i] = int(data[i])

        return data[0], data[1], data[2]

    @staticmethod
    def validation(data):
        data = Data.extractor(data)

        if 0 < data[0] < 31:
            if 0 < data[1] < 13:
                if data[2] > 0:
                    return "все верно"
                else:
                    print('год не правильный')
            else:
                print("Не правильный Месяц")

        else:
            print("Не правильный день")


if __name__ == '__main__':
    # проверка методов без создания класса
    print(Data.extractor("31-10-1985"))
    print(Data.validation('18-12-2019'))

    # проверка методов с соданием экземплиара класса
    today = Data('12-12-2019')
    print(today.extractor('12-12-2019'))
    print(today.validation('28-12-2019'))

    # экперименты
    now = datetime.datetime.now()  # 2019-12-18
    today = f'{now.day}-{now.month}-{now.year}'  # тут должен быть другой порядок
    print(Data.extractor(today))
    print(Data.validation(today))
