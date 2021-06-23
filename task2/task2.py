import tkinter as tk
import math

window = tk.Tk()
window.title('Калькулятор')
window.geometry('750x750')
window.resizable(False, False)
window.config(bg='yellow')

buttons = ["C", "DEL", "*", "=",
           "1", "2", "3", "/",
           "4", "5", "6", "+",
           "7", "8", "9", "-",
           "(", "0", ")", "^2",
           "cos", "sin", "tan", "ctg",
           "log", "ln", "%", "bin"]


def logical(operation):
    global oper

    if operation == 'C':
        oper = ''
    elif operation == "DEL":
        oper = oper[0:-1]
    elif operation == "^2":
        oper = str((eval(oper)) ** 2)
    elif operation == "cos":
        oper = str(math.cos(eval(oper)))
    elif operation == "sin":
        oper = str(math.sin(eval(oper)))
    elif operation == "tan":
        oper = str(math.tan(eval(oper)))
    elif operation == "ln":
        oper = str(math.log1p(eval(oper)))
    elif operation == "log":
        oper = str(math.log(eval(oper)))
    elif operation == "ctg":
        oper = str(math.cos(eval(oper)) / math.sin(eval(oper)))
    elif operation == "bin":
        oper = str(bin(eval(oper)))
    elif operation == "=":
        oper = str(eval(oper))
    else:
        if oper == '0':
            oper = ''
        oper += operation
    label_text.configure(text=oper)


oper = '0'
label_text = tk.Label(text=oper, font=('Times New Romans', 19))
label_text.place(x=11, y=50)

x = 10
y = 140
for button in buttons:
    get_lbl = lambda x=button: logical(x)
    tk.Button(text=button, bg='white', font=('Times New Romans', 19), command=get_lbl).place(x=x, y=y, width=115,
                                                                                             height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81

window.mainloop()
