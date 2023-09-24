s = "There is no time like the present"

# Находим количество букв "e" в строке и возводим это число в квадрат
count_e = s.count('e')
squared_count_e = pow(count_e, 2)

# Находим количество пробелов в строке и возводим это число в квадрат
count_space = s.count(' ')
squared_count_space = pow(count_space, 2)

# Рассчитываем разницу двух полученных чисел
difference = squared_count_e - squared_count_space

print("Разница:", difference)
