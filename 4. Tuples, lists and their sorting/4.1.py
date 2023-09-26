n = int(input("Введите начальное значение (n): "))
k = int(input("Введите конечное значение (k): "))

# Создание кортежа с использованием функции range
my_tuple = tuple(range(n, k + 1))

# Инициализация переменных для суммы четных и нечетных элементов
total_even = 0
total_odd = 0

# Перебор элементов кортежа
for num in my_tuple:
    if num % 2 == 0:
        total_even += num
    else:
        total_odd += num

# Сравнение сумм и вывод результата
if total_even > total_odd:
    print(f"Сумма чётных элементов больше: total_even > total_odd")
elif total_odd > total_even:
    print(f"Сумма нечётных элементов больше: total_even < total_odd")
else:
    print("Сумма чётных и нечётных элементов равны: total_even == total_odd")
