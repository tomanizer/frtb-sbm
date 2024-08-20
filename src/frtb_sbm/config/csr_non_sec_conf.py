description = """
### Delta CSR Non-Securitisations Configuration Summary

#### **Bucket Definitions**
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
| 17                | Investment Grade (IG)      | IG indices                                                                                     |
| 18                | High Yield (HY)            | HY indices                                                                                      |

#### **Risk Weights**
| **Bucket Number** | **Risk Weight** |
|-------------------|-----------------|
| 1                 | 0.5%            |
| 2                 | 1.0%            |
| 3                 | 5.0%            |
| 4                 | 3.0%            |
| 5                 | 3.0%            |
| 6                 | 2.0%            |
| 7                 | 1.5%            |
| 8                 | 2.5%            |
| 9                 | 2.0%            |
| 10                | 4.0%            |
| 11                | 12.0%           |
| 12                | 7.0%            |
| 13                | 8.5%            |
| 14                | 5.5%            |
| 15                | 5.0%            |
| 16                | 12.0%           |
| 17                | 1.5%            |
| 18                | 5.0%            |

#### **Intra-Bucket Correlations**

- **Buckets 1 to 15**:
  - **Name Correlation**:
    - 1 if the two names of sensitivities are identical.
    - 35% otherwise.
  - **Tenor Correlation**:
    - 1 if the two tenors are identical.
    - 65% otherwise.
  - **Curve Correlation**:
    - 1 if the two sensitivities are related to the same curves.
    - 99.90% otherwise.

- **Buckets 17 and 18**:
  - **Name Correlation**:
    - 1 if the two names of sensitivities are identical.
    - 80% otherwise.
  - **Tenor Correlation**:
    - 1 if the two tenors are identical.
    - 65% otherwise.
  - **Curve Correlation**:
    - 1 if the two sensitivities are related to the same curves.
    - 99.90% otherwise.

- **Bucket 16 (Other Sector)**:
  - The aggregation is the simple sum of the absolute values of the net weighted sensitivities.

#### **Inter-Bucket Correlations**

- **Rating Category Correlation**:
  - 1 if the two buckets have the same rating category.
  - 50% if the two buckets have different rating categories (IG vs HY/NR).

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
| 1               | 17            | 45%             |
| 1               | 18            | 45%             |
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
| 2               | 17            | 45%             |
| 2               | 18            | 45%             |
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
| 3               | 17            | 45%             |
| 3               | 18            | 45%             |
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
| 4               | 17            | 45%             |
| 4               | 18            | 45%             |
| 5               | 6             | 25%             |
| 5               | 7             | 5%              |
| 5               | 8             | 15%             |
| 5               | 9             | 0%              |
| 5               | 10            | 45%             |
| 5               | 11            | 45%             |
| 5               | 12            | 45%             |
| 5              
"""


