## CSR Non-Securitization CRIF Specification Summary

### RiskType
- `CSR_NS_DELTA`
- `CSR_NS_VEGA`
- `CSR_NS_CURVATURE`

### Qualifier
- **Issuer Name**: The name of the credit issuer, such as 'Citi Group', 'JP Morgan', 'Goldman Sachs'.

### Bucket
- **CSR Non-Sec Bucket**: Specifies the CSR non-securitization bucket number, which ranges from 1 to 18.

### Label1
- **CSR_NS_DELTA**:
  - Tenor (e.g., '1Y', '5Y', '10Y').
- **CSR_NS_VEGA**:
  - Option Maturity (e.g., '1Y', '5Y', '10Y').
- **CSR_NS_CURVATURE**:
  - Risk Weight (e.g., 'RW1', 'RW2', 'RW3').

### Label2
- **Curve Type**: Specifies the risk-factor type, such as 'Bond' or 'CDS'.

### Amount
- **Sensitivity / Shock Up/Down**: The amount of the sensitivity, in the units of the currency specified in the `AmountCurrency` field.
  - **CSR_NS_DELTA** and **CSR_NS_VEGA**: Sensitivity from the applicable regulations (e.g., MAR21.4(1)).
  - **CSR_NS_CURVATURE**: PV shift (delta stripped).

### AmountCurrency
- **Sensitivity Currency**: The currency used in the `Amount` field, such as 'USD', 'EUR', 'GBP'.

### CreditQuality
- **Covered Bond Rating**: Credit rating for covered bonds, where ratings above “AA-” are considered “high” (e.g., 'AA+', 'A-', 'BBB+').
