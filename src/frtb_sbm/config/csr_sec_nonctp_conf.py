description="""
### Delta CSR Securitisation (non-CTP) Configuration Summary

#### **Bucket Definitions**

| **Bucket Number** | **Credit Quality**         | **Sector**                              |
|-------------------|----------------------------|-----------------------------------------|
| 1                 | Senior Investment Grade (IG) | RMBS – Prime                            |
| 2                 | Senior Investment Grade (IG) | RMBS – Mid-prime                        |
| 3                 | Senior Investment Grade (IG) | RMBS – Sub-prime                        |
| 4                 | Senior Investment Grade (IG) | CMBS                                    |
| 5                 | Senior Investment Grade (IG) | ABS – Student loans                     |
| 6                 | Senior Investment Grade (IG) | ABS – Credit cards                      |
| 7                 | Senior Investment Grade (IG) | ABS – Auto                              |
| 8                 | Senior Investment Grade (IG) | CLO non-CTP                             |
| 9                 | Non-Senior Investment Grade (IG) | RMBS – Prime                         |
| 10                | Non-Senior Investment Grade (IG) | RMBS – Mid-prime                     |
| 11                | Non-Senior Investment Grade (IG) | RMBS – Sub-prime                     |
| 12                | Non-Senior Investment Grade (IG) | CMBS                                 |
| 13                | Non-Senior Investment Grade (IG) | ABS – Student loans                  |
| 14                | Non-Senior Investment Grade (IG) | ABS – Credit cards                   |
| 15                | Non-Senior Investment Grade (IG) | ABS – Auto                           |
| 16                | Non-Senior Investment Grade (IG) | CLO non-CTP                          |
| 17                | High Yield & Non-Rated        | RMBS – Prime                           |
| 18                | High Yield & Non-Rated        | RMBS – Mid-prime                       |
| 19                | High Yield & Non-Rated        | RMBS – Sub-prime                       |
| 20                | High Yield & Non-Rated        | CMBS                                   |
| 21                | High Yield & Non-Rated        | ABS – Student loans                    |
| 22                | High Yield & Non-Rated        | ABS – Credit cards                     |
| 23                | High Yield & Non-Rated        | ABS – Auto                             |
| 24                | High Yield & Non-Rated        | CLO non-CTP                            |
| 25                | High Yield & Non-Rated        | Other sector                           |

#### **Risk Weights**

| **Bucket Number** | **Risk Weight** | **Calculation** |
|-------------------|-----------------|-----------------|
| 1                 | 0.9%            | Given           |
| 2                 | 1.5%            | Given           |
| 3                 | 2.0%            | Given           |
| 4                 | 2.0%            | Given           |
| 5                 | 0.8%            | Given           |
| 6                 | 1.2%            | Given           |
| 7                 | 1.2%            | Given           |
| 8                 | 1.4%            | Given           |
| 9                 | 1.125%          | 0.9% × 1.25     |
| 10                | 1.875%          | 1.5% × 1.25     |
| 11                | 2.5%            | 2.0% × 1.25     |
| 12                | 2.5%            | 2.0% × 1.25     |
| 13                | 1.0%            | 0.8% × 1.25     |
| 14                | 1.5%            | 1.2% × 1.25     |
| 15                | 1.5%            | 1.2% × 1.25     |
| 16                | 1.75%           | 1.4% × 1.25     |
| 17                | 1.575%          | 0.9% × 1.75     |
| 18                | 2.625%          | 1.5% × 1.75     |
| 19                | 3.5%            | 2.0% × 1.75     |
| 20                | 3.5%            | 2.0% × 1.75     |
| 21                | 1.4%            | 0.8% × 1.75     |
| 22                | 2.1%            | 1.2% × 1.75     |
| 23                | 2.1%            | 1.2% × 1.75     |
| 24                | 2.45%           | 1.4% × 1.75     |
| 25                | 3.5%            | Given           |

#### **Intra-Bucket Correlations**

- **Buckets 1 to 24**:
  - **Name Correlation (`ρ_name`)**:
    - **1** if the two names of sensitivities \( k \) and \( l \) are related to the same securitisation tranche (more than 80% overlap in notional terms).
    - **40%** otherwise.
  - **Tenor Correlation (`ρ_tenor`)**:
    - **1** if the two tenors of the sensitivities \( k \) and \( l \) are identical.
    - **80%** otherwise.
  - **Curve Correlation (`ρ_curve`)**:
    - **1** if the two sensitivities are related to the same curves.
    - **99.90%** otherwise.

- **Bucket 25 (Other Sector)**:
  - The aggregation of risk positions is equal to the simple sum of the absolute values of the net weighted sensitivities.

#### **Inter-Bucket Correlations**

- **Inter-Bucket Correlation (`ρ_bc`)**: Set to **0%** across all buckets (1 to 24).
- **Inter-Bucket Correlation (`ρ_bc`)**: Set to **40%** for Bucket 25 (Other Sector)."""


