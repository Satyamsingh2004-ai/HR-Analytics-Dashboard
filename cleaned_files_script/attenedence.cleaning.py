import pandas as pd
attendance = pd.read_csv("output/attendance.csv")
import pandas as pd

attendance = pd.read_csv("output/attendance.csv")

print(attendance["check_in"].head(10))
print(attendance["check_out"].head(10))
# Preview the dataset
print(attendance.head())
print(attendance.info())
# Missing values
print(attendance.isnull().sum())

print(attendance["status"].value_counts())
print(attendance[attendance["check_in"].isnull()])
print(attendance.duplicated().sum())
attendance = attendance.drop_duplicates()

print(attendance.duplicated().sum())

print(attendance.shape)
print(attendance.dtypes)
print(attendance.columns.tolist())

print(attendance.dtypes)
print(attendance.isnull().sum())
print(attendance[attendance["check_in"].isnull()]["status"].value_counts())
attendance.to_csv("output/cleaned_attendance.csv", index=False)
