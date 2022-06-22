import pandas as pd
df = pd.DataFrame([[363,474,33,32], [575,463,447,347], [585,443,583,462], [585,473,3626,584]], columns=["Q", "W", "E", "R"])
print(df)
df.to_csv("export.csv")
df.to_csv("exp2.csv", index=False)
