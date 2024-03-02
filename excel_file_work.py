import pandas as pd
from datetime import datetime
import os
# import shutil

df = pd.read_excel("main_file/Delays.xlsx")

output_folder = 'output'
today_date = datetime.today().strftime('%Y-%m-%d')

grouped = df.groupby(df.columns[0])

for group_name, group_data in grouped:
    file_name = os.path.join(output_folder, f"{group_name}.xlsx")
    group_data.to_excel(file_name, index=False)

# shutil.rmtree(output_folder)
