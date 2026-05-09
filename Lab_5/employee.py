class Employee:
    def __init__(self, name_employee, phone, birthday, email, position):
        self.__name_employee = name_employee
        self.__phone = phone
        self.__birthday = birthday
        self.__email = email
        self.__position = position

    # используются декораторы
    @property
    def name_employee(self):
        return self.__name_employee

    @name_employee.setter
    def name_employee(self, value):
        self.__name_employee = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def calculate_age(self):
        pass

    def calculate_salary(self):
        return self._calculate_salary()

    def _calculate_salary(self):
        return None


class HourlyEmployee(Employee):
    def __init__(self, name_employee, phone, birthday, email, position,
                 number_of_hour, hourly_pay):
        super().__init__(name_employee, phone, birthday, email, position)
        self.__number_of_hour = number_of_hour
        self.__hourly_pay = hourly_pay

    # используется предопределенная функция
    def set_number_of_hour(self, value):
        self.__number_of_hour = value

    # def get_number_of_hour(self):
    #     return self.__number_of_hour

    def set_hourly_pay(self, value):
        self.__hourly_pay = value

    def _calculate_salary(self):
        return self.__number_of_hour * self.__hourly_pay

class SalaryEmployee(Employee):
    def __init__(self, name_employee, phone, birthday, email, position, salary):
        super().__init__(name_employee, phone, birthday, email, position)
        self.__salary = salary

    # используются декораторы
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def _calculate_salary(self):
        return self.__salary