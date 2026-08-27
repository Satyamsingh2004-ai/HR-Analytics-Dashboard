import pandas as pd

# Load Job Application Dataset
job = pd.read_csv("output/job_applications.csv")

# Preview
print(job.head())

# Basic Information
print(job.info())

# Shape
print(job.shape)

# Missing Values
print(job.isnull().sum())

# Duplicate Records
print(job.duplicated().sum())
job = job.drop_duplicates()
print(job.duplicated().sum())

# Convert Date Column
job["application_date"] = pd.to_datetime(job["application_date"])

# Check Data Types
print(job.dtypes)

# Save Cleaned Dataset
job.to_csv("output/cleaned_job_applications.csv", index=False)

print("Job Applications dataset cleaned and saved successfully!")
