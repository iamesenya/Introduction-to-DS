import math

# Вводим длины сторон a и b
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))

# Рассчитываем гипотенузу треугольника
c = math.sqrt(a**2 + b**2)

# Рассчитываем sin(), cos() и tg() для угла alpha (первый острый угол)
sin_alpha = a / c
cos_alpha = b / c
tan_alpha = a / b

# Рассчитываем sin(), cos() и tg() для угла beta (второй острый угол)
sin_beta = b / c
cos_beta = a / c
tan_beta = b / a

# Выводим результаты
print("Гипотенуза треугольника:", c)
print("Значения для угла alpha (первый острый угол):")
print("sin(alpha):", sin_alpha)
print("cos(alpha):", cos_alpha)
print("tan(alpha):", tan_alpha)
print("Значения для угла beta (второй острый угол):")
print("sin(beta):", sin_beta)
print("cos(beta):", cos_beta)
print("tan(beta):", tan_beta)
