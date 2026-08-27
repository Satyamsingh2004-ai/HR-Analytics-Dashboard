import pandas as pd

performance = pd.read_csv("output/performance_reviews.csv")
print(performance.head())
print(performance.info())
print(performance.isnull().sum())
print(performance.duplicated().sum())
print(performance.shape)

performance = performance.drop_duplicates()

print(performance.duplicated().sum())
print(performance.shape)
print(performance["performance_rating"].describe())
print(performance["performance_rating"].value_counts().sort_index())
performance["performance_rating"] = performance["performance_rating"].fillna(3)
print(performance["performance_rating"].isnull().sum())
performance["performance_rating"] = performance["performance_rating"].fillna(3)
print(performance["performance_rating"].isnull().sum())
performance.to_csv("output/cleaned_performance_review.csv", index=False)
print(performance.columns.tolist())