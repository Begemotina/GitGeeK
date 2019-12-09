'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
#  подготовка
profit = {}
profit_average_dict = {}
prof = 0
prof_aver = 0
i = 0
# получаем данные. считам среднюю и делае
with open('tusk_7.txt', 'r', encoding="UTF-8") as my_file:
    for line in my_file:
        name, type, earning, loss = line.split()
        profit[name] = int(earning) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {round(prof_aver, 2)}')
    else:
        print(f'Прибыль средняя - нет такой. Все в минусе')
    profit_average_dict = {'средняя прибыль': round(prof_aver, 2)}
    profit.update(profit_average_dict)
    print(f'Прибыль каждой компании - {profit}')

# записываем файлик.
with open('tusk_7.json', 'w', encoding="UTF-8") as write_js:
    json.dump(profit, write_js)

    js_string = json.dumps(profit)
    print(f'Создан файл с расширением json.')