def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Введите целое число: "))

# Вызов функции для вычисления факториала и вывод результата
print(f"{n}! = {factorial(n)}")
