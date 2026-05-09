import re


def check_phone():

    pattern = r'^(?:\+373[6-7][0,7-9]\d{6}|00373[6-7][0,7-9]\d{6}|0[6-7][0,7-9]\d{6}|[6-7][0,7-9]\d{6})$'
    # []

    while True:
        try:
            phone = input("Введите номер телефона: ").strip()

            if not phone:
                raise Exception("Пустой ввод!")

            if re.fullmatch(pattern, phone):
                print(f"Номер {phone} введён корректно")
                break

            else:
                raise Exception('Неверный формат номера. Попробуйте снова.')

        except Exception as e:
            print(f"Ошибка ввода: {e}")
            print("Попробуйте ещё раз.\n")


check_phone()
