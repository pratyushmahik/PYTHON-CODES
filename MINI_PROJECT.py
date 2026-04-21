
# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 2: LOAD THE DATASET
df = pd.read_csv("illegal_emigration_data.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Fill missing numeric values (if any)
df.fillna(df.mean(numeric_only=True), inplace=True)
print("Filled missing numeric values with column means.")

# Convert categorical columns to category type
categorical_columns = ["Country", "Primary_Route", "Reason_For_Emigration", "Gender"]
for col in categorical_columns:
    df[col] = df[col].astype('category')
    print(f"Converted column '{col}' to category type.")


