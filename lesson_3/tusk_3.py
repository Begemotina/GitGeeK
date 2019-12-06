"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""
# Решаем чего выводить
def sum_f(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and a <= c:
        return a + c
    else:
        return b + c

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

# Собственно само действо
a = numbers_f(1)
b = numbers_f(2)
c = numbers_f(3)

print(f"Результат: {sum_f(a, b, c)}")
