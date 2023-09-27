numbers = [2, 13, 5, 7, 111, 13, 17, 999, 23, 88]

# Используем map() и lambda для нахождения квадрата каждого элемента
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Вывод результата
print(squared_numbers)
