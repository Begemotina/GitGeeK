"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление.
 Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
"""
# Запрашиваем числа
def numbers_f(n):
    while True:
        number = (input(f"ВВедите чило {n}\n"))
        if number.isdigit():
            number = float(number)
            break
        else:
            if number[0] == "-":
                number = float(number)
                break
            else:
                print("Надо цифрой, а не букавками : ")
    return number

# делим
def division_f(a = 72.0, b = 72.0):

    if b != 0:
        return(a / b)
    else:
        return "Нечего на ноль делить, это вредно для кармы"

# запускаем наше развлечение
a = numbers_f(1)
b = numbers_f(2)
print(f" \nРезультат: {division_f(a,b)}")