
description = """
### Delta CSR Securitisation (CTP) Configuration Summary

#### **Bucket Definitions**

The bucket structure mirrors the CSR Non-Securitisation framework:

| **Bucket Number** | **Credit Quality**         | **Sector**                                                                                     |
|-------------------|----------------------------|------------------------------------------------------------------------------------------------|
| 1                 | Investment Grade (IG)      | Sovereigns including central banks, multilateral development banks                             |
| 2                 | Investment Grade (IG)      | Local government, government-backed non-financials, education, public administration           |
| 3                 | Investment Grade (IG)      | Financials including government-backed financials                                              |
| 4                 | Investment Grade (IG)      | Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying         |
| 5                 | Investment Grade (IG)      | Consumer goods and services, transportation and storage, administrative and support services   |
| 6                 | Investment Grade (IG)      | Technology, telecommunications                                                                 |
| 7                 | Investment Grade (IG)      | Health care, utilities, professional and technical activities                                  |
| 8                 | Investment Grade (IG)      | Covered bonds                                                                                  |
| 9                 | High Yield (HY) & Non-Rated (NR) | Sovereigns including central banks, multilateral development banks                             |
| 10                | High Yield (HY) & Non-Rated (NR) | Local government, government-backed non-financials, education, public administration           |
| 11                | High Yield (HY) & Non-Rated (NR) | Financials including government-backed financials                                              |
| 12                | High Yield (HY) & Non-Rated (NR) | Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying         |
| 13                | High Yield (HY) & Non-Rated (NR) | Consumer goods and services, transportation and storage, administrative and support services   |
| 14                | High Yield (HY) & Non-Rated (NR) | Technology, telecommunications                                                                 |
| 15                | High Yield (HY) & Non-Rated (NR) | Health care, utilities, professional and technical activities                                  |
| 16                | High Yield (HY) & Non-Rated (NR) | Other sector                                                                                   |

#### **Risk Weights**

Risk weights for CSR Securitisation (CTP) are adjusted to reflect longer liquidity horizons and larger basis risk:

| **Bucket Number** | **Risk Weight** |
|-------------------|-----------------|
| 1                 | 4.0%            |
| 2                 | 4.0%            |
| 3                 | 8.0%            |
| 4                 | 5.0%            |
| 5                 | 4.0%            |
| 6                 | 3.0%            |
| 7                 | 2.0%            |
| 8                 | 6.0%            |
| 9                 | 13.0%           |
| 10                | 13.0%           |
| 11                | 16.0%           |
| 12                | 10.0%           |
| 13                | 12.0%           |
| 14                | 12.0%           |
| 15                | 12.0%           |
| 16                | 13.0%           |

#### **Intra-Bucket Correlations**

- **Buckets 1 to 15**:
  - **Name Correlation**:
    - **1** if the two names of sensitivities \( k \) and \( l \) are identical.
    - **35%** otherwise.
  - **Tenor Correlation**:
    - **1** if the two tenors of the sensitivities \( k \) and \( l \) are identical.
    - **65%** otherwise.
  - **Curve Correlation**:
    - **1** if the two sensitivities are related to the same curves.
    - **99.00%** otherwise (modified from 99.90%).

- **Bucket 16 (Other Sector)**:
  - The aggregation is the simple sum of the absolute values of the net weighted sensitivities.

#### **Inter-Bucket Correlations**

The inter-bucket correlations for Delta CSR Securitisations (CTP) are identical to those for CSR Non-Securitisation:

- **Rating Category Correlation**:
  - **1** if the two buckets have the same rating category.
  - **50%** if the two buckets have different rating categories (IG vs HY/NR).

- **Sector Correlation**:

| **From Bucket** | **To Bucket** | **Correlation** |
|-----------------|---------------|-----------------|
| 1               | 2             | 75%             |
| 1               | 3             | 10%             |
| 1               | 4             | 20%             |
| 1               | 5             | 25%             |
| 1               | 6             | 20%             |
| 1               | 7             | 15%             |
| 1               | 8             | 10%             |
| 1               | 9             | 0%              |
| 1               | 10            | 45%             |
| 1               | 11            | 45%             |
| 1               | 12            | 45%             |
| 1               | 13            | 45%             |
| 1               | 14            | 45%             |
| 1               | 15            | 45%             |
| 1               | 16            | 0%              |
| 2               | 3             | 5%              |
| 2               | 4             | 15%             |
| 2               | 5             | 20%             |
| 2               | 6             | 15%             |
| 2               | 7             | 10%             |
| 2               | 8             | 10%             |
| 2               | 9             | 0%              |
| 2               | 10            | 45%             |
| 2               | 11            | 45%             |
| 2               | 12            | 45%             |
| 2               | 13            | 45%             |
| 2               | 14            | 45%             |
| 2               | 15            | 45%             |
| 2               | 16            | 0%              |
| 3               | 4             | 5%              |
| 3               | 5             | 15%             |
| 3               | 6             | 20%             |
| 3               | 7             | 5%              |
| 3               | 8             | 20%             |
| 3               | 9             | 0%              |
| 3               | 10            | 45%             |
| 3               | 11            | 45%             |
| 3               | 12            | 45%             |
| 3               | 13            | 45%             |
| 3               | 14            | 45%             |
| 3               | 15            | 45%             |
| 3               | 16            | 0%              |
| 4               | 5             | 20%             |
| 4               | 6             | 25%             |
| 4               | 7             | 5%              |
| 4               | 8             | 5%              |
| 4               | 9             | 0%              |
| 4               | 10            | 45%             |
| 4               | 11            | 45%             |
| 4               | 12            | 45%             |
| 4               | 13            | 45%             |
| 4               | 14            | 45%             |
| 4               | 15            | 45%             |
| 4               | 16            | 0%              |
| 5               | 6             | 25%             |
| 5               | 7             | 5%              |
| 5               | 8             | 15%             |
| 5               | 9             | 0%              |
| 5               | 10            | 45%             |
| 5               | 11            | 45%             |
| 5               | 12            | 45%             |
| 5               | 13            | 45%             |
| 5               | 14            | 45%             |
| 5               | 15            | 45%             |
| 5               | 16            | 0%              |
| 6               | 7             | 5%              |
| 6               | 8             | 20%             |
| 6               | 9             | 0%              |
| 6               | 10            | 45%             |
| 6               | 11            | 45%             |
| 6               | 12            | 45%             |
| 6               | 13            | 45%             |
| 6               | 14            | 45%             |
| 6               | 15            | 45%             |
| 6               | 16            | 0%              |
| 7               | 8             | 5%              |
| 7               | 9             | 0%              |
| 7               | 10            | 45%             |
| 7               | 11            | 45%             |
| 7               | 12            | 45%             |
| 7               | 13            | 45%             |
| 7               | 14            | 45%             |
| 7               | 15            | 45%             |
| 7               | 16            | 0%              |
| 8               | 9             | 0%              |
| 8               | 10            | 45%             |
| 8               | 11            | 45%             |
| 8               | 12            | 45%             |
| 8               | 13            | 45%             |
| 8               | 14            | 45%             |
| 8               | 15            | 45%             |
| 8               | 16            | 0%              |
| 9               | 10            | 75%             |
| 9               | 11            | 10%             |
| 9               | 12            | 20%             |
| 9               | 13            | 25%             |
| 9               | 14            | 20%             |
| 9               | 15            | 15%             |
| 9               | 16            | 0%              |
| 10              | 11            | 5%              |
| 10              | 12            | 15%             |
| 10              | 13            | 20%             |
| 10              | 14            | 15%             |
| 10              | 15            | 10%             |
| 10              | 16            | 0%              |
| 11              | 12            | 5%              |
| 11              | 13            | 15%             |
| 11              | 14            | 20%             |
| 11              | 15            | 5%              |
| 11              | 16            | 0%              |
| 12              | 13            | 20%             |
| 12              | 14            | 25%             |
| 12              | 15            | 5%              |
| 12              | 16            | 0%              |
| 13              | 14            | 25%             |
| 13              | 15            | 5%              |
| 13              | 16            | 0%              |
| 14              | 15            | 5%              |
| 14              | 16            | 0%              |
| 15              | 16            | 0%              |
"""

