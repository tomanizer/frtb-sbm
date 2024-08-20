## Commodities CRIF Specification Summary

### RiskType
- `COMM_DELTA`
- `COMM_VEGA`
- `COMM_CURVATURE`

### Qualifier
- **Commodity Name**: The name of the commodity, such as 'WTI Crude', 'Brent Crude', 'Gold'.

### Bucket
- **Commodity Bucket**: Specifies the commodity bucket number, which ranges from 1 to 11.

### Label1
- **COMM_DELTA**:
  - Tenor (e.g., '1M', '6M', '1Y').
- **COMM_VEGA**:
  - Option Maturity (e.g., '1M', '6M', '1Y').
- **COMM_CURVATURE**:
  - Risk Weight (e.g., 'RW1', 'RW2', 'RW3').

### Label2
- **Commodity Location**: Specifies the delivery location of the commodity, such as 'NYMEX', 'ICE', 'CME'.

### Amount
- **Sensitivity / Shock Up/Down**: The amount of the sensitivity, in the units of the currency specified in the `AmountCurrency` field.
  - **COMM_DELTA** and **COMM_VEGA**: Sensitivity from the applicable regulations (e.g., MAR21.4(1)).
  - **COMM_CURVATURE**: PV shift (delta stripped).

### AmountCurrency
- **Sensitivity Currency**: The currency used in the `Amount` field, such as 'USD', 'EUR', 'GBP'.


