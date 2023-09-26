n = int(input("Введите натуральное число n: "))

factorial = 1
i = 1

# Вычисляем факториал числа n
while i <= n:
    factorial *= i
    i += 1

print(f"Факториал числа {n} равен {factorial}")
