import pandas as pd

# Specify the path to the MathQA JSON file
dataset_path = "/*/MathQA/test.json"  # Replace with the actual path to your JSON file

# Load the JSON dataset into a DataFrame
df = pd.read_json(dataset_path)

# Print the first few rows of the dataset to explore its contents
print("First few rows of the dataset:")
print(df.head())  # Shows the first 5 rows by default


# Print the column names to understand the structure of the data
print("\nColumn names:")
print(df.columns)

# If the dataset has a 'problem' column, print the first few questions
if 'Problem' in df.columns:
    print("\nFirst few math questions:")
    print(df['Problem'].head())
    
    
