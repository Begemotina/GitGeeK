'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''


class OwnError(Exception):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    @staticmethod
    def null_division(number1, number2):
        try:
            return (number1 / number2)
        except:
            return (f"Нельзя так, а то же всех поглотит черная дыра!!!")


division = OwnError(10, 15)
print(OwnError.null_division(12, 35))
print(OwnError.null_division(10, 0))
