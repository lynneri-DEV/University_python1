import task2 as f

print(' Учет данных о детях сотрудников компании “Подарки всем”')

def main():
    while True:
        print("\nМЕНЮ:\n1. Ввод данных\n2. Просмотр всех данных\n3. Бездетные сотрудники\n4. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            f.input_data()
        elif choice == "2":
            f.show_data()
        elif choice == "3":
            f.no_children()
        elif choice == "4":
            print("Выход...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
