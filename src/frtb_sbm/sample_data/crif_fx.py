import pandas as pd
import numpy as np
import os

# Define the number of records per risk type
num_records = 2000

# Common fields
currency_pairs = ['USD/EUR', 'GBP/JPY', 'USD/JPY']
currencies = ['USD', 'EUR', 'GBP']
risk_weights = ['RW1', 'RW2', 'RW3']

# Function to generate synthetic CRIF data for FX
def generate_fx_data(risk_type, label1_options, label2_options):
    data = {
        'RiskType': [risk_type] * num_records,
        'Qualifier': np.random.choice(currency_pairs, num_records),
        'Bucket': [None] * num_records,  # FX typically does not use buckets in the same way
        'Label1': np.random.choice(label1_options, num_records),
        'Label2': np.random.choice(label2_options, num_records),
        'Amount': np.random.uniform(10000, 1000000, num_records),
        'AmountCurrency': np.random.choice(currencies, num_records)
    }
    return pd.DataFrame(data)

# Define specific label options for FX
delta_label1_options = [None]  # Not typically used for FX_DELTA
vega_label1_options = ['1M', '6M', '1Y']  # Option maturities
curvature_label1_options = risk_weights

# Generate data for each RiskType
fx_delta_data = generate_fx_data('FX_DELTA', delta_label1_options, [None])
fx_vega_data = generate_fx_data('FX_VEGA', vega_label1_options, [None])
fx_curvature_data = generate_fx_data('FX_CURVATURE', curvature_label1_options, [None])

# Create a directory to save the CSV files
os.makedirs('data', exist_ok=True)

# Save each dataframe as a CSV file
fx_delta_data.to_csv('data/FX_DELTA.csv', index=False)
fx_vega_data.to_csv('data/FX_VEGA.csv', index=False)
fx_curvature_data.to_csv('data/FX_CURVATURE.csv', index=False)

print("FX data generated and saved as individual CSV files.")
