import task_3 as f

products = []

def menu():
    print("\nМЕНЮ\n1. Вывести список товаров\n2. Добавить товар\n3. Удалить товар\n4. Выход")

while True:
    menu()
    choice = input("Выберите опцию: ")

    if choice == "1":
        f.show_products(products)

    elif choice == "2":
        f.add_product(products)

    elif choice == "3":
        f.delete_product(products)

    elif choice == "4":
        print("Выход из программы")
        break

    else:
        print("Неверная опция. Попробуйте снова.")
