import pandas as pd
import numpy as np

# Load the cleaned dataset
df = pd.read_csv('final_cleaned_amazon.csv')

# Convert 'Timestamp' column to datetime type
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Replace ambiguous values with NaN in certain columns
ambiguous_values = ['.', 'nil', 'NA', 'unknown', 'n/a', 'not specified']

for column in ['Service_Appreciation', 'Improvement_Areas']:
    df[column] = df[column].replace(ambiguous_values, np.nan)

# Standardize text values in columns with inconsistent data
df['Service_Appreciation'] = df['Service_Appreciation'].replace({
    'ui': 'user interface',
    'all the above': 'multiple factors',  # Example standardisation
    # Add more replacements as needed...
})

df['Improvement_Areas'] = df['Improvement_Areas'].replace({
    'ui': 'user interface',
    'user interface of app': 'user interface',
    "i don't have any problem with amazon": 'no problems with amazon',
    # Add more replacements as needed...
})

# Check again for missing values, data types, and duplicates after changes
print("\nMissing values in each column after cleaning:")
print(df.isnull().sum())

print("\nData types of each column after cleaning:")
print(df.dtypes)

print("\nNumber of duplicate rows after cleaning:")
duplicates = df.duplicated().sum()
print(duplicates)

print("\nSummary statistics for numerical columns after cleaning:")
print(df.describe())

print("\nFirst few rows of the dataset after cleaning:")
print(df.head())

print("\nRandom sample of the dataset after cleaning:")
print(df.sample(5))

# Save the cleaned and finalized dataset
df.to_csv('final_cleaned_amazon.csv', index=False)

