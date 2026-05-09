import calendar
import re


def get_date():
    pattern = r"^(\d{2})([-.])(\d{2})\2(\d{4})$"

    while True:
        date_input = input("Введите дату: ")

        match = re.match(pattern, date_input)
        if not match:
            print("Неверный формат")
            continue

        get_day = int(match.group(1))
        get_month = int(match.group(3))
        get_year = int(match.group(4))

        try:
            calendar.weekday(get_year, get_month, get_day)
            return get_year, get_month, get_day
        except ValueError:
            print("Неверный формат")

def get_weekday(get_year, get_month, get_day):
    user_weekday = calendar.weekday(get_year, get_month, get_day)

    days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]

    return days[user_weekday]

year, month, day = get_date()
weekday = get_weekday(year, month, day)
print(f"\nДата {day:02d}-{month:02d}-{year} приходится на: {weekday}")