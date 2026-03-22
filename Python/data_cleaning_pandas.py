from pathlib import Path

import pandas as pd

# Make the CSV path work no matter where the repo is located.
DATA_PATH = Path(__file__).resolve().parents[1] / "FILES" / "data.csv"

df = pd.read_csv(DATA_PATH, index_col="Name")
# dropping irrelevant column
df=df.drop(columns=['Legendary'])

#managing missing values

# dropping rows with missing values in Type2 column
# df=df.dropna(subset=["Type2"])
# print(df.to_string())

# filling missing values in Type2 column with "None"
df["Type2"]=df["Type2"].fillna("None")
print(df.to_string())

#fixing inconsistent data
df["Type1"]=df["Type1"].replace({"Fire": "FIRE"})
print(df.to_string())


#fixing data types
df["Legendary"]=df["Legendary"].astype(bool)
print(df.dtypes)

#dulicate data
df=df.drop_duplicates()
print(df.to_string())