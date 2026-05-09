import re
from Lab_5.employee import Employee, HourlyEmployee, SalaryEmployee

NAME_PATTERN = r"^[A-Za-zА-Яа-я]+$"
PHONE_PATTERN = r"^\+373\d{8}$"

BIRTHDAY_PATTERN = (
    r"^(0[1-9]|[12][0-9]|3[01])\."
    r"(0[1-9]|1[0-2])\."
    r"(19[6-9][0-9]|200[0-7])$"
)

EMAIL_PATTERN = (
    r"^[A-Za-z0-9]([._-]?[A-Za-z0-9]){1,19}"
    r"@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$"
)

POSITION_PATTERN = r"^[A-Za-zА-Яа-я]{2,20}(?: [A-Za-zА-Яа-я]{2,20})*$"

def input_with_validation(message, pattern):
    while True:
        value = input(message)

        if re.fullmatch(pattern, value):
            return value
        else:
            print("Неверный формат. Попробуйте снова.")

def new_employee():
    print('\nВведите данные Employee:')

    emp = Employee("", "", "", "", "")

    emp.name_employee = input_with_validation('Имя: ', NAME_PATTERN)
    emp.phone = input_with_validation('Телефон (+373XXXXXXXX): ', PHONE_PATTERN)
    emp.birthday = input_with_validation('Дата рождения (дд.мм.гггг): ', BIRTHDAY_PATTERN)
    emp.email = input_with_validation('Эл.почта: ', EMAIL_PATTERN)
    emp.position = input_with_validation('Должность: ', POSITION_PATTERN)

    return emp

# HourlyEmployee
def new_hourly_employee():
    print('\nВведите данные HourlyEmployee:')

    emp = HourlyEmployee("", "", "", "", "", 0, 0)

    emp.name_employee = input_with_validation('Имя: ', NAME_PATTERN)
    emp.phone = input_with_validation('Телефон: ', PHONE_PATTERN)
    emp.birthday = input_with_validation('Дата рождения: ', BIRTHDAY_PATTERN)
    emp.email = input_with_validation('Эл.почта: ', EMAIL_PATTERN)
    emp.position = input_with_validation('Должность: ', POSITION_PATTERN)

    emp.set_number_of_hour(float(input('Кол-во часов: ')))
    emp.set_hourly_pay(float(input('Оплата за час: ')))

    return emp

# SalaryEmployee
def new_salary_employee():
    print('\nВведите данные SalaryEmployee:')

    emp = SalaryEmployee("", "", "", "", "", 0)

    emp.name_employee = input_with_validation('Имя: ', NAME_PATTERN)
    emp.phone = input_with_validation('Телефон: ', PHONE_PATTERN)
    emp.birthday = input_with_validation('Дата рождения: ', BIRTHDAY_PATTERN)
    emp.email = input_with_validation('Эл.почта: ', EMAIL_PATTERN)
    emp.position = input_with_validation('Должность: ', POSITION_PATTERN)

    emp.salary = float(input('Оклад: '))

    return emp


def main():
    employees = []

    for i in range(2):
        employees.append(new_employee())

    for i in range(2):
        employees.append(new_hourly_employee())

    for i in range(2):
        employees.append(new_salary_employee())

    print('Информация о сотрудниках')

    for emp in employees:
        print("\nИмя:", emp.name_employee)
        print("Телефон:", emp.phone)
        print("Должность:", emp.position)

        salary = emp.calculate_salary()

        if salary is not None:
            print("Зарплата:", salary)

    # Зарплаты по типу
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

    print("\nЗарплаты сотрудников по типу найма:")
    print("HourlyEmployee:", hourly_salaries)
    print("SalaryEmployee:", salary_salaries)

if __name__ == "__main__":
    main()
