import math
# Задание 1: Объясните что было реализовано в следующем примере

greet_user = lambda name: print('Hello My Dear,', name)
user_name = input('What is your name? ')
greet_user(user_name)

# Задание 2: Отсортируйте список из 7 элементов-кортежей, состоящих соответственно из 2-х элементов,
# по второму элементу. Для решения поставленной задачи используйте функцию sorted(iterable, key=key, reverse=reverse)
# и создайте лямбда-выражение для 2-го параметра.
data = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 3), (9, 20)]
sorted_data = sorted(data, key=lambda x: x[1], reverse=False)
sorted_data_2 = sorted(data, key=lambda x: x[1], reverse=True)

print(sorted_data)
print(sorted_data_2)

# Задание 3
number = lambda x, y: print(math.pow(x, y))
number_1 = int(input ('Введите первое число: '))
number_2 = int(input ('Введите второе число: '))
number(number_1, number_2)

# Задание 4. Функции
# с параметрами
def number(x, y):
    pow_number = math.gcd(x, y)  # наибольший общий делитель
    return pow_number

# num_1 = int(input ('Введите первое число: '))
# num_2 = int(input ('Введите второе число: '))
# print('НОД:', number(num_1, num_2))

# без параметров
def get_name_1():
    return 'Меня зовут Арина'

print(get_name_1())

def get_name_2():
    print ('Меня зовут Арина')

get_name_2()

# с предопределенными параметрами
def draw_line(num=5, symbol='-'):
    print(symbol * num)

draw_line()

# Задание 5. Задача
def average_mark(test, laboratory, exam, individual):
    list_mark = [test, laboratory, exam, individual]
    avg_element = sum(list_mark) / len(list_mark)
    print('Ваш средний балл:', list_mark)
    for mark in list_mark:
        if not isinstance(mark, int) or mark < 1 or mark > 10:
            print ('Неверная оценка!')

    if avg_element >= 5:
        return 'Зачет'
    else:
        return 'Незачет'

test_num = int(input('Введите оценку за тест:'))
test_laboratory = int(input('Введите оценку за лабораторную:'))
test_exam = int(input('Введите оценку за экзамен:'))
test_individual = int(input('Введите оценку за индивидуальную работу:'))

print(average_mark(test_num, test_laboratory, test_exam, test_individual))
