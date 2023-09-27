#Reading data from CSV in Python

import pandas as pd

df = pd.read_csv('./addresses.csv', header = None)
print(df)

df.columns = ['First Name', 'Last Name', 'Address', 'City', 'State', 'Area Code']

print(df)

print(df['First Name']) 

df = df[['First Name', 'Last Name', 'Address', 'City','State','Area Code']]

print(df)

print(df.loc[0])

print(df.loc[[0,1,2], "First Name"])

print(df.iloc[[0,1,2], 0])