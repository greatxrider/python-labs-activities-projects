#finding out calories in a banana
import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")

results = json.loads(data.content)
pd.DataFrame(results)

df2 = pd.json_normalize(results)
print(df2)

banana = df2.loc[df2['name'] == 'Banana']
print((banana.iloc[0]['nutritions.calories']))