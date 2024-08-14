import tkinter as tk

root = tk.Tk()

root.title("Application Testing Ground")

#Create and label rentries
tk.Label(root, text="Company Name: ").grid(row=0)
tk.Label(root, text="Position: ").grid(row=1)
tk.Label(root, text="Email: ").grid(row=2)
tk.Label(root, text="Password: ").grid(row=3)

company_name = tk.Entry(root)
position = tk.Entry(root)
email = tk.Entry(root)
password = tk.Entry(root)

company_name.grid(row=0, column=1)
position.grid(row=1, column=1)
email.grid(row=2, column=1)
password.grid(row=3, column=1)

root.mainloop()