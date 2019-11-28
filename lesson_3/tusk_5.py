"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

"""
def numbers_f(number):

    if number.isdigit():
        number = float(number)
        return number
    else:
        if number[0] == "-":
            number = float(number)
            return number
        else:
            return 0   # если это не q и не число то будет возвращать 0
# def_sum()2
run = True
result = 0
while run:
    numbers = input("Введите числа через пробел или q что бы закончить \n ").split()
    for number in numbers:
        if number == "q" or number == "Q":
            run = False
            break
        else:
            data = numbers_f(number)
            result += data
    print(f"Результат: {result}")

print(f"окончательный итог: {result}")

