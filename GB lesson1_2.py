# Задача 2 к уроку 1
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000...

# Создать список
cube_list = [i**3 for i in range(1, 1001, 2)]

# накопители
total_sum = 0
total_sum2 = 0

# Сумма всех чисел с учетом условий 2.а
for i in cube_list:
    i2 = i
    sum_num = 0
    while i2 != 0:
        sum_num += i2 % 10
        i2 //= 10
    if sum_num % 7 == 0:
        total_sum += i

# Сумма всех чисел с учетом условий 2.b и 2.c
for i in cube_list:
    i2 = i + 17
    i3 = i + 17
    sum_num = 0
    while i2 != 0:
        sum_num += i2 % 10
        i2 //= 10
    if sum_num % 7 == 0:
        total_sum2 += i3

# Вывод
print(total_sum)
print(total_sum2)
