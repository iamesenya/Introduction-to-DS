import random

# Создаем список из 30 случайных целых чисел в диапазоне от 0 до 99
n = 30
random_numbers = [random.randint(0, 99) for _ in range(n)]

# Находим индекс максимального элемента
max_index = 0  # Индекс максимального элемента изначально равен 0

# Ищем максимальный элемент и его индекс
for i in range(1, n):
    if random_numbers[i] > random_numbers[max_index]:
        max_index = i

# Сортируем список так, чтобы максимальный элемент был первым
random_numbers[0], random_numbers[max_index] = random_numbers[max_index], random_numbers[0]

# Выводим максимальное значение
print("Максимальное значение:", random_numbers[0])
