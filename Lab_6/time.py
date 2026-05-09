from tkinter import *
from datetime import datetime

temp = 0 # счетчик времени
after_id = '' # идентификатор отложенного вызова

def tick():
    global temp, after_id

    after_id = root.after(1000, tick) # повторный запуск функции через 1 секунду
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S') # Переводит значение temp в формат времени

    temp += 1
    label1.configure(text=str(f_temp)) # Обновляет текст в label1, показывая текущее время таймера

def start_tick():
    btnStart.pack_forget() # Кнопка «Старт» скрывается из интерфейса
    btnStop.pack() # Кнопка «Стоп» отображается
    tick()


def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id) # останавливает запланированный вызов функции

def continue_tick():
    btnStart.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()

root = Tk()
root.title("Секундомер")
root.resizable(width=False, height=False)
root.geometry("300x200")

label1 = Label(root, width=10, font=('Comic Sans MS', 30), text='00:00')
label1.pack()

btnStart = Button(root, text='Старт', font=('Comic Sans MS', 20), width=15, command=start_tick)
btnStop = Button(root, text='Стоп', font=('Comic Sans MS', 20), width=15, command=stop_tick)
btnContinue = Button(root, text='Продолжить', font=('Comic Sans MS', 20), width=15, command=continue_tick)
btnReset = Button(root, text='Сброс', font=('Comic Sans MS', 20), width=15, command=reset_tick)
btnStart.pack()

root.mainloop()