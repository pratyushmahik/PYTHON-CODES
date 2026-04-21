
# STEP 1: IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# STEP 2: LOAD THE UPDATED 100-ROW DATASET
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

# ----------------------------------------------------------
# STEP 5: ENCODE CATEGORICAL COLUMNS
# ----------------------------------------------------------
df_encoded = df.copy()

for col in categorical_columns:
    df_encoded[col] = df_encoded[col].cat.codes

print("\n==== ENCODED DATA HEAD ====")
print(df_encoded.head())

# ----------------------------------------------------------
# STEP 6: CORRELATION HEATMAP
# ----------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ----------------------------------------------------------
# STEP 7: VISUALIZATIONS
# ----------------------------------------------------------

# 1. Gender distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.show()

# 2. Country-wise migration count
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="Country")
plt.xticks(rotation=45)
plt.title("Country-wise Migration Count")
plt.show()

# 3. Age distribution
plt.figure(figsize=(7, 4))
sns.histplot(df["Age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

# ----------------------------------------------------------
# STEP 8: FEATURE SELECTION
# ----------------------------------------------------------
X = df_encoded.drop("Emigration_Count", axis=1)
y = df_encoded["Emigration_Count"]

# ----------------------------------------------------------
# STEP 9: TRAIN-TEST SPLIT
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining and test split done.")

# ----------------------------------------------------------
# STEP 10: TRAIN MODEL (LINEAR REGRESSION)
# ----------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel training completed.")

# ----------------------------------------------------------
# STEP 11: MODEL PREDICTION
# ----------------------------------------------------------
y_pred = model.predict(X_test)

# ----------------------------------------------------------
# STEP 12: MODEL EVALUATION
# ----------------------------------------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n==== MODEL EVALUATION ====")
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# ----------------------------------------------------------
# STEP 13: SHOW ACTUAL VS PREDICTED
# ----------------------------------------------------------
result_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\n==== ACTUAL VS PREDICTED ====")
print(result_df.head())

plt.figure(figsize=(7,4))
plt.plot(result_df["Actual"].values, label="Actual")
plt.plot(result_df["Predicted"].values, label="Predicted")
plt.title("Actual vs Predicted Emigration Count")
plt.legend()
plt.show()

# ----------------------------------------------------------
# END OF PROJECT
# ----------------------------------------------------------

print("\nMini Project Completed Successfully!")