from tkinter import *
from tkinter import messagebox
import pickle
import re

root = Tk()
root.geometry("300x500")
root.title("Вход в систему")

# Цвета
BG = "#1e1e2e"
CARD = "#2a2a3e"
ACCENT = "#7c3aed"
ACCENT_HOVER = "#6d28d9"
TEXT = "#e2e8f0"
TEXT_MUTED = "#94a3b8"
ENTRY_BG = "#313147"
ERROR = "#ef4444"
SUCCESS = "#22c55e"

root.configure(bg=BG)


def style_entry(entry):
    entry.configure(
        bg=ENTRY_BG, fg=TEXT, insertbackground=TEXT,
        relief=FLAT, font=("Arial", 11),
        highlightthickness=1, highlightbackground=ACCENT,
        highlightcolor=ACCENT
    )


def style_button(btn, color=ACCENT):
    btn.configure(
        bg=color, fg=TEXT, relief=FLAT,
        font=("Arial", 11, "bold"),
        cursor="hand2", padx=10, pady=6,
        activebackground=ACCENT_HOVER, activeforeground=TEXT
    )


def style_label(lbl, muted=False):
    lbl.configure(
        bg=BG, fg=TEXT_MUTED if muted else TEXT,
        font=("Arial", 10)
    )


def clear():
    for widget in root.winfo_children():
        widget.destroy()


# Паттерны
def validate_login(login):
    # Только буквы, цифры и _, длина 3-20
    pattern = r'^[a-zA-Z0-9_]{3,20}$'
    return re.match(pattern, login)


def validate_password(password):
    # Минимум 6 символов, хотя бы одна цифра и одна буква
    pattern = r'^(?=.*[A-Za-z])(?=.*\d).{6,}$'
    return re.match(pattern, password)


def registration():
    clear()

    title = Label(root, text="Регистрация", font=("Arial", 16, "bold"))
    title.configure(bg=BG, fg=ACCENT)
    title.pack(pady=20)

    hint = Label(root, text="Логин: 3-20 символов (буквы, цифры, _)\nПароль: мин. 6 символов, буква + цифра",
                 justify="center")
    style_label(hint, muted=True)
    hint.pack(pady=(0, 10))

    Label(root, text="Логин", bg=BG, fg=TEXT_MUTED, font=("Arial", 9)).pack(anchor="w", padx=50)
    registr_login = Entry(root, width=25)
    style_entry(registr_login)
    registr_login.pack(pady=(2, 8))

    Label(root, text="Пароль", bg=BG, fg=TEXT_MUTED, font=("Arial", 9)).pack(anchor="w", padx=50)
    registr_password1 = Entry(root, show="*", width=25)
    style_entry(registr_password1)
    registr_password1.pack(pady=(2, 8))

    Label(root, text="Повторите пароль", bg=BG, fg=TEXT_MUTED, font=("Arial", 9)).pack(anchor="w", padx=50)
    registr_password2 = Entry(root, show="*", width=25)
    style_entry(registr_password2)
    registr_password2.pack(pady=(2, 8))

    error_label = Label(root, text="", bg=BG, fg=ERROR, font=("Arial", 9))
    error_label.pack()

    def save():
        login = registr_login.get()
        password1 = registr_password1.get()
        password2 = registr_password2.get()

        if not login or not password1 or not password2:
            error_label.config(text="Заполните все поля")
            return

        if not validate_login(login):
            error_label.config(text="Неверный формат логина")
            return

        if not validate_password(password1):
            error_label.config(text="Неверный формат пароля")
            return

        if password1 != password2:
            error_label.config(text="Пароли не совпадают")
            return

        with open("login.txt", "wb") as f:
            pickle.dump({login: password1}, f)

        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        login_screen()

    btn_reg = Button(root, text="Зарегистрироваться", command=save, width=20)
    style_button(btn_reg)
    btn_reg.pack(pady=10)

    btn_back = Button(root, text="Назад", command=login_screen, width=20)
    style_button(btn_back, color="#3f3f5a")
    btn_back.pack()


def login_screen():
    clear()

    title = Label(root, text="Вход в систему", font=("Arial", 16, "bold"))
    title.configure(bg=BG, fg=ACCENT)
    title.pack(pady=30)

    Label(root, text="Логин", bg=BG, fg=TEXT_MUTED, font=("Arial", 9)).pack(anchor="w", padx=50)
    enter_login = Entry(root, width=25)
    style_entry(enter_login)
    enter_login.pack(pady=(2, 8))

    Label(root, text="Пароль", bg=BG, fg=TEXT_MUTED, font=("Arial", 9)).pack(anchor="w", padx=50)
    enter_password = Entry(root, show="*", width=25)
    style_entry(enter_password)
    enter_password.pack(pady=(2, 8))

    error_label = Label(root, text="", bg=BG, fg=ERROR, font=("Arial", 9))
    error_label.pack()

    def check():
        login_input = enter_login.get()
        password_input = enter_password.get()

        if not login_input or not password_input:
            error_label.config(text="Заполните все поля")
            return

        try:
            with open("login.txt", "rb") as f:
                login_pass_save = pickle.load(f)

            if login_input in login_pass_save and login_pass_save[login_input] == password_input:
                messagebox.showinfo("Успех", f"Добро пожаловать, {login_input}!")
            else:
                error_label.config(text="Неверный логин или пароль")

        except FileNotFoundError:
            error_label.config(text="Сначала зарегистрируйтесь")

    btn_enter = Button(root, text="Войти", command=check, width=20)
    style_button(btn_enter)
    btn_enter.pack(pady=10)

    btn_reg = Button(root, text="Регистрация", command=registration, width=20)
    style_button(btn_reg, color="#3f3f5a")
    btn_reg.pack()


login_screen()
root.mainloop()