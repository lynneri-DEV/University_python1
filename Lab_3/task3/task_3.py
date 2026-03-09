# вывод списка товаров
def show_products(products):
    if len(products) == 0:
        print("Список товаров пуст")
    else:
        print("\nТекущие товары:")
        for i, product in enumerate(products, start=1):
            print(i, "-", product)


# добавление товара
def add_product(products):
    name = input("Введите название товара: ")

    if name in products:
        print("Такой товар уже есть в списке")
    else:
        products.append(name)
        print("Товар добавлен")


# удаление по номеру
def delete_by_number(products):
    if len(products) == 0:
        print("Список пуст")
        return

    try:
        num = int(input("Введите номер товара для удаления: "))

        if num <= 0 or num > len(products):
            print("Неверный номер")
        else:
            removed = products.pop(num - 1)
            print("Удален товар:", removed)

    except ValueError:
        print("Введите число")


# удаление по названию
def delete_by_name(products):
    name = input("Введите название товара: ")

    if name in products:
        products.remove(name)
        print("Товар удален")
    else:
        print("Такого товара нет в списке")


# выбор способа удаления
def delete_product(products):
    print("Удалить:")
    print("1 - по номеру")
    print("2 - по названию")

    choice = input("Ваш выбор: ")

    if choice == "1":
        delete_by_number(products)
    elif choice == "2":
        delete_by_name(products)
    else:
        print("Неверный выбор")
