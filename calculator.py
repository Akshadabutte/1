from tkinter import Tk, Button, Entry, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="grey")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_val = ''
        Entry(master, width=17, bg="#fff", font=('Arial bold', 18), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            'C', '(', ')', '+',
            '7', '8', '9', '-',
            '4', '5', '6', '*',
            '1', '2', '3', '/',
            '%', '0', '.', '='
        ]

        x, y = 0, 50
        for button in buttons:
            Button(master, width=11, height=4, text=button, relief='flat', bg='white',
                   command=lambda value=button: self.press(value)).place(x=x, y=y)
            x += 85
            if x > 257:
                x = 0
                y += 70

    def press(self, value):
        if value == 'C':
            self.clear()
        elif value == '=':
            self.solve()
        else:
            self.entry_val += str(value)
            self.equation.set(self.entry_val)

    def clear(self):
        self.entry_val = ''
        self.equation.set(self.entry_val)

    def solve(self):
        try:
            # Use eval to calculate the expression
            result = eval(self.entry_val)
            self.equation.set(result)
            self.entry_val = str(result)  # Update entry_val for further calculations
        except Exception as e:
            self.equation.set("Error")
            self.entry_val = ''

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
