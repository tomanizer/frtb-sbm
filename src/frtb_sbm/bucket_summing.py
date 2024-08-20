import numpy as np

# Example intra-bucket capital requirements (in million USD)
K = np.array([100, 150, 200])  # Capital requirements for buckets b, c, d

# Example correlation matrix for the buckets
rho = np.array([
    [1.00, 0.25, 0.20],  # Correlation between b and itself, c, d
    [0.25, 1.00, 0.30],  # Correlation between c and itself, b, d
    [0.20, 0.30, 1.00]   # Correlation between d and itself, b, c
])

# Inter-bucket aggregation formula
K_total = np.sqrt(K @ rho @ K.T)

print(f"Total Capital Requirement: {K_total:.2f} million USD")
