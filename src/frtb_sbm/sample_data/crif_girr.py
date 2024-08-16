import pandas as pd
import numpy as np
import os

# Define the number of records per risk type
num_records = 2000

# Common fields
currencies = ['USD', 'EUR', 'GBP', 'JPY']
risk_weights = ['RW1', 'RW2', 'RW3']

# Function to generate synthetic CRIF data without CalculationMethod
def generate_girr_data(risk_type, label1_options, label2_options):
    data = {
        'RiskType': [risk_type] * num_records,
        'Qualifier': np.random.choice(currencies, num_records),
        'Bucket': [None] * num_records,  # GIRR typically does not use buckets in the same way
        'Label1': np.random.choice(label1_options, num_records),
        'Label2': np.random.choice(label2_options, num_records),
        'Amount': np.random.uniform(10000, 1000000, num_records),
        'AmountCurrency': np.random.choice(currencies, num_records)
    }
    return pd.DataFrame(data)

# Define specific label options for GIRR
delta_label1_options = ['1Y', '5Y', '10Y', 'INFL', 'XCCY']
delta_label2_options = ['OIS USD', 'Libor3m EUR', 'INFL USD', 'XCCY USD']

vega_label1_options = ['1M', '6M', '1Y']  # Option maturities
vega_label2_options = ['2Y', '5Y', 'INFL', 'XCCY']

curvature_label1_options = risk_weights
curvature_label2_options = ['OIS USD', 'Libor3m EUR']


# Generate data for GIRR
girr_delta_data = generate_girr_data('GIRR_DELTA', delta_label1_options, delta_label2_options)
girr_vega_data = generate_girr_data('GIRR_VEGA', vega_label1_options, vega_label2_options)
girr_curvature_data = generate_girr_data('GIRR_CURVATURE', curvature_label1_options, curvature_label2_options)

# Create a directory to save the CSV files
os.makedirs('data', exist_ok=True)

# Save each dataframe as a CSV file
girr_delta_data.to_csv('data/GIRR_DELTA.csv', index=False)
girr_vega_data.to_csv('data/GIRR_VEGA.csv', index=False)
girr_curvature_data.to_csv('data/GIRR_CURVATURE.csv', index=False)

print("GIRR data generated and saved as individual CSV files.")


