import math

# Вводим координаты вектора a
X1 = float(input("Введите координату X1 вектора a: "))
Y1 = float(input("Введите координату Y1 вектора a: "))
Z1 = float(input("Введите координату Z1 вектора a: "))

# Вводим координаты вектора b
X2 = float(input("Введите координату X2 вектора b: "))
Y2 = float(input("Введите координату Y2 вектора b: "))
Z2 = float(input("Введите координату Z2 вектора b: "))

# Вычисляем скалярное произведение векторов
scalar_product = X1 * X2 + Y1 * Y2 + Z1 * Z2

# Вычисляем длины векторов
length_a = math.sqrt(X1**2 + Y1**2 + Z1**2)
length_b = math.sqrt(X2**2 + Y2**2 + Z2**2)

# Вычисляем угол между векторами (в радианах)
cos_phi = scalar_product / (length_a * length_b)
angle_phi = math.acos(cos_phi)

# Вычисляем векторное произведение векторов
vector_product = [
    Y1 * Z2 - Z1 * Y2,
    Z1 * X2 - X1 * Z2,
    X1 * Y2 - Y1 * X2
]

print("Скалярное произведение:", scalar_product)
print("Угол между векторами в радианах:", angle_phi)
print("Векторное произведение:", vector_product)

