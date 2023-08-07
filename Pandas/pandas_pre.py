#creating dataframe from a dictionary

import pandas as pd

x = {'Name': ['Jeph','Mari', 'Manos', 'Daligdig'], 'ID': [1, 2, 3, 4], 'Department': ['Java Group', 'Python Group', 'C-Sharp Group', 'C++ Group'], 
      'Salary':[100000, 80000, 50000, 60000]}
df = pd.DataFrame(x)
print(df)

#Selecting a column

x = df[["ID"]]
print(x)

z = df[['Department','Salary','ID']]
print(z)

#Creating new dataframe from a dictionary

y = {'Student': ['David', 'Samuel', 'Terry', 'Evan'], 'Age':[27,24,22,32], 'Country':['UK', 'Canada', 'China', 'USA'], 'Course':['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 'Marks':[85,72,89,76]}
dfy = pd.DataFrame(y)
print(dfy)

b = dfy[["Marks"]]
print(b)

c = dfy[["Country","Course"]]
print(c)

x=dfy[["Student"]]
print(x)

#loc() and iloc() functions

print(dfy.iloc[0,1])
print(dfy.loc[1,'Age'])

dfa = dfy
dfa = dfa.set_index('Student')

print(dfa.head())
print(dfa.loc['David', 'Age'])

#Slicing
print (dfy.iloc[0:2, 0:3])
print(dfy.loc[0:2, 'Student':'Country'])