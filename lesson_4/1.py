'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''


from sys import argv
# не буду делать никакую проверку.
# если в качестве числа будет например -2 то, пусть этот сотруднки страдает.
script_name, salary, time, bonus = argv

try:
    salary = float(salary)
    time = float(time)
    bonus = float(bonus)
    print(f" Зарплата сотрудника составляет: {(salary * time) + bonus}")

except ValueError:
    print('Я цифрами хочу!!!')



