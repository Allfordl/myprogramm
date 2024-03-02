import tkinter as tk
from tkinter import ttk

# Создаем главное окно
visual = tk.Tk()
visual.title('Multiple Tabs')

# Создаем Notebook для вкладок
notebook = ttk.Notebook(visual)
notebook.pack(fill='both', expand=True)

# Создаем вкладку 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Tab 1')

# Создаем элементы интерфейса для вкладки 1
label1 = tk.Label(tab1, text='This is Tab 1')
label1.pack(padx=20, pady=20)

# Создаем вкладку 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Tab 2')

# Создаем элементы интерфейса для вкладки 2
label2 = tk.Label(tab2, text='This is Tab 2')
label2.pack(padx=20, pady=20)

visual.mainloop()