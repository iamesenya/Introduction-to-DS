n = int(input("Введите целую часть стоимости одного яблока (рубли): "))
m = int(input("Введите дробную часть стоимости одного яблока (копейки): "))

# Вводим количество яблок
N = int(input("Введите количество яблок: "))

# Проверяем, что введенные значения корректны
if n >= 0 and m >= 0 and N >= 0:
    # Вычисляем общую стоимость в копейках
    total_cost_in_kopecks = (n * 100 + m) * N

    # Рассчитываем количество рублей и копеек
    rubles = total_cost_in_kopecks // 100
    kopecks = total_cost_in_kopecks % 100

    # Выводим результат
    if rubles == 1:
        rubles_str = "рубль"
    elif rubles in [2, 3, 4]:
        rubles_str = "рубля"
    else:
        rubles_str = "рублей"

    if kopecks == 1:
        kopecks_str = "копейка"
    elif kopecks in [2, 3, 4]:
        kopecks_str = "копейки"
    else:
        kopecks_str = "копеек"

    print(f"Нужно заплатить {rubles} {rubles_str} и {kopecks} {kopecks_str}")
else:
    print("Введите корректные значения.")
