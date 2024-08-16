import pandas as pd
import numpy as np
import os

# Define the number of records per risk type
num_records = 2000

# Common fields
commodity_names = ['WTI Crude', 'Brent Crude', 'Gold']
currencies = ['USD', 'EUR', 'GBP']
risk_weights = ['RW1', 'RW2', 'RW3']
locations = ['NYMEX', 'ICE', 'CME']
buckets = range(1, 12)

# Function to generate synthetic CRIF data for Commodities
def generate_commodities_data(risk_type, label1_options, label2_options):
    data = {
        'RiskType': [risk_type] * num_records,
        'Qualifier': np.random.choice(commodity_names, num_records),
        'Bucket': np.random.choice(buckets, num_records),
        'Label1': np.random.choice(label1_options, num_records),
        'Label2': np.random.choice(label2_options, num_records),
        'Amount': np.random.uniform(10000, 1000000, num_records),
        'AmountCurrency': np.random.choice(currencies, num_records)
    }
    return pd.DataFrame(data)

# Define specific label options for Commodities
delta_label1_options = ['1M', '6M', '1Y']
vega_label1_options = ['1M', '6M', '1Y']  # Option maturities
curvature_label1_options = risk_weights

# Generate data for each RiskType
commodities_delta_data = generate_commodities_data('COMM_DELTA', delta_label1_options, locations)
commodities_vega_data = generate_commodities_data('COMM_VEGA', vega_label1_options, locations)
commodities_curvature_data = generate_commodities_data('COMM_CURVATURE', curvature_label1_options, locations)

# Create a directory to save the CSV files
os.makedirs('data', exist_ok=True)

# Save each dataframe as a CSV file
commodities_delta_data.to_csv('data/COMM_DELTA.csv', index=False)
commodities_vega_data.to_csv('data/COMM_VEGA.csv', index=False)
commodities_curvature_data.to_csv('data/COMM_CURVATURE.csv', index=False)

print("Commodities data generated and saved as individual CSV files.")
