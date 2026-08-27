import pandas as pd

# Load Department Dataset
department = pd.read_csv("output/departments.csv")

# Preview
print(department.head())

# Basic Information
print(department.info())

# Shape
print(department.shape)

# Missing Values
print(department.isnull().sum())

# Duplicate Records
print(department.duplicated().sum())
department.to_csv("output/cleaned_departments.csv", index=False)

print("Department dataset cleaned successfully!")
