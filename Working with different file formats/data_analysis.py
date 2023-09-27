#Readng an image file

from PIL import Image
from IPython.display import display
import pandas as pd
import seaborn as sns
import data_analysis as da
import matplotlib.pyplot as plt

img = Image.open("./dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
img.show()

file = "./diabetes.csv"
df = pd.read_csv(file)

print("The first 5 rows of the datafrace")

df.head(5)

df.shape

df.info()

df.describe()

#Identify and handling missing values

missing_data = df.isnull()
missing_data.head(5)

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
    
print(df.dtypes)

labels = 'Diabetic', 'Not Diabetic'
plt.pie(df['Outcome'].value_counts(), labels = labels, autopct = '%0.02f%%')
plt.legend()
plt.show()