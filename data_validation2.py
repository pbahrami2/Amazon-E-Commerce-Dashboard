import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv('/Users/parsabahrami/Amazon E-Commerce/cleaned_amazon.csv')  # Replace 'cleaned_data.csv' with your actual file path if different

# 1. Convert Timestamp Column to Datetime Format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
print(f"Timestamp column dtype after conversion: {df['Timestamp'].dtypes}\n")

# 2. Check for Missing Values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)
print("\n")

# 3. Split 'Purchase_Categories' into Multiple Columns
# Convert string representations of lists back to actual lists
df['Purchase_Categories'] = df['Purchase_Categories'].apply(eval)

# Use str.get_dummies() to create binary columns for each category
purchase_dummies = df['Purchase_Categories'].str.join('|').str.get_dummies()
df = pd.concat([df, purchase_dummies], axis=1)

print("Columns after splitting 'Purchase_Categories':")
print(df.columns)
print("\n")

# 4. Standardize Categorical Data
# Example for Gender column
df['Gender'] = df['Gender'].str.lower().replace({
    'male': 'male',
    'female': 'female',
    'others': 'others',
    'prefer not to say': 'prefer not to say'
})

# Standardize other columns if needed (e.g., removing leading/trailing spaces, lowercasing, etc.)

# 5. Data Type Verification
print("Data types of each column:")
print(df.dtypes)
print("\n")


# Convert the 'Purchase_Categories' lists to tuples temporarily for duplicate check
df_temp = df.copy()  # Create a temporary copy
df_temp['Purchase_Categories'] = df_temp['Purchase_Categories'].apply(tuple)

# Now check for duplicates
duplicates = df_temp.duplicated().sum()
print(f"Number of duplicate rows after cleaning: {duplicates}\n")

# 7. Visualize Data Distribution for Numerical Columns
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_columns:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# 8. Save the Final Cleaned Data
df.to_csv('/Users/parsabahrami/Amazon E-Commerce/final_cleaned_amazon.csv', index=False)
print("Final cleaned data has been saved successfully as 'final_cleaned_data.csv'.")
