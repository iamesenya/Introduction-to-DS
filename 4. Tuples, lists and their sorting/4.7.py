import random
import math

# Создаем список из случайных целых чисел в диапазоне от 0 до 100
n = 10  # Количество элементов в списке
random_numbers = [random.randint(0, 100) for _ in range(n)]

# Рассчитываем среднее значение
mean = sum(random_numbers) / n

# Рассчитываем дисперсию
variance = sum((x - mean) ** 2 for x in random_numbers) / n

# Рассчитываем стандартное отклонение
std_deviation = math.sqrt(variance)

print("Список случайных чисел:", random_numbers)
print("Среднее значение:", mean)
print("Дисперсия:", variance)
print("Стандартное отклонение:", std_deviation)
