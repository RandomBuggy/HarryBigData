import pandas as pd
#nse stock market
df = pd.read_csv("data.csv")
print(df)
#with column as key
print(df["SERIES"])
#category object variable
print(df["SERIES"].astype("category"))
