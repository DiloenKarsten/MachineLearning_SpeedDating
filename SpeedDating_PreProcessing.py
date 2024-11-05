import pandas as pd
from scipy.io import arff

# Load ARFF file
data = arff.loadarff('C:/Users/svejr/Downloads/speeddating.arff')
df = pd.DataFrame(data[0])

# Decode byte strings and clean up values
def clean_bytes(val):
    if isinstance(val, bytes):
        val = val.decode('utf-8')  # Convert from byte string to regular string
    if isinstance(val, str) and (val.startswith('[') and val.endswith(']')):
        val = val[1:-1]  # Remove surrounding brackets if they exist
    return val

# Apply the cleaning function to all columns
df = df.map(clean_bytes)

# Save the cleaned DataFrame as CSV
df.to_csv('C:/Users/svejr/Downloads/speeddating_cleaned.csv', index=False)
print("Cleaned CSV file saved.")

print(df.head)
empty_columns = df.columns[df.isnull().any()]
for col in empty_columns:
    
    df[col].median()
    print(f"Column: {col}, Type: {df[col].dtype}, Lenght: {(len(df[col]))}")