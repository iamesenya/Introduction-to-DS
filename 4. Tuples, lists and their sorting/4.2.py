str1 = input("Введите первую строку чисел: ")
str2 = input("Введите вторую строку чисел: ")

tuple1 = tuple(map(int, str1.split()))
tuple2 = tuple(map(int, str2.split()))

# Находим максимальное и минимальное значение для каждого кортежа
max_value1 = max(tuple1)
min_value1 = min(tuple1)

max_value2 = max(tuple2)
min_value2 = min(tuple2)

# Рассчитываем разницу между максимальным и минимальным значениями для каждого кортежа
diff1 = max_value1 - min_value1
diff2 = max_value2 - min_value2

print(f"Максимальное значение в первом кортеже: {max_value1}")
print(f"Минимальное значение в первом кортеже: {min_value1}")
print(f"Разница в первом кортеже: {diff1}")

print(f"Максимальное значение во втором кортеже: {max_value2}")
print(f"Минимальное значение во втором кортеже: {min_value2}")
print(f"Разница во втором кортеже: {diff2}")
