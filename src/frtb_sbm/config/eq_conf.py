"""
### Delta Equities Configuration Summary

#### **Bucket Definitions**

| **Bucket Number** | **Market Cap** | **Economy**               | **Sector**                                                                                     |
|-------------------|----------------|---------------------------|------------------------------------------------------------------------------------------------|
| 1                 | Large          | Emerging Market Economy    | Consumer goods and services, transportation and storage, administrative and support service activities, healthcare, utilities |
| 2                 | Large          | Emerging Market Economy    | Telecommunications, industrials                                                                  |
| 3                 | Large          | Emerging Market Economy    | Basic materials, energy, agriculture, manufacturing, mining and quarrying                        |
| 4                 | Large          | Emerging Market Economy    | Financials including government-backed financials, real estate activities, technology            |
| 5                 | Large          | Advanced Economy           | Consumer goods and services, transportation and storage, administrative and support service activities, healthcare, utilities |
| 6                 | Large          | Advanced Economy           | Telecommunications, industrials                                                                  |
| 7                 | Large          | Advanced Economy           | Basic materials, energy, agriculture, manufacturing, mining and quarrying                        |
| 8                 | Large          | Advanced Economy           | Financials including government-backed financials, real estate activities, technology            |
| 9                 | Small          | Emerging Market Economy    | All sectors described under buckets 1, 2, 3, and 4                                               |
| 10                | Small          | Advanced Economy           | All sectors described under buckets 5, 6, 7, and 8                                               |
| 11                | N/A            | Other Sector               | Other sector                                                                                     |
| 12                | Large          | Advanced Economy           | Large market cap, advanced economy equity indices (non-sector specific)                          |
| 13                | N/A            | Other Economy              | Other equity indices (non-sector specific)                                                       |

#### **Risk Weights**

| **Bucket Number** | **Risk Weight for Equity Spot Price** | **Risk Weight for Equity Repo Rate** |
|-------------------|---------------------------------------|--------------------------------------|
| 1                 | 55%                                   | 0.55%                                |
| 2                 | 60%                                   | 0.60%                                |
| 3                 | 45%                                   | 0.45%                                |
| 4                 | 55%                                   | 0.55%                                |
| 5                 | 30%                                   | 0.30%                                |
| 6                 | 35%                                   | 0.35%                                |
| 7                 | 40%                                   | 0.40%                                |
| 8                 | 50%                                   | 0.50%                                |
| 9                 | 70%                                   | 0.70%                                |
| 10                | 50%                                   | 0.50%                                |
| 11                | 70%                                   | 0.70%                                |
| 12                | 15%                                   | 0.15%                                |
| 13                | 25%                                   | 0.25%                                |

#### **Intra-Bucket Correlations**

- **Spot Price and Repo Rate (Same Issuer)**:
  - **Correlation (`ρ`)** = 99.90%

- **Spot Price Correlations**:
  - **Buckets 1, 2, 3, 4 (Large, Emerging Market)**: **15%**
  - **Buckets 5, 6, 7, 8 (Large, Advanced Economy)**: **25%**
  - **Bucket 9 (Small, Emerging Market)**: **7.5%**
  - **Bucket 10 (Small, Advanced Economy)**: **12.5%**
  - **Buckets 12, 13 (Index Buckets)**: **80%**

- **Repo Rate Correlations**:
  - **Same as Spot Price**: Correlation as specified above

- **Spot Price and Repo Rate (Different Issuer)**:
  - **Correlation (`ρ`)** = Specified correlation parameter multiplied by 99.90%

- **Bucket 11 (Other Sector)**:
  - The aggregation is equal to the sum of the absolute values of the net weighted sensitivities.

  
  ### Inter-Bucket Correlations for Delta Equities

The inter-bucket correlations define how risks are aggregated across different equity buckets, according to the following rules:

1. **15% Correlation**:
   - Applies when both buckets fall within bucket numbers 1 to 10.

2. **0% Correlation**:
   - Applies when either bucket is bucket 11.

3. **75% Correlation**:
   - Applies when one bucket is 12 and the other is 13.

4. **45% Correlation**:
   - Applies in all other cases.

#### **Correlation Table**

| **From Bucket** | **To Bucket** | **Correlation** |
|-----------------|---------------|-----------------|
| 1               | 2 to 10       | 15%             |
| 1               | 11            | 0%              |
| 1               | 12, 13        | 45%             |
| 2               | 3 to 10       | 15%             |
| 2               | 11            | 0%              |
| 2               | 12, 13        | 45%             |
| 3               | 4 to 10       | 15%             |
| 3               | 11            | 0%              |
| 3               | 12, 13        | 45%             |
| 4               | 5 to 10       | 15%             |
| 4               | 11            | 0%              |
| 4               | 12, 13        | 45%             |
| 5               | 6 to 10       | 15%             |
| 5               | 11            | 0%              |
| 5               | 12, 13        | 45%             |
| 6               | 7 to 10       | 15%             |
| 6               | 11            | 0%              |
| 6               | 12, 13        | 45%             |
| 7               | 8 to 10       | 15%             |
| 7               | 11            | 0%              |
| 7               | 12, 13        | 45%             |
| 8               | 9, 10         | 15%             |
| 8               | 11            | 0%              |
| 8               | 12, 13        | 45%             |
| 9               | 10            | 15%             |
| 9               | 11            | 0%              |
| 9               | 12, 13        | 45%             |
| 10              | 11            | 0%              |
| 10              | 12, 13        | 45%             |
| 11              | 12, 13        | 0%              |
| 12              | 13            | 75%             |

"""

