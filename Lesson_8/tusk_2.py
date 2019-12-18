'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

number1 = input("Введите положительное число: ")
number2 = input("Введите положительное число: ")


try:

    number1 = int(number1)
    number2 = int(number2)
    print(type(number1))
    if number2 == 0:
        raise OwnError("Вы ввели 0!!! теперь нас всех съедят помидоры")
except ValueError:
    print("вы ввели аброкатабру")
except OwnError as err:
    print(err)
else:
    print(f" результат деления: {number1 / number2}")
