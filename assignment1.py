#Assignment 1 - Anuprash Pokharel

import pandas as pd

# 1. Read the CSV File
df = pd.read_csv("pandas_dataset.csv")
print("First 5 rows:")
print(df.head())

# 2. Rename Columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("\nCleaned Column Names:")
print(df.columns.tolist())

# 3. Drop Unnecessary Rows      
df = df.dropna(how="all").reset_index(drop=True)
  
# 4. Drop Columns (if needed)
#No columns are dropped.

# 5. Count Missing Values
print("\nMissing values per column:")
print(df.isnull().sum())   

# 6. Handle Missing Values
df = df.dropna(subset=["sales"]).copy()
profit_mean = df["profit"].mean()
discount_median = df["discount"].median()
df["profit"] = df["profit"].fillna(profit_mean)
df["discount"] = df["discount"].fillna(discount_median)

# 7. Handle Missing Categorical Data
df["customer_name"] = df["customer_name"].fillna("Unknown")

# 8. Detect and Remove Duplicates
duplicate_count = df.duplicated(subset=["order_id"]).sum()
print(f"\nNumber of duplicate rows found based on order_id: {duplicate_count}")
df = df.drop_duplicates(subset=["order_id"], keep="first").reset_index(
    drop=True
)

# 9. Filtering and Creating New Columns
high_price = df[df["unit_price"] > 20000]
print("\nOrders with unit_price > 20,000:")
print(high_price[["order_id", "customer_name", "product", "unit_price"]])
filtered = df[(df["unit_price"] > 10000) & (df["status"] == "Completed")][
    ["customer_name", "category", "status"]
]
print(
    "\nCompleted orders with unit_price > 10,000 (customer_name, category, status):"
)
print(filtered)
df["total_amount"] = (df["quantity"] * df["unit_price"]) - df["discount"]
df["customer_type"] = df["quantity"].apply(
    lambda qty: "Bulk Buyer" if qty >= 3 else "Regular Buyer"
)

# 10. Final Clean Dataset Output
print(f"\nShape of dataset before cleaning: (27, 12)")
print(f"Shape of dataset after cleaning: {df.shape}")
print("\nFirst 10 rows of cleaned dataset:")
print(df.head(10))