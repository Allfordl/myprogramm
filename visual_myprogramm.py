import tkinter as tk
from tkinter import ttk

myprogramm = tk.Tk()
myprogramm.title('Suppliers')
myprogramm.geometry('1000x1000+10+100')

question_value = tk.StringVar()


photo = tk.PhotoImage(file='logo/maytoni.png')
myprogramm.iconphoto(False, photo)

background_image = tk.PhotoImage(file='logo/background.png')
background_label = tk.Label(myprogramm, image=background_image)
background_label.image = background_image  # Keep a reference
background_label.place(relwidth=1, relheight=1)

menubar = tk.Menu(myprogramm)
settings_menu = tk.Menu(menubar)
settings_menu.add_command(label='Open file')
settings_menu.add_command(label='Close current file')
settings_menu.add_command(label='Reset')
settings_menu.add_command(label='Delete')


menubar.add_cascade(label='File',menu=settings_menu)
myprogramm.config(menu=menubar)


notebook = ttk.Notebook(myprogramm)
notebook.pack(fill='both', expand=True)

open_file = ttk.Frame(notebook)
notebook.add(open_file, text='Open_file')


myprogramm.mainloop()
