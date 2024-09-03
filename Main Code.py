from tkinter import Tk, Entry, Button, StringVar
import math

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x480")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""

        # Entry widget with updated display bar style
        self.entry = Entry(master, width=17, bg="#555555", fg="#ffffff", font=("Arial Bold", 28), textvariable=self.equation, justify='right')
        self.entry.grid(row=0, column=0, columnspan=5)

        # Button styles
        button_style = {
            'relief': 'raised',
            'padx': 10,
            'pady': 10,
            'font': ('Arial', 16)
        }

        buttons = [
            ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('x', 2, 3), ('^', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('sin', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3), ('cos', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('C', 5, 2), ('=', 5, 3), ('tan', 5, 4)
        ]

        for (text, row, column) in buttons:
            if text == 'C':
                button = Button(master, text=text, command=self.clear, **button_style, bg="red", fg="white")
            elif text == '=':
                button = Button(master, text=text, command=self.solve, **button_style, bg="lightblue", fg="black")
            else:
                button = Button(master, text=text, command=lambda t=text: self.show(t), **button_style, bg="#f0f0f0", fg="black")
            button.grid(row=row, column=column, sticky="nsew")

        # Configure row and column weights
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(5):
            master.grid_columnconfigure(i, weight=1)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            expression = self.entry_value.replace('x', '*').replace('^', '**')
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            result = eval(expression)
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")

root = Tk()
calc = Calculator(root)
root.mainloop()
