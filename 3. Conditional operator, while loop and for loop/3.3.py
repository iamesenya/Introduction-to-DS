a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if a >= b and a >= c:
    print("Наибольшее число:", a)
elif b >= a and b >= c:
    print("Наибольшее число:", b)
elif c >= a and c >= b:
    print("Наибольшее число:", c)
else:
    print("Ни одно из условий не выполнено")
