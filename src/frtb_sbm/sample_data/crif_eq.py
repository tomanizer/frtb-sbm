import pandas as pd
import numpy as np
import os

# Define the number of records per risk type
num_records = 2000

# Common fields
equity_names = ['Apple Inc.', 'Google LLC', 'Microsoft Corp.']
currencies = ['USD', 'EUR', 'GBP']
risk_weights = ['RW1', 'RW2', 'RW3']
equity_types = ['SPOT', 'REPO']
buckets = range(1, 14)

# Function to generate synthetic CRIF data for Equities
def generate_equities_data(risk_type, label1_options, label2_options):
    data = {
        'RiskType': [risk_type] * num_records,
        'Qualifier': np.random.choice(equity_names, num_records),
        'Bucket': np.random.choice(buckets, num_records),
        'Label1': np.random.choice(label1_options, num_records),
        'Label2': np.random.choice(label2_options, num_records),
        'Amount': np.random.uniform(10000, 1000000, num_records),
        'AmountCurrency': np.random.choice(currencies, num_records)
    }
    return pd.DataFrame(data)

# Define specific label options for Equities
delta_label1_options = ['1Y', '5Y', '10Y']
vega_label1_options = ['1M', '6M', '1Y']  # Option maturities
curvature_label1_options = risk_weights

# Generate data for each RiskType
equities_delta_data = generate_equities_data('EQ_DELTA', delta_label1_options, equity_types)
equities_vega_data = generate_equities_data('EQ_VEGA', vega_label1_options, equity_types)
equities_curvature_data = generate_equities_data('EQ_CURVATURE', curvature_label1_options, equity_types)

# Create a directory to save the CSV files
os.makedirs('data', exist_ok=True)

# Save each dataframe as a CSV file
equities_delta_data.to_csv('data/EQ_DELTA.csv', index=False)
equities_vega_data.to_csv('data/EQ_VEGA.csv', index=False)
equities_curvature_data.to_csv('data/EQ_CURVATURE.csv', index=False)

print("Equities data generated and saved as individual CSV files.")
