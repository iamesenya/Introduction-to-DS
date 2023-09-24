s = input("Введите строку из натуральных чисел от 0 до 9: ")

# Заменяем числа 1, 3, 5 и 7 на соответствующие слова
s = s.replace('1', 'one')
s = s.replace('3', 'three')
s = s.replace('5', 'five')
s = s.replace('7', 'seven')

print("Результат:", s)
