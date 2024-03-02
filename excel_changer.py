import tkinter as tk
from tkinter import filedialog
import openpyxl

def open_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    if file_path:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        display_excel_data(sheet)

def display_excel_data(sheet):
    for row_idx, row_data in enumerate(sheet.iter_rows(values_only=True), start=1):
        for col_idx, cell_value in enumerate(row_data, start=1):
            entry = tk.Entry(root)
            entry.insert(0, str(cell_value))
            entry.grid(row=row_idx, column=col_idx)

# Создание основного окна
root = tk.Tk()
root.title('Excel Editor')

# Кнопка для открытия Excel файла
open_button = tk.Button(root, text='Открыть Excel файл', command=open_excel_file)
open_button.grid(row=0, column=0)

root.mainloop()