delta_csr_ns_config = {
    "DeltaCSRNonSecuritisations": {
        "BucketDefinitions": {
            1: {"CreditQuality": "Investment Grade (IG)", "Sector": "Sovereigns including central banks, multilateral development banks"},
            2: {"CreditQuality": "Investment Grade (IG)", "Sector": "Local government, government-backed non-financials, education, public administration"},
            3: {"CreditQuality": "Investment Grade (IG)", "Sector": "Financials including government-backed financials"},
            4: {"CreditQuality": "Investment Grade (IG)", "Sector": "Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying"},
            5: {"CreditQuality": "Investment Grade (IG)", "Sector": "Consumer goods and services, transportation and storage, administrative and support service activities"},
            6: {"CreditQuality": "Investment Grade (IG)", "Sector": "Technology, telecommunications"},
            7: {"CreditQuality": "Investment Grade (IG)", "Sector": "Health care, utilities, professional and technical activities"},
            8: {"CreditQuality": "Investment Grade (IG)", "Sector": "Covered bonds"},
            9: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Sovereigns including central banks, multilateral development banks"},
            10: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Local government, government-backed non-financials, education, public administration"},
            11: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Financials including government-backed financials"},
            12: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Basic materials, energy, industrials, agriculture, manufacturing, mining and quarrying"},
            13: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Consumer goods and services, transportation and storage, administrative and support service activities"},
            14: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Technology, telecommunications"},
            15: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Health care, utilities, professional and technical activities"},
            16: {"CreditQuality": "High Yield (HY) & Non-Rated (NR)", "Sector": "Other sector"},
            17: {"CreditQuality": "Investment Grade (IG)", "Sector": "IG indices"},
            18: {"CreditQuality": "High Yield (HY)", "Sector": "HY indices"}
        },
        "RiskWeights": {
            1: 0.005,
            2: 0.010,
            3: 0.050,
            4: 0.030,
            5: 0.030,
            6: 0.020,
            7: 0.015,
            8: 0.025,
            9: 0.020,
            10: 0.040,
            11: 0.120,
            12: 0.070,
            13: 0.085,
            14: 0.055,
            15: 0.050,
            16: 0.120,
            17: 0.015,
            18: 0.050
        },
        "IntraBucketCorrelations": {
            "Buckets1to15": {
                "NameCorrelation": {"Identical": 1, "Different": 0.35},
                "TenorCorrelation": {"Identical": 1, "Different": 0.65},
                "CurveCorrelation": {"Identical": 1, "Different": 0.999}
            },
            "Buckets17and18": {
                "NameCorrelation": {"Identical": 1, "Different": 0.80},
                "TenorCorrelation": {"Identical": 1, "Different": 0.65},
                "CurveCorrelation": {"Identical": 1, "Different": 0.999}
            },
            "Bucket16": "Sum of absolute values of net weighted sensitivities"
        },
        "InterBucketCorrelations": {
            "RatingCategoryCorrelation": {"SameRating": 1, "DifferentRating": 0.50},
            "SectorCorrelation": {
                1: {"2": 0.75, "3": 0.10, "4": 0.20, "5": 0.25, "6": 0.20, "7": 0.15, "8": 0.10, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                2: {"3": 0.05, "4": 0.15, "5": 0.20, "6": 0.15, "7": 0.10, "8": 0.10, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                3: {"4": 0.05, "5": 0.15, "6": 0.20, "7": 0.05, "8": 0.20, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                4: {"5": 0.20, "6": 0.25, "7": 0.05, "8": 0.05, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                5: {"6": 0.25, "7": 0.05, "8": 0.15, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                6: {"7": 0.05, "8": 0.20, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                7: {"8": 0.05, "9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                8: {"9": 0.0, "10": 0.45, "11": 0.45, "12": 0.45, "13": 0.45, "14": 0.45, "15": 0.45, "16": 0.0, "17": 0.45, "18": 0.45},
                9: {"10": 0.75, "11": 0.10, "12": 0.20, "13": 0.25, "14": 0.20, "15": 0.15, "16": 0.0, "17": 0.45, "18": 0.45},
                10: {"11": 0.05, "12": 0.15, "13": 0.20, "14": 0.15, "15": 0.10, "16": 0.0, "17": 0.45, "18": 0.45},
                11: {"12": 0.05, "13": 0.15, "14": 0.20, "15": 0.05, "16": 0.0, "17": 0.45, "18": 0.45},
                12: {"13": 0.20, "14": 0.25, "15": 0.05, "16": 0.0, "17": 0.45, "18": 0.45},
                13: {"14": 0.25, "15": 0.05, "16": 0.0, "17": 0.45, "18": 0.45},
                14: {"15": 0.05, "16": 0.0, "17": 0.45, "18": 0.45},
                15: {"16": 0.0, "17": 0.45, "18": 0.45},
                16: {"17": 0.0, "18": 0.0},
                17: {"18": 0.75}
            }
        }
    }
}
