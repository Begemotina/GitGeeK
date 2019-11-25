'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# узнаем месяц
while True:
    user_number = (input("Введите число от 1 до 12\n"))
    if user_number.isdigit() :
        user_number = int(user_number)
        if user_number != 0 and user_number < 13:
            break
        else:
            print("Ну от 1 до 12 ")
    else:
        print("Надо цифрой, а не букавками : ")



# определяем какой у нас сезон
# оставил вот так  просто потому что так так читать проще как мне кажется
if user_number == 1 or user_number == 2 or user_number == 12:
    season = 0
if user_number == 3 or user_number == 4 or user_number == 5:
    season = 1
if user_number == 6 or user_number == 7 or user_number == 8:
    season = 2
if user_number == 9 or user_number == 10 or user_number == 11:
    season = 3

# решение с помощью списка
season_list = ["зима", "весна", "лето", "осень"]
print(" Вывод с помощью списка: Время года - ", season_list[season])

# решение с помощью словаря. Ключи начинаются с 0, иначе предется делать еще кучу веток if
season_dict = {
    0 : "зима",
    1 : "весна",
    2 : "лето",
    3 : "осень",
}

print(" Вывод с помощью словаря: Время года - ", season_dict.get(season))