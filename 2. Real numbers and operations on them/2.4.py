import math

# Вводим цену товара в рублях и копейках
price = float(input("Введите цену товара в рублях и копейках (например, 10.50): "))

# Вводим количество единиц товара
k = int(input("Введите количество единиц товара: "))

# Разделяем цену на рубли и копейки
rub = int(price)
kop = round((price - rub) * 100)  # Округляем копейки до целого числа

# Рассчитываем общую стоимость в копейках
total_cost_in_kopecks = (rub * 100 + kop) * k

# Рассчитываем количество рублей и копеек в общей стоимости
total_rubles = total_cost_in_kopecks // 100
total_kopecks = total_cost_in_kopecks % 100

print("Стоимость покупки:")
print("Рубли:", total_rubles)
print("Копейки:", total_kopecks)


