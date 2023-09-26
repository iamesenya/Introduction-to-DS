# Вводим исходную сумму вклада и желаемую прибыль
initial_deposit = float(input("Введите исходную сумму вклада (в рублях): "))
desired_profit = 0.25 * initial_deposit  # 25% от исходной суммы

# Вводим процент годовых
annual_interest_rate = 0.10  # 10% годовых

# Инициализируем переменную для подсчета дней
days = 0

# Рассчитываем, через сколько дней получим желаемую прибыль
while initial_deposit < initial_deposit + desired_profit:
    daily_interest = initial_deposit * annual_interest_rate / 365
    initial_deposit += daily_interest
    days += 1

print(f"Через {days} дней после открытия вклада вы получите прибыль в размере 25% от исходной суммы.")

