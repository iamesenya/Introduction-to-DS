# Функция для нахождения суммы двух чисел
def sum(a, b):
    return a + b

# Функция для нахождения разности двух чисел
def diff(a, b):
    return a - b

# Функция для нахождения произведения двух чисел
def comp(a, b):
    return a * b

# Функция для нахождения частного двух чисел
def div(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

# Ввод двух вещественных чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Вызываем каждую функцию и выводим результаты через пробел
result_sum = sum(a, b)
result_diff = diff(a, b)
result_comp = comp(a, b)
result_div = div(a, b)

print(f"{result_sum} {result_diff} {result_comp} {result_div}")
