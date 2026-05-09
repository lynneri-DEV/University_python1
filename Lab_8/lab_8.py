import os
from gtts import gTTS
from gtts.lang import tts_langs


def text_to_speech():
    print("--- Приложение Text-to-Audio (gTTS) ---")

    # 1. Выбор источника текста
    choice = input("Выберите источник текста (1 - консоль, 2 - файл .txt): ")
    # text = ""
    # lang = "ru"  # По умолчанию русский

    try:
        if choice == '1':
            text = input("Введите текст для озвучивания: ").strip()
        elif choice == '2':
            file_path = input("Введите путь к .txt файлу: ").strip()
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл {file_path} не найден.")

            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read().strip()
        else:
            print("Ошибка: Неверный выбор.")
            return

        # 2. Проверка: не пуст ли текст
        if not text:
            print("Ошибка: Текст для преобразования отсутствует.")
            return

        # 3. Проверка поддержки языка
        supported_langs = tts_langs()
        user_lang = input("Введите код языка (например, 'ru' или 'en'): ").lower()

        if user_lang not in supported_langs:
            print(f"Предупреждение: Язык '{user_lang}' не поддерживается. Используем 'ru'.")
            user_lang = 'ru'

        # 4. Генерация речи
        print("Генерация аудио... подождите.")
        tts = gTTS(text=text, lang=user_lang, slow=False)

        output_file = "result.mp3"
        tts.save(output_file)

        # 5. Проверка результата
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            print(f"Успех! Файл сохранен как: {os.path.abspath(output_file)}")
            print(f"Размер файла: {os.path.getsize(output_file)} байт.")
        else:
            print("Ошибка: Аудиофайл не был создан или он пуст.")

    except Exception as e:
        print(f"Произошла ошибка в процессе выполнения: {e}")


if __name__ == "__main__":
    text_to_speech()
