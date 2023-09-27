numbers = [2, 3, 5, 7, 11, 13, 666, 19, 23, 299]

# Используем filter() и lambda для фильтрации элементов
filtered_numbers = list(filter(lambda x: x > 3, numbers))

print(filtered_numbers)
