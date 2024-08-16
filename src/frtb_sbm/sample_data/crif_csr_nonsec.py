import pandas as pd
import numpy as np
import os

# Define the number of records per risk type
num_records = 2000

# Common fields
issuer_names = ['Citi Group', 'JP Morgan', 'Goldman Sachs']
currencies = ['USD', 'EUR', 'GBP']
risk_weights = ['RW1', 'RW2', 'RW3']
curve_types = ['Bond', 'CDS']
buckets = range(1, 19)
credit_quality = ['AA+', 'A-', 'BBB+']

# Function to generate synthetic CRIF data for CSR Non-Securitization
def generate_csr_ns_data(risk_type, label1_options, label2_options):
    data = {
        'RiskType': [risk_type] * num_records,
        'Qualifier': np.random.choice(issuer_names, num_records),
        'Bucket': np.random.choice(buckets, num_records),
        'Label1': np.random.choice(label1_options, num_records),
        'Label2': np.random.choice(label2_options, num_records),
        'Amount': np.random.uniform(10000, 1000000, num_records),
        'AmountCurrency': np.random.choice(currencies, num_records),
        'CreditQuality': np.random.choice(credit_quality, num_records)
    }
    return pd.DataFrame(data)

# Define specific label options for CSR Non-Securitization
delta_label1_options = ['1Y', '5Y', '10Y']
vega_label1_options = ['1Y', '5Y', '10Y']  # Option maturities
curvature_label1_options = risk_weights

# Generate data for each RiskType
csr_ns_delta_data = generate_csr_ns_data('CSR_NS_DELTA', delta_label1_options, curve_types)
csr_ns_vega_data = generate_csr_ns_data('CSR_NS_VEGA', vega_label1_options, curve_types)
csr_ns_curvature_data = generate_csr_ns_data('CSR_NS_CURVATURE', curvature_label1_options, curve_types)

# Create a directory to save the CSV files
os.makedirs('data', exist_ok=True)

# Save each dataframe as a CSV file
csr_ns_delta_data.to_csv('data/CSR_NS_DELTA.csv', index=False)
csr_ns_vega_data.to_csv('data/CSR_NS_VEGA.csv', index=False)
csr_ns_curvature_data.to_csv('data/CSR_NS_CURVATURE.csv', index=False)

print("CSR Non-Securitization data generated and saved as individual CSV files.")
