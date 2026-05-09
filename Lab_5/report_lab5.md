# Лабораторная работа №5
## Тема: Классы и объекты в Python. Соблюдение принципов инкапсуляции и наследования.
**Дисциплина:** Python для приложений  
**Студент:** Петровская Арина  
**Группа:** IA2504  
**Преподаватель:** Борш Д.  
**Год:** 2026  

---

### Выполнение лабораторной работы
Перед выполнением создаем новую директорию `Lab_5`, в которой будет храниться содержание пятой лабораторной работы.  
В директории `Lab_5` создаем нужные папки и файлы (рис. 1).  
##### **Лабораторная работа имеет следующую структуру:**
- файлы `employee.py`, `main.py` (файлы со скриптами)
- файл `report_lab5.md` (оформление отчета лабораторной работы).
- текстовый файл `user.txt`, который создается автоматически у пользователя пустым для реализации второй задачи.
1. Создаем класс `Employee`, который является родительским классом. Содержит:
- приватные переменные (`nameEmployee`, `phone`, `bday`, `email`, `position`);  
- методы (`calculateAge()` – публичный (`pass`), `calculateSalary()` – защищенный)  
В каждом из классов создаем геттеры и сеттеры.
- getter — получает значение поля
- setter — изменяет значение поля (с проверкой)  
Объявить их можно двумя способами
-  Используя предопределенную функцию `property()`
```python
def set_number_of_hour(self, value):
    self.__number_of_hour = value

def get_number_of_hour(self):
    return self.__number_of_hour
```  
- Используя декораторы(рекомендуемый способ)
```python
@property
def name_employee(self):
    return self.__name_employee

@name_employee.setter
def name_employee(self, value):
    self.__name_employee = value
```  
Для метода «calculateSalary», в классе «HourlyEmployee», переопределите его –
подсчитав зарплату как количество проработанных часов, умноженных на оплату за
час, а для дочернего-класса ”SalaryEmployee” – как фиксированная месячная
зарплата, на основе контракта.
2. Объявляем два класса наследника
- `HourlyEmployee` (`nmbrOfHour`, `hourlyPay`);  
- `SalaryEmployee` (`salary`)  
Для обращения к методам родительского класса используется функция `super()`.  
Для метода `calculateSalary`, в классе `HourlyEmployee`, переопределяем его
подсчитав зарплату как количество проработанных часов, умноженных на оплату за
час.  
```python
def _calculate_salary(self):
    return self.__number_of_hour * self.__hourly_pay
```
Для дочернего-класса `SalaryEmployee` – как фиксированная месячная зарплата, на основе контракта.
```python
 def _calculate_salary(self):
        return self.__salary
```  
В отдельной функции в файле `main.py` создаем 6 объектов на основе определенных классов – по 2 каждого типа. 
```python
def main():
    employees = []

    for i in range(2):
        employees.append(new_employee())

    for i in range(2):
        employees.append(new_hourly_employee())

    for i in range(2):
        employees.append(new_salary_employee())
```  
Также работаем с регулярными выражениями, используя модуль `re`  
`NAME_PATTERN = r"^[A-Za-zА-Яа-я]+$"` - для имени сотрудника  
`PHONE_PATTERN = r"^\+373\d{8}$"` – для номера телефона  
Для даты дня рождения:
```
BIRTHDAY_PATTERN = (
    r"^(0[1-9]|[12][0-9]|3[01])\."
    r"(0[1-9]|1[0-2])\."
    r"(19[6-9][0-9]|200[0-7])$"
)
```  
Для указания почтового адреса:
```
EMAIL_PATTERN = (
    r"^[A-Za-z0-9]([._-]?[A-Za-z0-9]){1,19}"
    r"@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$"
)
```  
`POSITION_PATTERN = r"^[A-Za-zА-Яа-я]{2,20}(?: [A-Za-zА-Яа-я]{2,20})*$"` - для должности  
❗Все данные можно ввести как на русском, так и на английском языках.  
Далее проверяем через функцию правильность введенных данных  
```python
def input_with_validation(message, pattern):
    while True:
        value = input(message)

        if re.fullmatch(pattern, value):
            return value
        else:
            print("Неверный формат. Попробуйте снова.")
```  
Создаем 3 списка, где будут находиться зарплаты в зависимости от типа найма. Перебираем список из `employees = []`
```python
employee_salaries = []
hourly_salaries = []
salary_salaries = []

for emp in employees:
    s = emp.calculate_salary()
    if isinstance(emp, HourlyEmployee):
        hourly_salaries.append(s)
    elif isinstance(emp, SalaryEmployee):
        salary_salaries.append(s)
    elif isinstance(emp, Employee):
        employee_salaries.append(s)
```  
`isinstance()` - встроенная функция, которая проверяет, принадлежит ли объект указанному классу.
**Уровни доступа методов и атрибутов:**
- Public (по умолчанию). Обозначается `self.name = name`
- Protected (используются внутри класса наследников). Обозначается `self.name = _name`
- Private (используются только внутри класса). Обозначается `self.name = __name`  
### [Официальная документация для Python 3.14.3.](https://docs.python.org/3.14/)