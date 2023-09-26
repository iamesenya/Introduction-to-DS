# Заданная строка
s = "Better late than never"

# Инициализируем переменные для подсчета букв "e" и пробелов
count_e = 0
count_space = 0

# Проходим по каждому символу строки
for char in s:
    if char == "e":
        count_e += 1
    elif char == " ":
        count_space += 1

# Вычисляем квадраты
e_squared = pow(count_e, 2)
space_squared = pow(count_space, 2)

# Рассчитываем разницу
difference = e_squared - space_squared

print("Количество 'e' в квадрате:", e_squared)
print("Количество пробелов в квадрате:", space_squared)
print("Разница:", difference)
