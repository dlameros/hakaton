import tkinter as tk
import sat

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result.config(text="Результат: " + str(result))
    except ValueError:
        label_result.config(text="Ошибка: введите числа!")


window = tk.Tk()
window.geometry("250x250")

label1 = tk.Label(window, text="Координата ширина:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Координата долготы:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Рассчитать", command=calculate)
button.pack()

label_result = tk.Label(window, text="Результат: ")
label_result.pack()

window.mainloop()