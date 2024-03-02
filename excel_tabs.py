import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pandastable import Table
import pandas as pd

def open_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    if file_path:
        excel_data = pd.read_excel(file_path)
        display_excel_data(excel_data, file_path)

def display_excel_data(data, file_name):
    new_tab = ttk.Frame(notebook)
    notebook.add(new_tab, text=file_name)

    table = Table(new_tab, dataframe=data)
    table.show()

# Создание основного окна
root = tk.Tk()
root.title('Excel Viewer')

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Кнопка для открытия Excel файла
open_button = tk.Button(root, text='Открыть Excel файл', command=open_excel_file)
open_button.pack()

root.mainloop()
