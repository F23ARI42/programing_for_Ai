import pandas as pd
data=pd.read_csv("data.csv")
data["calories"].fillna(data["calories"].mean(),inplace=True)
