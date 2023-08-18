import requests
import json
import pandas as pd

data2 = requests.get("https://cat-fact.herokuapp.com/facts")

results2 = json.loads(data2.text)
df3 = pd.DataFrame(results2)
df3.drop(columns = "status", inplace = True)
print(df3)