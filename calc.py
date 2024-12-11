import tkinter as tk

def update_expression(expression):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + expression)

def calculate():
    try:
        result = eval(entry.get())   
        print(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: update_expression(t))
    button.grid(row=row, column=col)

root.mainloop()


 # Проверка уязвимости, ввести в окно вода калькулятора __import__('os').system('echo Hello')