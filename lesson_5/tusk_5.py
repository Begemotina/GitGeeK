'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

# Делаем список который будет суваться в файл
my_list = input("Введите числа через пробел\n").split()

with open("tusk_5.txt", "w", encoding="UTF-8") as my_file:
    # ох какого я крокодила придумал что бы список засунуть в файл. Не хочу использовать print(*my_list) уже было
    my_file.writelines(' '.join(map(str, my_list)))
with open("tusk_5.txt", "r", encoding="UTF-8") as my_file:
    content = my_file.readline().split()
    print(content)
# посчтаем сумму того что получили из файла
summ = 0
try:
    for i in content:
        summ = summ + float(i)
except ValueError:
    print("Ошибка данных.")
    summ = summ + float(input("Ведите верное число, если не знаете его введите 0\n"))
print(summ)