delta_csr_ctp_config = {
    "DeltaCSRSecuritisationCTP": {
        "BucketDefinitions": {
            1: {"CreditQuality": "Investment Grade (IG)", "Sector": "Sovereigns including central banks, multilateral development banks"},
            2: {"CreditQuality": "Investment Grade (IG)", "Sector": "Local government, government-backed non-financials, education, public administration"},
            3: {"CreditQuality": "Investment Grade (IG)", "Sector": "Financials including government-backed financials"},
            4: {"CreditQuality": "Investment Grade (IG)", "Sector": "Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying"},
            5: {"CreditQuality": "Investment Grade (IG)", "Sector": "Consumer goods and services, transportation and storage, administrative and support services"},
            6: {"CreditQuality": "Investment Grade (IG)", "Sector": "Technology, telecommunications"},
            7: {"CreditQuality": "Investment Grade (IG)", "Sector": "Health care, utilities, professional and technical activities"},
            8: {"CreditQuality": "Investment Grade (IG)", "Sector": "Covered bonds"},
            9: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Sovereigns including central banks, multilateral development banks"},
            10: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Local government, government-backed non-financials, education, public administration"},
            11: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Financials including government-backed financials"},
            12: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying"},
            13: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Consumer goods and services, transportation and storage, administrative and support services"},
            14: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Technology, telecommunications"},
            15: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Health care, utilities, professional and technical activities"},
            16: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Other sector"}
        },
        "RiskWeights": {
            1: 0.040,
            2: 0.040,
            3: 0.080,
            4: 0.050,
            5: 0.040,
            6: 0.030,
            7: 0.020,
            8: 0.060,
            9: 0.130,
            10: 0.130,
            11: 0.160,
            12: 0.100,
            13: 0.120,
            14: 0.120,
            15: 0.120,
            16: 0.130
        },
        "IntraBucketCorrelations": {
            "Buckets1to15": {
                "NameCorrelation": {"Identical": 1, "Different": 0.35},
                "TenorCorrelation": {"Identical": 1, "Different": 0.65},
                "CurveCorrelation": {"Identical": 1, "Different": 0.99}  # Modified from 0.999
            },
            "Bucket16": "Sum of absolute values of net weighted sensitivities"
        },
        "InterBucketCorrelations": {
            "RatingCategoryCorrelation": {"SameRating": 1, "DifferentRating": 0.50},
            "SectorCorrelation": {
                1: {"2": 0.75, "3": 0.10, "4": 0.20, "5": 0.25, "6": 0.20, "7": 0.15, "8": 0.10, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                2: {"3": 0.05, "4": 0.15, "5": 0.20, "6": 0.15, "7": 0.10, "8": 0.10, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                3: {"4": 0.05, "5": 0.15, "6": 0.20, "7": 0.05, "8": 0.20, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                4: {"5": 0.20, "6": 0.25, "7": 0.05, "8": 0.05, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                5: {"6": 0.25, "7": 0.05, "8": 0.15, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                6: {"7": 0.05, "8": 0.20, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                7: {"8": 0.05, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                8: {"9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0},
                9: {"10": 0.75, "11": 0.10, "12": 0.20, "13": 0.25, "14": 0.20, "15": 0.15, "16": 0.0},
                10: {"11": 0.05, "12.": 0.15, "13": 0.20, "14": 0.15, "15": 0.10, "16": 0.0},
                11: {"12": 0.05, "13": 0.15, "14": 0.20, "15": 0.05, "16": 0.0},
                12: {"13": 0.20, "14": 0.25, "15": 0.05, "16": 0.0},
                13: {"14": 0.25, "15": 0.05, "16": 0.0},
                14: {"15": 0.05, "16": 0.0},
                15: {"16": 0.0}
            }
        }
    }
}

