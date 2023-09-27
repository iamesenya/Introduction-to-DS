# Исходный словарь с начальными значениями
animal_dict = {
    "dog": "собака",
    "cat": "кошка",
    "rabbit": "кролик"
}

while True:
    new_key = input("Введите название животного на английском (или 'STOP' для завершения): ")

    if new_key == 'STOP':
        break

    new_value = input("Введите название животного на русском: ")

    # Добавляем новую пару ключ-значение в словарь
    animal_dict[new_key] = new_value

print("Полученный словарь:")
for key, value in animal_dict.items():
    print(f"{key}: {value}")
