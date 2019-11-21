'''
 Узнайте у пользователя число n.
 Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
# запрашиваем число
while True:
    n = input("Введите желаемое число: ")
    if n.isdigit():
        break
    else:
        print("Надо цифрой, а не букавками : ")

# собираем наше условие
number_1 = int(n)
number_2 = int(n + n)
number_3 = int(n + n + n)

# считаем чего получилось
sum = number_1 + number_2 + number_3

# выводим результат
print(f'{number_1} + {number_2} + {number_3} = {sum}')