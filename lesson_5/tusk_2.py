'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

i = 1

# узнаем что живет в файле.
with open("tusk_2.txt", "r", encoding="UTF-8") as my_file:
    content = my_file.readlines()
    line_number = len(content)
    print(f"Всего в файле {line_number} строк\n")

    # считаем колчичество слов. держать открытым файл нам больше незачем
for line in content:
    line = len(line.split())
    if line == 1:
        word = "cлово"
    elif line >1 and line < 5:
         word = "cлова"
    else:
        word = "слов"
    print(f"В строке {i} -- {line} {word}")
    i += 1

print("\n")
print("Все готово")