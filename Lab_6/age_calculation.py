import re
import datetime
import calendar


def user_birthday():
    pattern = r"^(?:\d{2}-\d{2}-\d{4}|\d{2}\.\d{2}\.\d{4})$"
    while True:
        birthday = input("Enter your birthday: ").strip()

        if not re.fullmatch(pattern, birthday):
            print("Invalid format birthday")
            continue

        birthday = birthday.replace(".", "-")
        day, month, year = map(int, birthday.split("-"))

        if month < 1 or month > 12:
            print("Invalid month")
            continue

        max_days = calendar.monthrange(year, month)[1]

        if day > max_days:
            print("Invalid day")
            continue

        return datetime.date(year, month, day)

def lived_days(human_birthday):
    today = datetime.date.today()

    if human_birthday > today:
        print("Invalid birthday")
        return

    human_lived_days = (today - human_birthday).days
    print("Lived days: ", human_lived_days)


result = user_birthday()
lived_days(result)
