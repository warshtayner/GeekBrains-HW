# Задача 3 к уроку 1
# Реализовать склонение слова «процент» для чисел до 20
base = 'процент'

for i in range(1, 21):
    if 0 < i < 2:
        print(f'{i} - {base}')
    elif 1 < i < 5:
        print(f'{i} - {base}а')
    else:
        print(f'{i} - {base}ов')
