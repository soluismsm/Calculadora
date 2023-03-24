import tkinter as tk
from tkinter import ttk

values = {"num1": "0", "num2": "0", "operator": None, "repeat": False}


def calculate():
    num1 = float(values["num1"])
    num2 = float(values["num2"])
    operator = values["operator"]
    if operator is not None:
        if "/" in operator:
            result = num1 / num2
        elif "x" in operator:
            result = num1 * num2
        elif "-" in operator:
            result = num1 - num2
        else:
            result = num1 + num2
    else:
        result = num1

    if result.is_integer():
        result = int(result)

    values["num1"] = result
    values["repeat"] = True

    output_text.configure(text=result)


def get_num(number):
    if values["repeat"]:
        clear_output()

    if values["operator"] is None:
        num = values["num1"]

        if values["num1"] == "0":
            num = number
            values["num1"] = num
        else:
            num += number
            values["num1"] = num
    else:
        num = values["num2"]

        if values["num2"] == "0":
            num = number
            values["num2"] = num
        else:
            num += number
            values["num2"] = num

    values["repeat"] = False
    output_text.configure(text=num)


def get_operator(operator):
    repeat = values["repeat"]
    if repeat:
        values["num2"] = "0"
        values["repeat"] = False
    values["operator"] = operator


def clear_output():
    values["num1"] = "0"
    values["num2"] = "0"
    values["operator"] = None
    values["repeat"] = False
    output_text.configure(text="0")


root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack()

style = ttk.Style()
style.configure("TButton", font=("TkDefaultFont", 15))
style.configure("TLabel", font=("TkDefaultFont", 15))


output_text = ttk.Label(frame, text="0")
output_text.grid(row=0, columnspan=4, sticky="E")

# First Row
number7 = ttk.Button(frame, text="7", command=lambda: get_num("7"))
number7.grid(row=3, column=0, ipady=10)
number8 = ttk.Button(frame, text="8", command=lambda: get_num("8"))
number8.grid(row=3, column=1, ipady=10)
number9 = ttk.Button(frame, text="9", command=lambda: get_num("9"))
number9.grid(row=3, column=2, ipady=10)
division = ttk.Button(frame, text="÷", command=lambda: get_operator("/"))
division.grid(row=3, column=3, ipady=10)

# Second Row
number4 = ttk.Button(frame, text="4", command=lambda: get_num("4"))
number4.grid(row=4, column=0, ipady=10)
number5 = ttk.Button(frame, text="5", command=lambda: get_num("5"))
number5.grid(row=4, column=1, ipady=10)
number6 = ttk.Button(frame, text="6", command=lambda: get_num("6"))
number6.grid(row=4, column=2, ipady=10)
multiplication = ttk.Button(frame, text="x", command=lambda: get_operator("x"))
multiplication.grid(row=4, column=3, ipady=10)

# Third Row
number1 = ttk.Button(frame, text="1", command=lambda: get_num("1"))
number1.grid(row=5, column=0, ipady=10)
number2 = ttk.Button(frame, text="2", command=lambda: get_num("2"))
number2.grid(row=5, column=1, ipady=10)
number3 = ttk.Button(frame, text="3", command=lambda: get_num("3"))
number3.grid(row=5, column=2, ipady=10)
subtraction = ttk.Button(frame, text="-", command=lambda: get_operator("-"))
subtraction.grid(row=5, column=3, ipady=10)

# Fourth Row
number0 = ttk.Button(frame, text="0", command=lambda: get_num("0"))
number0.grid(row=6, column=0, ipady=10)
dot = ttk.Button(frame, text=",", command=lambda: get_num("."))
dot.grid(row=6, column=1, ipady=10)
clear = ttk.Button(frame, text="C", command=clear_output)
clear.grid(row=6, column=2, ipady=10)
addition = ttk.Button(frame, text="+", command=lambda: get_operator("+"))
addition.grid(row=6, column=3, ipady=10)

equal_button = ttk.Button(frame, text="=", command=calculate)
equal_button.grid(row=7, columnspan=4, rowspan=2, sticky="WSNE")


root.mainloop()
