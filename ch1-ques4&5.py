import os

# Specify the directory path
directory_path = r"C:\Users\praty\OneDrive\Desktop"

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"\nContents of directory '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print("The specified path does not exist or is not a directory.")
