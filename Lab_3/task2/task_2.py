def get_age():
    while True:
        answer = input("Кошке меньше года? (Да/Нет): ").lower()
        if answer in ["да"]:
            return True
        elif answer in ["нет"]:
            return False
        else:
            print("Введите Да/Нет")


def get_month():
    while True:
        try:
            month = int(input("Введите возраст кошки в месяцах (1-11): "))
            if 1 <= month <= 11:
                return month
            else:
                print("Введите число от 1 до 11")
        except ValueError:
            print("Введите число")


def get_year():
    while True:
        try:
            year = int(input("Введите возраст кошки в годах (1-35): "))
            if 1 <= year <= 35:
                return year
            else:
                print("Введите число от 1 до 35")
        except ValueError:
            print("Введите число")


def months_to_human(month):
    cat_dict = {
        1: "6 месяцев",
        2: "10 месяцев",
        3: "2 года",
        4: "5 лет",
        5: "8 лет",
        6: "14 лет",
        7: "15 лет",
        8: "16 лет",
        9: "16 лет",
        10: "17 лет",
        11: "17 лет"
    }

    return cat_dict[month]


def years_to_human(year):
    if year == 1:
        return 18
    elif year == 2:
        return 25
    elif 3 <= year <= 15:
        return 25 + (year - 2) * 4
    else:
        return 25 + (13 * 4) + (year - 15) * 3
