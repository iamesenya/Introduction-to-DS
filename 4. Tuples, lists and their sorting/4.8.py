import random

# Создаем список из 10 случайных целых чисел в диапазоне от 0 до 99
n = 10
random_numbers = [random.randint(0, 99) for _ in range(n)]

# Находим минимальный и максимальный элементы
min_index = random_numbers.index(min(random_numbers))
max_index = random_numbers.index(max(random_numbers))

# Меняем местами минимальный и максимальный элементы
random_numbers[min_index], random_numbers[max_index] = random_numbers[max_index], random_numbers[min_index]

# Выводим исходный список
print("Исходный список:", random_numbers)

# Создаем новый список
new_random_numbers = random_numbers.copy()

# Выводим новый список
print("Новый список:", new_random_numbers)
