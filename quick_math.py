from tkinter import *
from tkinter import ttk, messagebox

class QuickMathCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Math Calculator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        font = ("Times New Roman", 48, "bold")

        main_frame = Frame(self.root)
        main_frame.pack(expand=True)

        # Input frame
        input_frame = Frame(main_frame)
        input_frame.pack(pady=50)

        self.input1 = Entry(input_frame, font=font, width=5)
        self.input1.grid(row=0, column=0, padx=5)

        self.operator_var = StringVar()
        self.operator = ttk.Combobox(
            input_frame, textvariable=self.operator_var, values=["+", "-", "*", "/"], font=font, width=2
        )
        self.operator.grid(row=0, column=1, padx=5)
        self.operator.current(0)

        self.input2 = Entry(input_frame, font=font, width=5)
        self.input2.grid(row=0, column=2, padx=5)

        self.equal_button = Button(input_frame, text="=", font=font, command=self.calculate)
        self.equal_button.grid(row=0, column=3, padx=5)

        # Result label
        self.result = Label(main_frame, text=" ", font=font)
        self.result.pack(pady=20)

    def calculate(self):
        try:
            first = int(self.input1.get())
            second = int(self.input2.get())
            op = self.operator_var.get()

            if op == '+':
                res = first + second
            elif op == '-':
                res = first - second
            elif op == '*':
                res = first * second
            elif op == '/':
                if second == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                res = first // second  # Integer division
            else:
                messagebox.showerror("Error", "Invalid operator")
                return

            self.result.config(text=str(res))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers")

if __name__ == "__main__":
    root = Tk()
    calculator = QuickMathCalculator(root)
    root.mainloop()
