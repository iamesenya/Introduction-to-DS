fruits = ("яблоко", "банан", "апельсин", "груша", "мандарин")
kolv = (5, 8, 3, 5, 10)

fruit_name = input("Введите название фрукта: ")

# Ищем индекс фрукта в первом кортеже
try:
    index = fruits.index(fruit_name)
    if index >= 0 and index < len(kolv):
        quantity = kolv[index]
        print(f"Количество {fruit_name}: {quantity}")
    else:
        print("Фрукт не найден во втором кортеже.")
except ValueError:
    print("Фрукт не найден в первом кортеже.")
