'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

"""
Я решил упроться
"""

key_list = []
value_list =[]
my_dict = {}

# вытаскиваем данные из файлика и делаем два списка
with open("tusk_6.txt", "r", encoding="UTF-8") as my_file:
    for line in my_file:
        line = line.split()
        r = 0
        for i in line:
            i= i.split("(")
            try:
                i.pop(1)
            except IndexError:
                r += 1
                continue
            line.pop(r)
            i
            line.insert(r, i)
            r += 1
        key = line.pop(0)
        key_list.append(key)
        value_list.append(line)

# вытаскиеваем лист из листа
for item in value_list:
    summ = 0
    for i in range(0, len(item)):
        pop = item[i]
        n = pop[0]
        summ = summ + int(n)
    item.clear()
    item.append(summ)

i = 0
# еще разочек разворачиваем список.
for item in value_list:
    key = item[0]
    value_list[i] = key
    i += 1

# я совсем запутался, с этими словаарями. буду делать циклом
i = 0
for key in key_list:
    item = {key: value_list[i]}
    my_dict.update(item)
    i += 1
# Вывести словарь на экран
print(my_dict)









