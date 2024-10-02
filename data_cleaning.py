# Import necessary libraries
import pandas as pd
import numpy as np
import re

# Step 1: Load the Data
file_path = '/Users/parsabahrami/Amazon E-Commerce/amazon.csv'
df = pd.read_csv(file_path)

# Step 2: Handle Duplicate Columns
# Check if 'Personalized_Recommendation_Frequency' columns are identical
if 'Personalized_Recommendation_Frequency.1' in df.columns:
    are_identical = df['Personalized_Recommendation_Frequency'].equals(df['Personalized_Recommendation_Frequency.1'])
    if are_identical:
        df = df.drop(columns=['Personalized_Recommendation_Frequency.1'])
    else:
        # If they are not identical, reconcile or decide based on data context
        df['Personalized_Recommendation_Frequency'] = df['Personalized_Recommendation_Frequency'].combine_first(
            df['Personalized_Recommendation_Frequency.1']
        )
        df = df.drop(columns=['Personalized_Recommendation_Frequency.1'])

# Step 3: Convert Data Types
# Remove leading/trailing whitespaces (if any)
df['Timestamp'] = df['Timestamp'].str.strip()

# Remove any invisible characters or control characters
df['Timestamp'] = df['Timestamp'].apply(lambda x: re.sub(r'[\x00-\x1f\x7f-\x9f]', '', x))

# Print some example values from the Timestamp column to diagnose further
print("\nSample values from 'Timestamp' column:")
print(df['Timestamp'].head(10))

# Try a more flexible date parsing approach
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Check how many values were successfully converted
print("\nNumber of valid timestamps after conversion:")
print(df['Timestamp'].notna().sum())

print("\nFirst few rows of the 'Timestamp' column after conversion:")
print(df['Timestamp'].head())

# Step 4: Handle Missing Values
# Fill missing values in categorical columns with a placeholder or mode
df['Product_Search_Method'] = df['Product_Search_Method'].fillna('unknown')

# Step 5: Standardize Categorical Data
# Standardize text data (e.g., converting to lowercase and stripping whitespace)
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].str.lower().str.strip()

# Step 6: Parse and Standardize Multi-Category Columns
# Example for 'Purchase_Categories'
df['Purchase_Categories'] = df['Purchase_Categories'].str.lower().str.split(';')

# Temporarily convert list-like columns back to strings for deduplication
df['Purchase_Categories'] = df['Purchase_Categories'].apply(lambda x: ';'.join(x) if isinstance(x, list) else x)

# Step 7: Handle Outliers
# Remove rows with impossible or improbable 'age' values
df = df[(df['age'] >= 18) & (df['age'] <= 100)]

# Step 8: Remove Duplicate Rows
df = df.drop_duplicates()

# Step 9: Convert List Columns Back After Deduplication
# Reconvert 'Purchase_Categories' to lists
df['Purchase_Categories'] = df['Purchase_Categories'].str.split(';')

# Step 10: Final Check and Save Cleaned Data
print("\nFinal Data Check After Cleaning:")
print(df.info())  # Final check for data types and summary
df.to_csv('/Users/parsabahrami/Amazon E-Commerce/cleaned_amazon.csv', index=False)
print("\nCleaned data has been saved successfully.")
