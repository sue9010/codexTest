import tkinter as tk
from tkinter import ttk, messagebox

from calculator import add, subtract, multiply, divide

class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        padding = {'padx': 5, 'pady': 5}
        tk.Label(self, text="First Number:").grid(row=0, column=0, **padding)
        tk.Entry(self, textvariable=self.num1_var).grid(row=0, column=1, **padding)

        tk.Label(self, text="Second Number:").grid(row=1, column=0, **padding)
        tk.Entry(self, textvariable=self.num2_var).grid(row=1, column=1, **padding)

        self.operation = tk.StringVar(value='add')
        operations = [('Add', 'add'),
                      ('Subtract', 'subtract'),
                      ('Multiply', 'multiply'),
                      ('Divide', 'divide')]
        row = 2
        for text, value in operations:
            ttk.Radiobutton(self, text=text, variable=self.operation, value=value).grid(row=row, columnspan=2, sticky='w', **padding)
            row += 1

        ttk.Button(self, text="Calculate", command=self.calculate).grid(row=row, columnspan=2, **padding)
        row += 1

        tk.Label(self, text="Result:").grid(row=row, column=0, **padding)
        tk.Entry(self, textvariable=self.result_var, state='readonly').grid(row=row, column=1, **padding)

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")
            return
        op = self.operation.get()
        try:
            if op == 'add':
                result = add(num1, num2)
            elif op == 'subtract':
                result = subtract(num1, num2)
            elif op == 'multiply':
                result = multiply(num1, num2)
            elif op == 'divide':
                result = divide(num1, num2)
            else:
                raise ValueError("Unknown operation")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
        self.result_var.set(str(result))

if __name__ == '__main__':
    app = CalculatorUI()
    app.mainloop()
