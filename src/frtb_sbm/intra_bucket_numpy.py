import numpy as np

# Number of equities (risk factors)
n_equities = 4

# Define the correlation rules based on MAR21
correlations = {
    "same_name_same_type": 1.00,
    "same_name_different_type": 0.995,
    "different_name_same_type": 0.95,
    "different_name_different_type": 0.90
}

# Define the groups for the equities
group = np.array([1, 1, 2, 3])  # Group assignment for each equity

# Initialize the correlation matrix with ones on the diagonal
correlation_matrix = np.eye(n_equities)

# Same Name, Same Type
mask_same_name_same_type = (group[:, None] == group[None, :]) & (group == 1)
correlation_matrix[mask_same_name_same_type] = correlations["same_name_same_type"]

# Same Name, Different Type
mask_same_name_different_type = (group[:, None] != group[None, :]) & ((group == 1) | (group == 2))
correlation_matrix[mask_same_name_different_type] = correlations["same_name_different_type"]

# Different Name, Same Type
mask_different_name_same_type = (group[:, None] == 2) & (group[None, :] == 3) | (group[:, None] == 3) & (group[None, :] == 2)
correlation_matrix[mask_different_name_same_type] = correlations["different_name_same_type"]

# Different Name, Different Type
mask_different_name_different_type = (group[:, None] != group[None, :]) & (group != 1) & (group != 2)
correlation_matrix[mask_different_name_different_type] = correlations["different_name_different_type"]

# Print the correlation matrix
print("Intra-Bucket Correlation Matrix:")
print(correlation_matrix)
