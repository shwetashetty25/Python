import tkinter as tk
root = tk.Tk()
root.geometry("250x150")

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()
    Lbl1 = tk.Label(root, text="Username is " + name)
    Lbl2 = tk.Label(root, text="Password is " + password)
    Lbl1.grid(row=3, column=0, columnspan=2, sticky="w")
    Lbl2.grid(row=4, column=0, columnspan=2, sticky="w")
    name_var.set('')
    passw_var.set('')

name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')
sub_btn = tk.Button(root, text='Submit', command=submit)

name_label.grid(row=0, column=0, pady=10)
name_entry.grid(row=0, column=1, pady=10)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=0, columnspan=2)

root.mainloop()
