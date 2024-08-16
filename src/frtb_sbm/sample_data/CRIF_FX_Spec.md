## FX CRIF Specification Summary

### RiskType
- `FX_DELTA`
- `FX_VEGA`
- `FX_CURVATURE`

### Qualifier
- **Currency / Currency Pair**: The name of the currency or currency pair, such as 'USD/EUR', 'GBP/JPY', 'USD/JPY'.

### Bucket
- Typically, FX buckets are not used, so this field can be set as `None` or left empty.

### Label1
- **FX_DELTA**:
  - Not typically used, so this field can be set as `None` or left empty.
- **FX_VEGA**:
  - Option Maturity (e.g., '1M', '6M', '1Y').
- **FX_CURVATURE**:
  - Risk Weight (e.g., 'RW1', 'RW2', 'RW3').

### Label2
- Not typically used for FX, so this field can be set as `None` or left empty.

### Amount
- **Sensitivity / Shock Up/Down**: The amount of the sensitivity, in the units of the currency specified in the `AmountCurrency` field.
  - **FX_DELTA** and **FX_VEGA**: Sensitivity from the applicable regulations.
  - **FX_CURVATURE**: PV shift (delta stripped).

### AmountCurrency
- **Sensitivity Currency**: The currency used in the `Amount` field, such as 'USD', 'EUR', 'GBP'.
