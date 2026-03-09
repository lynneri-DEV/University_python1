import task_1_2 as f

print('Калькулятор идеального веса')

def main():
    age = f.get_age()
    height = f.get_height()
    gender = f.get_gender()
    weight = f.get_weight()

    ideal_weight = f.lorentz_formula(gender, height, age)

    print('Идеальный вес:', round(ideal_weight, 2), 'кг')

    difference = weight - ideal_weight

    if difference > 0:
        print("Ваш вес выше нормы. Рекомендуется снизить вес.")
    elif difference < 0:
        print("Ваш вес ниже нормы. Рекомендуется набрать вес.")
    else:
        print("Ваш вес идеальный!")


if __name__ == "__main__":
    main()
