import pandas as pd

# Load your dataset
df = pd.read_csv('final_cleaned_amazon.csv')

# Convert the 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Replace missing values in 'Improvement_Areas' with "nothing"
df['Improvement_Areas'].fillna('nothing', inplace=True)

# Replace missing values in 'Service_Appreciation' with "Not Provided"
df['Service_Appreciation'].fillna('Not Provided', inplace=True)

# Check for missing values
print("\nMissing values in each column after handling:")
print(df.isnull().sum())

# Other analysis or saving the dataset
df.to_csv('final_cleaned_amazon.csv', index=False)

