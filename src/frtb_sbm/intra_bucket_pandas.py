import pandas as pd
import numpy as np

# Define the number of equities
n_equities = 4

# Define the correlation rules based on MAR21
correlations = {
    "same_name_same_type": 1.00,
    "same_name_different_type": 0.995,
    "different_name_same_type": 0.95,
    "different_name_different_type": 0.90
}

# Create a DataFrame representing the equities and their groups
# Here 'Name' represents the underlying name, 'Type' represents the instrument type
data = {
    'Equity': ['Equity1', 'Equity2', 'Equity3', 'Equity4'],
    'Name': ['CompanyA', 'CompanyA', 'CompanyA', 'CompanyB'],
    'Type': ['Type1', 'Type1', 'Type2', 'Type1']
}
df = pd.DataFrame(data)

# Initialize the correlation matrix as a DataFrame with ones on the diagonal
correlation_matrix = pd.DataFrame(np.eye(n_equities), index=df['Equity'], columns=df['Equity'])

# Pairwise comparison using pandas to create masks
name_comparison = df['Name'].values == df['Name'].values[:, None]
type_comparison = df['Type'].values == df['Type'].values[:, None]

# Same Name, Same Type
mask_same_name_same_type = name_comparison & type_comparison

# Same Name, Different Type
mask_same_name_different_type = name_comparison & ~type_comparison

# Different Name, Same Type
mask_different_name_same_type = ~name_comparison & type_comparison

# Different Name, Different Type
mask_different_name_different_type = ~name_comparison & ~type_comparison

# Apply the correlation values based on the masks
correlation_matrix.values[mask_same_name_same_type] = correlations["same_name_same_type"]
correlation_matrix.values[mask_same_name_different_type] = correlations["same_name_different_type"]
correlation_matrix.values[mask_different_name_same
