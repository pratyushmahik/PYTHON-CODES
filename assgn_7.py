#1.) IMPORTING THE LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2.) LOADING DATASET...
print("\nLoading dataset...")
df = pd.read_csv("illegal_emigration_data.csv")
print("\nDataset Loaded Successfully!")
print(df.head())

# 3.) CHECKING BASIC INFORMATION
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# 4.) HANDLING MISSING VALUES (IF ANY)
df.fillna(df.mean(numeric_only=True), inplace=True)
print("\nMissing numeric values filled using column means.")

# 5.) CONVERTING CATEGORICAL COLUMNS
categorical_columns = [
    "Country",
    "Primary_Route",
    "Reason_For_Emigration",
    "Gender"
]

print("\nConverting categorical columns to category type...")
for col in categorical_columns:
    df[col] = df[col].astype("category")
    print(f"Converted {col} to category type.")

# STEP 6: CORRELATION HEATMAP
print("\nGenerating correlation heatmap...")

plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 6.) VISUALIZATIONS

print("\nDisplaying Age Distribution Histogram...")

plt.figure(figsize=(10, 5))
sns.histplot(df["Average_Age"], bins=20, kde=True)
plt.title("Average Age Distribution of Emigrants")
plt.xlabel("Average Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\nDisplaying Emigration Attempts per Country...")

plt.figure(figsize=(10, 5))
sns.barplot(x="Country", y="Attempt_Count", data=df, estimator=sum)
plt.title("Total Attempt Count per Country")
plt.ylabel("Total Attempts")
plt.tight_layout()
plt.show()

print("\nDisplaying Reason For Emigration Count Plot...")

plt.figure(figsize=(10, 5))
sns.countplot(x="Reason_For_Emigration", data=df)
plt.title("Reason For Emigration Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nDisplaying Pairplot (Relationships Between Variables)...")
sns.pairplot(df, hue="Gender")
plt.show()

print("\nAll graphs displayed successfully!")


print("THANKYOU!!! ")
print("FROM PRATYUSH AND TEAM....!!! ")
