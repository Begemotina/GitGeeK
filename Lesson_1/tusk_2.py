number=int(input("введите количество секунд : "))

# калькулятор
hours=number//3600
minutes= (number%3600)//60
seconds= (number%3600)%60

# выводим часы
print(f'{hours}:{minutes}:{seconds}')