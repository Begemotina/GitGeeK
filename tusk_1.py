# тест переменных без пользователя
hellow = "hellow World"
number_1 = 25
number_2 = 15
print(type(number_1))

a = "Мир"
b = "Дверь"
c = "Жвачка "

print(number_1 + number_2) #сложение переменных
print(hellow) # вывести текстовую строку
print(a + b + c) #конкатинация без пробелов
print(c*2) # а тут есть пробел

# тест переменных с пользователем
# просто фигня с именем и воздрастом
name = input("Как имя твое, дитя\n ")

while True:
    age = input("Сколько годиков тебе: ") # не буду делать проверку на "аброкатабру"
    if age.isdigit():
        break
    else:
        print("Циферкой надо ввести : ")

age = int(age)
if int age >= 18:
    print("Уже не дитя по имени " + name + " аж " + age + " годков")
elif int age <= 18:
    print("Дитя по имени " + name + "  аж " + age + " годков")
else:
    print("Что же вы тут такое вкорячили что пришли сюда?")

