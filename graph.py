import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from pandastable import Table

def read_excel_file(file_path):
    try:
        excel_data = pd.read_excel(file_path)
        return excel_data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read Excel file: {str(e)}")
        return None

def display_chart(data):
    plt.figure(figsize=(8, 6))
    plt.plot(data['Фабрика'], data['Кол во дней просрочки среднее'])  # Замените 'X' и 'Y' на названия столбцов в вашем Excel файле
    plt.title('График данных из Excel')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

# Пример пути к файлу Excel
file_path = 'main_file/Delays.xlsx'

# Чтение данных из Excel файла
excel_data = read_excel_file(file_path)

# Отображение графика на основе данных из Excel
display_chart(excel_data)