# Исходный список
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Создаем новый список для хранения результатов
new_list = []

# Проходим по каждому вложенному списку
for sublist in mylist:
    # Считаем сумму трех элементов во вложенном списке
    total = sum(sublist)
    # Считаем произведение трех элементов во вложенном списке
    product = sublist[0] * sublist[1] * sublist[2]
    # Создаем новый список из суммы и произведения
    new_sublist = sublist + [total, product]
    # Добавляем новый список в новый список результатов
    new_list.append(new_sublist)

for sublist in new_list:
    print(sublist)
