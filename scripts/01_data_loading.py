# ======================================
# Import Libraries
# ======================================

import pandas as pd
import numpy as np

# ======================================
# Load Dataset
# ======================================

df = pd.read_csv("data/nigerian_retail_and_ecommerce_cross_channel_sales_data.csv")

print(df.head())

# ======================================
# Data Inspection
# ======================================

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("Columns")
print("=" * 50)
print(df.columns)

print("\nDescriptive Statistics")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nUnique Values:")
print(df.nunique())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Transaction IDs:")
print(df["transaction_id"].duplicated().sum())

# =====================================
# Data Cleaning
# =====================================

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Values Percentage:")
print((df.isnull().sum() / len(df) * 100).sort_values(ascending=False))

print("\nDescriptive Statistics:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include='object'))

print("\nData Shape:")
print(df.shape)

print("\nUnique Values:")
print(df.nunique())