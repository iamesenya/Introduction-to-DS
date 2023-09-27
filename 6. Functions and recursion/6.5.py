def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Введите целое число: "))

# Вызов функции для вычисления факториала и вывод результата
print(f"{n}! = {factorial(n)}")
