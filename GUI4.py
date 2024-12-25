import tkinter as tk
def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text=f"Addition of two variables is: {result}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Adder")

# Create and place the widgets
label_num1 = tk.Label(root, text="Num1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Num2:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.grid(row=2, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=3, columnspan=2)

# Run the application
root.mainloop()
