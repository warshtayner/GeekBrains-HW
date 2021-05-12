# Задача 1 к уроку 1
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

# Запрос данных у пользователя
duration_time = int(input('Введите время в секундах: '))

# Тело программы
week = duration_time // 604800
day = (duration_time // 86400) % 7
hours = (duration_time // 3600) % 24
minutes = (duration_time // 60) % 60
seconds = duration_time % 60

# Ввывод результата
if week != 0:
    print(f'{week} н, {day} дн, {hours} час, {minutes} мин, {seconds} сек.')
elif day != 0:
    print(f'{day} дн, {hours} час, {minutes} мин, {seconds} сек.')
elif hours != 0:
    print(f'{hours} час, {minutes} мин, {seconds} сек.')
elif minutes != 0:
    print(f'{minutes} мин, {seconds} сек.')
else:
    print(f'{seconds} сек.')

