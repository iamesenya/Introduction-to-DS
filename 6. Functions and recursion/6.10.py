films = [
 ['Назад в будущее', 1985, 8.6, 116, ['фант.', 'комедия'], 19.0, 381.1],
 ['Назад в будущее 2', 1989, 8.3, 108, ['фант.', 'прикл.'], 40.0, 331.9],
 ['Малыш', 1921, 8.2, 68, ['драма', 'комедия'], 0.25, 5.45],
 ['Один дома', 1990, 8.2, 103, ['семейный', 'комедия'], 18.0, 476.68],
 ['Один дома 2', 1992, 7.9, 119, ['семейный', 'комедия'], 18.0, 358.9],
 ['Большой', 1988, 7.9, 104, ['фэнтези', 'мелодрама'], 18.0, 151.6],
 ['Рыжий пёс', 2011, 7.7, 92, ['мелодрама', 'комедия'], 8.5, 21.18],
 ['Марли и я', 2008, 7.8, 115, ['драма', 'комедия'], 60.0, 255.7],
 ['Миссис Даутфайр', 1993, 7.7, 125, ['драма', 'комедия'], 25.0, 441.28],
 ['Кудряшка Сью', 1991, 7.6, 101, ['семейный', 'комедия'], 25.0, 33.6]
]
# Сортировка данных по годам (в убывающем порядке)
films.sort(key=lambda x: x[1], reverse=True)

# Вывод заголовка таблицы
print('Название фильма | Год | Рейтинг | Длина | Бюджет | Сборы |')
print('--------------------------------------------------------------------')

# Вывод отсортированной таблицы
for row in films:
    print('{: <35} | {} | {: >7.2f} | {: >5} | {: >6.1f} | {: >6.1f} |'.format(
        row[0], row[1], row[2], row[3], row[5], row[6]))

def column_total(films, column, start_year, end_year):
    total = 0
    for film in films:
        year = film[1]
        if start_year <= year <= end_year:
            total += film[column]
    return total

# Пример использования функции для рассчёта суммы бюджетов фильмов с 1980 по 1990 годы
start_year = 1980
end_year = 1990
budget_total = column_total(films, 5, start_year, end_year)
print(f"Сумма бюджетов за {start_year}-{end_year}: {budget_total:.1f}")

def column_mean(films, column, start_year, end_year):
    total = column_total(films, column, start_year, end_year)
    count = sum(1 for film in films if start_year <= film[1] <= end_year)
    return total / count if count > 0 else 0

# Пример использования функции для рассчёта среднего бюджета фильмов с 1980 по 1990 годы
start_year = 1980
end_year = 1990
budget_mean = column_mean(films, 5, start_year, end_year)
print(f"Средний бюджет за {start_year}-{end_year}: {budget_mean:.1f}")

def cost_per_minute(films):
    new_films = []
    for film in films:
        budget = film[5]
        length = film[3]
        cost_per_minute = budget / length if length > 0 else 0
        new_film = film + [cost_per_minute]
        new_films.append(new_film)
    return new_films

# Получение нового списка с стоимостью одной минуты
new_films = cost_per_minute(films)

# Сортировка нового списка по стоимости одной минуты
new_films.sort(key=lambda x: x[-1], reverse=True)

# Вывод заголовка новой таблицы
print('Название фильма | Год | Рейтинг | Длина | Бюджет | Сборы | Стоимость 1 минуты |')
print('-----------------------------------------------------------------------------------------------')

# Вывод отсортированной новой таблицы
for row in new_films:
    print('{: <35} | {} | {: >7.2f} | {: >5} | {: >6.1f} | {: >6.1f} | {: >17.2f} |'.format(
        row[0], row[1], row[2], row[3], row[5], row[6], row[7]))