equities_config = {
    "DeltaEquities": {
        "BucketDefinitions": {
            1: {"MarketCap": "Large", "Economy": "Emerging Market", "Sector": "Consumer goods and services, transportation and storage, administrative and support service activities, healthcare, utilities"},
            2: {"MarketCap": "Large", "Economy": "Emerging Market", "Sector": "Telecommunications, industrials"},
            3: {"MarketCap": "Large", "Economy": "Emerging Market", "Sector": "Basic materials, energy, agriculture, manufacturing, mining and quarrying"},
            4: {"MarketCap": "Large", "Economy": "Emerging Market", "Sector": "Financials including government-backed financials, real estate activities, technology"},
            5: {"MarketCap": "Large", "Economy": "Advanced Economy", "Sector": "Consumer goods and services, transportation and storage, administrative and support service activities, healthcare, utilities"},
            6: {"MarketCap": "Large", "Economy": "Advanced Economy", "Sector": "Telecommunications, industrials"},
            7: {"MarketCap": "Large", "Economy": "Advanced Economy", "Sector": "Basic materials, energy, agriculture, manufacturing, mining and quarrying"},
            8: {"MarketCap": "Large", "Economy": "Advanced Economy", "Sector": "Financials including government-backed financials, real estate activities, technology"},
            9: {"MarketCap": "Small", "Economy": "Emerging Market", "Sector": "All sectors described under buckets 1, 2, 3, and 4"},
            10: {"MarketCap": "Small", "Economy": "Advanced Economy", "Sector": "All sectors described under buckets 5, 6, 7, and 8"},
            11: {"MarketCap": "N/A", "Economy": "Other Sector", "Sector": "Other sector"},
            12: {"MarketCap": "Large", "Economy": "Advanced Economy", "Sector": "Large market cap, advanced economy equity indices (non-sector specific)"},
            13: {"MarketCap": "N/A", "Economy": "Other Economy", "Sector": "Other equity indices (non-sector specific)"}
        },
        "RiskWeights": {
            "SpotPrice": {
                1: 0.55,
                2: 0.60,
                3: 0.45,
                4: 0.55,
                5: 0.30,
                6: 0.35,
                7: 0.40,
                8: 0.50,
                9: 0.70,
                10: 0.50,
                11: 0.70,
                12: 0.15,
                13: 0.25
            },
            "RepoRate": {
                1: 0.0055,
                2: 0.0060,
                3: 0.0045,
                4: 0.0055,
                5: 0.0030,
                6: 0.0035,
                7: 0.0040,
                8: 0.0050,
                9: 0.0070,
                10: 0.0050,
                11: 0.0070,
                12: 0.0015,
                13: 0.0025
            }
        },
        "IntraBucketCorrelations": {
            "SpotPriceRepoRateSameIssuer": 0.999,
            "SpotPrice": {
                1: 0.15,  # Buckets 1-4
                2: 0.15,
                3: 0.15,
                4: 0.15,
                5: 0.25,  # Buckets 5-8
                6: 0.25,
                7: 0.25,
                8: 0.25,
                9: 0.075, # Bucket 9
                10: 0.125, # Bucket 10
                12: 0.8,  # Buckets 12-13
                13: 0.8
            },
            "RepoRate": {
                1: 0.15,  # Buckets 1-4
                2: 0.15,
                3: 0.15,
                4: 0.15,
                5: 0.25,  # Buckets 5-8
                6: 0.25,
                7: 0.25,
                8: 0.25,
                9: 0.075, # Bucket 9
                10: 0.125, # Bucket 10
                12: 0.8,  # Buckets 12-13
                13: 0.8
            },
            "SpotPriceRepoRateDifferentIssuer": {
                1: 0.15 * 0.999,  # Buckets 1-4
                2: 0.15 * 0.999,
                3: 0.15 * 0.999,
                4: 0.15 * 0.999,
                5: 0.25 * 0.999,  # Buckets 5-8
                6: 0.25 * 0.999,
                7: 0.25 * 0.999,
                8: 0.25 * 0.999,
                9: 0.075 * 0.999, # Bucket 9
                10: 0.125 * 0.999, # Bucket 10
                12: 0.8 * 0.999,  # Buckets 12-13
                13: 0.8 * 0.999
            },
            "Bucket11": "Sum of absolute values of net weighted sensitivities"
        },
        "InterBucketCorrelations": {
    1: {2: 0.15, 3: 0.15, 4: 0.15, 5: 0.15, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    2: {3: 0.15, 4: 0.15, 5: 0.15, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    3: {4: 0.15, 5: 0.15, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    4: {5: 0.15, 6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    5: {6: 0.15, 7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    6: {7: 0.15, 8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    7: {8: 0.15, 9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    8: {9: 0.15, 10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    9: {10: 0.15, 11: 0.00, 12: 0.45, 13: 0.45},
    10: {11: 0.00, 12: 0.45, 13: 0.45},
    11: {12: 0.00, 13: 0.00},
    12: {13: 0.75},
}
        }

}
