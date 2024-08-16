## Equities CRIF Specification Summary

### RiskType
- `EQ_DELTA`
- `EQ_VEGA`
- `EQ_CURVATURE`

### Qualifier
- **Equity Name**: The name of the equity (issuer), such as 'Apple Inc.', 'Google LLC', 'Microsoft Corp.'

### Bucket
- **Equity Bucket**: Specifies the equity bucket number, which ranges from 1 to 13.

### Label1
- **EQ_DELTA**:
  - Tenor (e.g., '1Y', '5Y', '10Y').
- **EQ_VEGA**:
  - Option Maturity (e.g., '1M', '6M', '1Y').
- **EQ_CURVATURE**:
  - Risk Weight (e.g., 'RW1', 'RW2', 'RW3').

### Label2
- **Equity Type**
  - **EQ_DELTA**: Specifies the type of equity, such as 'SPOT' or 'REPO'.

### Amount
- **Sensitivity / Shock Up/Down**: The amount of the sensitivity, in the units of the currency specified in the `AmountCurrency` field.
  - **EQ_DELTA** and **EQ_VEGA**: Sensitivity from the applicable regulations (e.g., MAR21.4(1)).
  - **EQ_CURVATURE**: PV shift (delta stripped).

### AmountCurrency
- **Sensitivity Currency**: The currency used in the `Amount` field, such as 'USD', 'EUR', 'GBP'.
