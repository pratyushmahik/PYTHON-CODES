# WRITE A PROGRAM TO DATA PREPROCESSING ON .csv/.xls FILE

import pandas as pd

# Input file path
file_path = input("Enter the csv or excel file path: ")

# Conditional reading based on file extension
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
    df = pd.read_excel(file_path)
else:
    print("Unsupported file format.")
    df = pd.DataFrame() # Create an empty DataFrame to prevent errors

# Check if DataFrame is loaded before proceeding
if not df.empty:
    print("\nOriginal Data: ")
    print(df.head())

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill NaN values (using 0 as an example fill value)
    df = df.fillna(0) # Assuming the '0' in your notes means filling NaNs with 0

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv("cleaned_file.csv", index=False) # index=False prevents writing the DataFrame index

    print("\nData Preprocessing Completed !!!")
    print("Cleaned file saved as cleaned_file.csv")
    print("\nCleaned data preview:")
    print(df.head())