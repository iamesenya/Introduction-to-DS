set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

# Объединение множеств
union_result = set1.union(set2)

# Пересечение множеств
intersection_result = set1.intersection(set2)

# Разность множеств (элементы, которые есть в set1, но нет в set2)
difference_result = set1.difference(set2)

# Симметричная разность множеств (элементы, которые есть только в одном из множеств)
symmetric_difference_result = set1.symmetric_difference(set2)

print("Объединение:", union_result)
print("Пересечение:", intersection_result)
print("Разность:", difference_result)
print("Симметричная разность:", symmetric_difference_result)
