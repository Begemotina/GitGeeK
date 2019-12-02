'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def my_sum_function(ferst_el, el ):
    '''
    :param ferst_el: предидущий элемент
    :param el:  текущий элемент
    :return: сумма двух элементов
    '''
    return ferst_el * el

print(reduce(my_sum_function, [el for el in range(100, 1001) if el % 2 == 0]))

