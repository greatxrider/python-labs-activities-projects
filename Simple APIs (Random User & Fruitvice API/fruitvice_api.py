import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.content)
pd.DataFrame(results)

df2 = pd.json_normalize(results)
print(df2)

# family and genes of a cherry

cherry = df2.loc[df2['name'] == 'Cherry']
print((cherry.iloc[0]['family']), (cherry.iloc[0]['genus']))