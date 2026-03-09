def ideal_weight(age, height, weight, gender):
    if height < 150 or height > 220:
        raise ValueError("Ошибка роста")
    if weight < 45 or weight > 300:
        raise ValueError("Ошибка веса")
    if age > 120 or age < 20:
        raise ValueError("Ошибка возраста")

    if gender.lower() not in ['м', 'ж']:
        raise ValueError("Возраст должен быть 'm' или 'f'")

    if gender == 'м':
        weight_f = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
        return weight_f
    else:
        weight_m = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
        return weight_m

user_age = int(input("Введите ваш возраст: "))
user_height = int(input("Введите ваш рост: "))
user_weight = int(input("Введите ваш вес: "))
user_gender = input("Введите гендер (м/ж): ")

result  = ideal_weight(user_age, user_height, user_weight, user_gender)
print(round(result, 2))
