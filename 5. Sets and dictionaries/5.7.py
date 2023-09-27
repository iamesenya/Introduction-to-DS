# Создаем словарь с названиями стран и столицами
countries_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Китай": "Пекин"
}

# Функция для поиска столицы по названию страны
def find_capital(country_name):
    if country_name in countries_capitals:
        return countries_capitals[country_name]
    else:
        return "Такой страны в словаре нет"

# Ввод названия страны от пользователя
country_to_find = input("Введите название страны: ")

# Поиск и вывод столицы
capital = find_capital(country_to_find)
print(capital)