delta_csr_non_ctp_config = {
    "DeltaCSRSecuritisationNonCTP": {
        "BucketDefinitions": {
            1: {"CreditQuality": "Senior IG", "Sector": "RMBS – Prime"},
            2: {"CreditQuality": "Senior IG", "Sector": "RMBS – Mid-prime"},
            3: {"CreditQuality": "Senior IG", "Sector": "RMBS – Sub-prime"},
            4: {"CreditQuality": "Senior IG", "Sector": "CMBS"},
            5: {"CreditQuality": "Senior IG", "Sector": "ABS – Student loans"},
            6: {"CreditQuality": "Senior IG", "Sector": "ABS – Credit cards"},
            7: {"CreditQuality": "Senior IG", "Sector": "ABS – Auto"},
            8: {"CreditQuality": "Senior IG", "Sector": "CLO non-CTP"},
            9: {"CreditQuality": "Non-Senior IG", "Sector": "RMBS – Prime"},
            10: {"CreditQuality": "Non-Senior IG", "Sector": "RMBS – Mid-prime"},
            11: {"CreditQuality": "Non-Senior IG", "Sector": "RMBS – Sub-prime"},
            12: {"CreditQuality": "Non-Senior IG", "Sector": "CMBS"},
            13: {"CreditQuality": "Non-Senior IG", "Sector": "ABS – Student loans"},
            14: {"CreditQuality": "Non-Senior IG", "Sector": "ABS – Credit cards"},
            15: {"CreditQuality": "Non-Senior IG", "Sector": "ABS – Auto"},
            16: {"CreditQuality": "Non-Senior IG", "Sector": "CLO non-CTP"},
            17: {"CreditQuality": "High Yield & Non-Rated", "Sector": "RMBS – Prime"},
            18: {"CreditQuality": "High Yield & Non-Rated", "Sector": "RMBS – Mid-prime"},
            19: {"CreditQuality": "High Yield & Non-Rated", "Sector": "RMBS – Sub-prime"},
            20: {"CreditQuality": "High Yield & Non-Rated", "Sector": "CMBS"},
            21: {"CreditQuality": "High Yield & Non-Rated", "Sector": "ABS – Student loans"},
            22: {"CreditQuality": "High Yield & Non-Rated", "Sector": "ABS – Credit cards"},
            23: {"CreditQuality": "High Yield & Non-Rated", "Sector": "ABS – Auto"},
            24: {"CreditQuality": "High Yield & Non-Rated", "Sector": "CLO non-CTP"},
            25: {"CreditQuality": "High Yield & Non-Rated", "Sector": "Other sector"}
        },
        "RiskWeights": {
            1: 0.009,
            2: 0.015,
            3: 0.020,
            4: 0.020,
            5: 0.008,
            6: 0.012,
            7: 0.012,
            8: 0.014,
            9: 0.01125,
            10: 0.01875,
            11: 0.025,
            12: 0.025,
            13: 0.01,
            14: 0.015,
            15: 0.015,
            16: 0.0175,
            17: 0.01575,
            18: 0.02625,
            19: 0.035,
            20: 0.035,
            21: 0.014,
            22: 0.021,
            23: 0.021,
            24: 0.0245,
            25: 0.035
        },
        "IntraBucketCorrelations": {
            "Buckets1to24": {
                "NameCorrelation": {"SameTranche": 1, "DifferentTranche": 0.40},
                "TenorCorrelation": {"Identical": 1, "Different": 0.80},
                "CurveCorrelation": {"Identical": 1, "Different": 0.999}
            },
            "Bucket25": "Sum of absolute values of net weighted sensitivities"
        },
        "InterBucketCorrelations": {
            1: {2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            2: {3: 0.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            3: {4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            4: {5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            5: {6: 0.0, 7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            6: {7: 0.0, 8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            7: {8: 0.0, 9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            8: {9: 0.0, 10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            9: {10: 0.0, 11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            10: {11: 0.0, 12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            11: {12: 0.0, 13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            12: {13: 0.0, 14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            13: {14: 0.0, 15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            14: {15: 0.0, 16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            15: {16: 0.0, 17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            16: {17: 0.0, 18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            17: {18: 0.0, 19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            18: {19: 0.0, 20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            19: {20: 0.0, 21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            20: {21: 0.0, 22: 0.0, 23: 0.0, 24: 0.0},
            21: {22: 0.0, 23: 0.0, 24: 0.0},
            22: {23: 0.0, 24: 0.0},
            23: {24: 0.0},
        }
    }
}
