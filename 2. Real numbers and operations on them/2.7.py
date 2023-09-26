pressure_mmHg = float(input("Введите давление в мм рт.ст.: "))

# Преобразуем давление в Паскали
pressure_Pa = pressure_mmHg * 133.3

# Преобразуем Паскали в кПа
pressure_kPa = pressure_Pa / 1000

# Выводим результат с точностью до 3 знаков после запятой
print("Давление в кПа:", format(pressure_kPa, ".3f"))
