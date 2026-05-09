# СПИСКИ
# создаем список и выводим 1 и 3 значения
list_1 = [34, 46, 7, 75, 8, 0, 23]
print(list_1[0], list_1[2])

# замена элемента
list_1[1] = 100
print(list_1[1])

print(list_1[::-1])

# применяем метод
list_1.append(666)
print('!!!!', list_1)

# применяем функции
maximum = max(list_1)
minimum = min(list_1)

print(maximum, minimum)

# операторы
print(list_1 * 2)
print(666 in list_1)
print(list_1 == [2, 27, 4094, 746])

# КОРТЕЖИ
tuple_1 = (34, 'a', 7, 'I', 8, 'w', 23)
print(type(tuple_1))
# операторы выводим первый и последний элемент
print(tuple_1[0], tuple_1[-1])
# срез
print(tuple_1[2::-2])
# применение функций
new_list = list(tuple_1)
print('Список из кортежа:', new_list)
new_set = set(tuple_1)
print('Множество:', new_set)
new = 34 not in tuple_1
print(new)

# МНОЖЕСТВО
set_1 = {1, 45, 76, 34, 1, 46, 1, 8}
print(set_1)

set_1.add(100)
print(set_1)

print(len(set_1))

# СЛОВАРИ
dict_num = {
    10: 'математика',
    9: 'география',
    8: 'информатика'
}

dict_str = {
    'Кишинев': 'столица Молдовы',
    'Дублин': 'столица Ирландии',
    'Осло': 'столица Норвегии'
}

print(dict_num[8])
print(dict_str['Дублин'])

print(dict_str.keys())
print(dict_str.values())

age_value = dict_str.pop("Осло")
print("Удалено:", age_value)

print(len(dict_num))
print(type(dict_num))

list_num = [344, 500, 765]
list_str = ['магний', 'кальций', 'натрий']

# способ 1
info1 = "Товар: {}, Цена: {} руб.".format(list_str[0], list_num[0])
info2 = "Товар: {}, Цена: {} руб.".format(list_str[1], list_num[1])
info3 = "Товар: {}, Цена: {} руб.".format(list_str[2], list_num[2])

print(info1)
print(info2)
print(info3)

# способ 2
for i in range(len(list_num)):
    print('{}: {}'.format(list_str[i], list_num[i]))

age = int(input('Введите ваш возраст '))
new_age = age + 5

print(f'Через 5 лет вам будет: {new_age}')
