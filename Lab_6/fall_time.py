import math


def get_height():
    while True:
        try:
            get_user_height = float(input("Введите высоту падения в метрах: "))

            if math.isnan(get_user_height):
                print("Введите корректное число: ")
                continue

            if get_user_height < 0:
                print("Введите положительное число: ")
                continue

            return get_user_height
        except ValueError:
            print("Введите число: ")


def calculate_fall_time(h):
    g = 9.8
    t = math.sqrt((2 * h) / g)

    return t

height = get_height()
time = calculate_fall_time(height)

print(f"\nВремя падения объекта: {time:.2f} секунд")