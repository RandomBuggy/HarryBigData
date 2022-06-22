import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)

df1 = pd.DataFrame([[34,66,4,87], [47,32,45,17], [56, 34, 78, 89], [45, 89,70,34]])
print(df1)
print(df1.head(3))
print(df1.tail(2))

#to find data-frame size rows and columns
print(df1.shape)
#data-frame slicing
print(df1.iloc[0, 3])
print(df.iloc[0:3, 1:3])
#custom column
df2 = pd.DataFrame([[34,66,4,87], [47,32,45,17], [56, 34, 78, 89], [45, 89,70,34]], columns=["A", "B", "C", "D"])
print(df2)
