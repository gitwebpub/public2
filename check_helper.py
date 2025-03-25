import pandas as pd

# Read the helper file
df = pd.read_excel('/Users/dshin/Dropbox/Lancet/cat101/finishing/helper_5ref.xlsx')

print("Columns in the DataFrame:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

