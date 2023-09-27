#Reading the data from XLSX file

import pandas as pd

excel = "./file_example_XLSX_10.xlsx"

df = pd.read_excel(excel)

print(df)