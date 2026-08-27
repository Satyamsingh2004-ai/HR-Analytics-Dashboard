import pandas as pd
import numpy as np
leave = pd.read_csv("output/leaves.csv")
print(leave.head())
print(leave.info())
print(leave.shape)
print(leave.isnull().sum())

print(leave.duplicated().sum())
leave = leave.drop_duplicates()

print(leave.duplicated().sum())
leave["start_date"] = pd.to_datetime(leave["start_date"])

leave["end_date"] = pd.to_datetime(leave["end_date"])
print(leave.dtypes)
leave.to_csv("output/cleaned_leaves.csv", index=False)
print("Leaves dataset cleaned and saved successfully!")
