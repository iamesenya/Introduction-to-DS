import random

# Функция для броска одного кубика
def roll_die():
    return random.randint(1, 6)

# Функция для совместного броска двух кубиков n раз
def simulate_rolls(n):
    results = []
    for _ in range(n):
        total = roll_die() + roll_die()
        results.append(total)
    return results

# Функция для подсчёта частоты результатов
def count_frequency(results):
    frequency = {}
    for result in results:
        if result in frequency:
            frequency[result] += 1
        else:
            frequency[result] = 1
    return frequency

# Вызываем вторую функцию с указанным количеством бросков
num_rolls = 10  # Здесь можно указать любое количество бросков
rolls = simulate_rolls(num_rolls)

# Подсчитываем частоту результатов
frequency = count_frequency(rolls)

# Сортируем словарь по убыванию и выводим три наиболее часто встречающихся числа
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
top_three = sorted_frequency[:3]

print("Результаты бросков:", rolls)
print("Частота результатов:")
for result, count in top_three:
    print(f"{result}: {count} раз")
