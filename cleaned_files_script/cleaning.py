import pandas as pd
import numpy as np
employees = pd.read_csv("output/employees.csv")
print(employees.head())
print(employees.shape)
print(employees.columns)
print(employees.info())
print(employees.isnull().sum())
print(employees.duplicated().sum())
print(employees[employees.duplicated()])
employees = employees.drop_duplicates()
print(employees.duplicated().sum())
print(employees.shape)
print(employees.isnull().sum())
employees["phone"] = employees["phone"].fillna("Not Available")

print(employees["phone"].isnull().sum())
employees["email"] = employees["email"].fillna("Not Available")

print(employees["email"].isnull().sum())
median_score = employees["satisfaction_score"].median()

employees["satisfaction_score"] = employees["satisfaction_score"].fillna(median_score)

print(employees["satisfaction_score"].isnull().sum())
print(employees.dtypes)
employees["date_of_joining"] = pd.to_datetime(employees["date_of_joining"])


print(employees["date_of_joining"].dtype)
employees["exit_date"] = pd.to_datetime(employees["exit_date"])

print(employees["exit_date"].dtype)
print(employees["age"].describe())

print(employees[employees["age"] > 60])
print(employees[employees["age"] == 99])
print(employees["experience_years"].describe())

print(employees[employees["experience_years"] > employees["age"]])
print(employees.loc[
    employees["experience_years"] > employees["age"],
    ["employee_id", "age", "experience_years"]
].head(10))

employees = employees[
    employees["experience_years"] <= employees["age"]
]
print(employees.shape)
employees.to_csv("output/cleaned_employees.csv", index=False)
