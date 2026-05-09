import re

FILE = 'user.txt'

def user_name(name):
    pattern = r'^[А-Яа-яA-Za-z]{2,20}(-[А-Яа-я]{2,20})*$'
    return re.fullmatch(pattern, name)

def user_department(department):
    pattern = r'^[А-Яа-я0-9]+([А-Яа-я0-9]+)?$'
    return re.fullmatch(pattern, department)

def user_children(number):
    return number.isdigit() and 0 <= int(number) < 18

def input_data():
    while True:
        surname = input("Введите фамилию: ").strip()
        name = input("Введите имя: ").strip()
        department = input("Введите отдел: ").strip()
        children = input("Введите количество детей: ").strip()

        if not user_name(surname):
            print("Ошибка в фамилии!")
            continue

        if not user_name(name):
            print("Ошибка в имени!")
            continue

        if not user_department(department):
            print("Ошибка в отделе!")
            continue

        if not user_children(children):
            print("Ошибка в фамилии!")
            continue

        department = department.replace(" ", "_")

        with open(FILE, 'a', encoding='utf-8') as f:
            f.write(f"{surname}\t{name}\t{department}\t{children}\n")

        print("Данные успешно сохранены!")
        break

def show_data():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            all_children = 0

            for line in f:
                surname, name, department, children = line.strip().split('\t')

                print(f'{surname} {name} ({department}) - детей: {children}')
                all_children += int(children)

            print(f'\nОбщее количество детей: {all_children}')

    except FileNotFoundError:
        print('файл не найден')

def no_children():
    try:
        with open(FILE, 'r', encoding='utf-8') as f:
            print('\nСотрудники без детей')

            for line in f:
                surname, name, department, children = line.strip().split('\t')

                if int(children) == 0:
                    print(f'{surname} {name}')

    except FileNotFoundError:
        print('файл не найден')