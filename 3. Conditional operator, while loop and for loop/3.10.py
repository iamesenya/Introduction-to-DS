# Инициализируем переменную для хранения максимального числа
max_number = None

while True:
    num = float(input("Введите число (или 0 для завершения): "))

    # Проверяем, равно ли введенное число 0
    if num == 0:
        break  # Выходим из цикла, если число равно 0

    # Проверяем, является ли текущее число максимальным
    if max_number is None or num > max_number:
        max_number = num

if max_number is not None:
    print(f"Максимальное введенное число: {max_number}")
else:
    print("Вы не ввели ни одного числа.")
