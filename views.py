
import tkinter as tk
import sat, main

def calculate():
    try:
        
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = main.get_distance(num1, num2)
        name, distance = result[2], result[0]
        label_result.config(text=f"Ближайший спутник {name}\n{round(distance, 2)}км")
    except ValueError:
        label_result.config(text="Ошибка: введите числа!")


window = tk.Tk()
window.geometry("400x250")

label1 = tk.Label(window, text="Введите координаты широты в градусах -90 90:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Введите координаты долготы в градусах -180 180:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Рассчитать", command=calculate)
button.pack()

label_result = tk.Label(window, text="Результат: ")
label_result.pack()

window.mainloop()