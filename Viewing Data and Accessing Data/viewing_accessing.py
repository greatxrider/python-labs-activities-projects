#Jeph Mari Daligdig
#Viewing and Accessing Data

import pandas as pd

# Read data from CSV file

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

await download(xlsx_path, "TopSellingAlbums.xlsx")
df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()