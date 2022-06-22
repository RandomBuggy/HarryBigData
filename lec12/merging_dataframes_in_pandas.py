import pandas as pd

df1 = pd.DataFrame([[13,26,45], [34, 28, 23], [56, 19, 89]], columns=["A", "B", "C"])
print(df1)
df2 = pd.DataFrame([[23,26,42], [32, 28, 22], [52, 19, 99]], columns=["X", "Y", "Z"])
print(df2)

df3 = pd.merge(df1, df2, left_on="B", right_on="Y")
print(df3)
