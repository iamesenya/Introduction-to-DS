# Создаем словарь с названиями стран и столицами
countries_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Китай": "Пекин"
}

# Первый цикл: вывод построчно "Столицей country является capital."
print("Первый цикл:")
for country, capital in countries_capitals.items():
    print(f"Столицей {country} является {capital}.")

# Второй цикл: вывод пар ключ-значение с помощью метода items()
print("\nВторой цикл:")
for item in countries_capitals.items():
    print(item)

# Третий цикл: вывод ключей словаря с помощью метода keys()
print("\nТретий цикл:")
for country in countries_capitals.keys():
    print(country)

# Четвертый цикл: вывод значений словаря с помощью метода values()
print("\nЧетвертый цикл:")
for capital in countries_capitals.values():
    print(capital)
