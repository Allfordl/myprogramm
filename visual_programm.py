import tkinter as tk
from tkinter import ttk

def say_hello():
    print("Hello")

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print("Empty")

def select_all():
    for check in question:
        check.select()






visual = tk.Tk()
visual.title('Suppliers')
visual.geometry('1000x1000+10+100')

question_value = tk.StringVar()


photo = tk.PhotoImage(file='logo/maytoni.png')
visual.iconphoto(False, photo)

background_image = tk.PhotoImage(file='logo/background.png')
background_label = tk.Label(visual, image=background_image)
background_label.image = background_image  # Keep a reference
background_label.place(relwidth=1, relheight=1)

# label1 = tk.Label(visual, text='Hello')
# label1.pack()

btn1 = tk.Button(visual, text='Hello',
                 command=say_hello)

btn1.grid(row=0,column=0)
# visual.resizable(True,True)
# visual.minsize(300,400)
# visual.maxsize(900,900)

name = tk.Entry(visual)
name.grid(row=0,column=1)

btn2 = tk.Button(visual, text='get',command=get_entry).grid(row=2,column=1)

question = tk.Checkbutton(visual,text='?')
question.grid(row=3,column=5)

question2 = tk.Checkbutton(visual)
question2.grid(row=3,column=6)

combo = ttk.Combobox(visual)
combo.grid(row=4,column=7)

menubar = tk.Menu(visual)
settings_menu = tk.Menu(menubar)
settings_menu.add_command(label='Reset')
settings_menu.add_command(label='Delete')


menubar.add_cascade(label='File',menu=settings_menu)
visual.config(menu=menubar)


visual.mainloop() # Делаем так, чтобы программа всегда была открыта, ждала наших действий