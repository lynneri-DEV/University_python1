import task_2 as f

print("Калькулятор возраста кошки")

def main():
    if f.get_age():
        month = f.get_month()
        human_age = f.months_to_human(month)
        print("Возраст кошки в человеческих годах:", human_age)

    else:
        year = f.get_year()
        human_age = f.years_to_human(year)
        print("Возраст кошки примерно", human_age, "человеческих лет")


if __name__ == "__main__":
    main()
