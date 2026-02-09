# Задание 1
#3. Функции print() и input()
"""
пункт 3.
Функции print() и input()
"""

print('Привет, меня зовут Арина!')
name = input('Введите ваше имя: ')
print('Привет,', name)

#5. Определяем переменные
number_first = 3 # числовое целое значение
number_second = 2.4 # вещественное значение
text_value_1 = 'Здесь должен быть текст' # короткое текстовое значение
text_value_2 = ('Здесь должен быть '
                'многострочный текст'
                'с информацией') # текстовое значение, занимающее несколько строк

#6. Выводим тип переменных
print (type(number_second))
print (type(text_value_1))

#7. Выводим длину переменной
print (len(text_value_2))

#8. Приводим все буквы к верхнему регистру
print (text_value_1.upper())

#9. Срез
substring = text_value_2[0:6]
print(substring)

#11. Вывод на экран
age = 21
city = 'Кишинев'

print(f'Мне {age} год')
print('Мне {} год. Я живу в городе {}'.format(age, city))

# Задание 2
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip())

txt = "More results from text..."
print(txt.split())

age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))

# Изменяем тип данных
new_age = str(age)
print("Число: " + new_age)
