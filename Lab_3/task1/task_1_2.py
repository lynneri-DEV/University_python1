def get_age():
    while True:
        try:
            age = int(input('Введите возраст: '))
            if 20 < age < 120:
                return age
            else:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')


def get_height():
    while True:
        try:
            height = int(input('Введите рост (см): '))
            if 150 < height < 220:
                return height
            else:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')


def get_weight():
    while True:
        try:
            weight = int(input('Введите вес (кг): '))
            if 45 < weight < 300:
                return weight
            else:
                raise ValueError
        except ValueError:
            print('Некорректный ввод')


def get_gender():
    while True:
        gender = input('Введите пол (M/F): ').upper()
        if gender in ['M', 'F']:
            return gender
        else:
            print('Введите только M или F')


def lorentz_formula(gender, height, age):
    if gender == 'M':
        ideal = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    else:
        ideal = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
    return ideal
