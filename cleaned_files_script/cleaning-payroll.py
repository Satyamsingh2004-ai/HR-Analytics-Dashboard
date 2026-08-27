import pandas as pd

payroll = pd.read_csv("output/payroll.csv")
print(payroll.head())

print(payroll.info())

print(payroll.isnull().sum())

print(payroll.duplicated().sum())
print(payroll.shape)
payroll = payroll.drop_duplicates()

print(payroll.duplicated().sum())

print(payroll.shape)
print(payroll[payroll["net_pay"].isnull()].head())
payroll["net_pay"] = payroll["net_pay"].fillna(
    payroll["basic_salary"] +
    payroll["hra"] +
    payroll["bonus"] -
    payroll["deductions"]
)
print(payroll["net_pay"].isnull().sum())
text_columns = payroll.select_dtypes(include="object").columns

for col in text_columns:
    payroll[col] = payroll[col].str.strip()
    print(payroll.head())
    print((payroll["basic_salary"] < 0).sum())

print((payroll["hra"] < 0).sum())

print((payroll["bonus"] < 0).sum())

print((payroll["deductions"] < 0).sum())

print((payroll["net_pay"] < 0).sum())
payroll["pay_month"] = pd.to_datetime(payroll["pay_month"], format="%Y-%m")
print(payroll.info())
payroll.to_csv("output/clean_payroll.csv", index=False)
