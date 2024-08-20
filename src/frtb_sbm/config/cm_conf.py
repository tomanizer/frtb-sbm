description = """
### Delta Commodities Configuration Summary

#### **Bucket Definitions**

| **Bucket Number** | **Commodity Bucket**                      | **Examples**                                                                                                                 | **Risk Weight** |
|-------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------|
| 1                 | Energy - Solid combustibles               | Coal, Charcoal, Wood pellets, Uranium                                                                                         | 30%             |
| 2                 | Energy - Liquid combustibles              | Light-sweet crude oil, Bioethanol, Propane, Jet fuel, Diesel                                                                  | 35%             |
| 3                 | Energy - Electricity and carbon trading   | Spot electricity, Renewable energy certificates                                                                               | 60%             |
| 4                 | Freight                                   | Capesize, Panamax, Handysize, Supramax, Suezmax, Aframax                                                                      | 80%             |
| 5                 | Metals – Non-precious                     | Aluminium, Copper, Lead, Nickel, Zinc, Steel billet, Cobalt                                                                   | 40%             |
| 6                 | Gaseous combustibles                      | Natural gas, Liquefied natural gas                                                                                            | 45%             |
| 7                 | Precious metals (including gold)          | Gold, Silver, Platinum, Palladium                                                                                             | 20%             |
| 8                 | Grains and oilseed                        | Corn, Wheat, Soybean seed, Palm oil, Canola, Barley, Rice                                                                     | 35%             |
| 9                 | Livestock and dairy                       | Live cattle, Feeder cattle, Hog, Poultry, Milk, Cheese                                                                        | 25%             |
| 10                | Softs and other agriculturals             | Cocoa, Arabica coffee, Tea, Orange juice, Potatoes, Sugar, Cotton, Wool, Rubber                                               | 35%             |
| 11                | Other commodity                           | Potash, Fertilizer, Phosphate rocks, Rare earths, Terephthalic acid, Flat glass                                               | 50%             |

#### **Intra-Bucket Correlations**

| **Bucket Number** | **Correlation (`ρ`)** |
|-------------------|-----------------------|
| 1                 | 55%                   |
| 2                 | 95%                   |
| 3                 | 40%                   |
| 4                 | 80%                   |
| 5                 | 60%                   |
| 6                 | 65%                   |
| 7                 | 55%                   |
| 8                 | 45%                   |
| 9                 | 15%                   |
| 10                | 40%                   |
| 11                | 15%                   |

#### **Inter-Bucket Correlations**

| **From Bucket** | **To Bucket** | **Correlation (`γ_bc`)** |
|-----------------|---------------|--------------------------|
| 1               | 2 to 10       | 20%                      |
| 1               | 11            | 0%                       |
| 2               | 3 to 10       | 20%                      |
| 2               | 11            | 0%                       |
| 3               | 4 to 10       | 20%                      |
| 3               | 11            | 0%                       |
| 4               | 5 to 10       | 20%                      |
| 4               | 11            | 0%                       |
| 5               | 6 to 10       | 20%                      |
| 5               | 11            | 0%                       |
| 6               | 7 to 10       | 20%                      |
| 6               | 11            | 0%                       |
| 7               | 8 to 10       | 20%                      |
| 7               | 11            | 0%                       |
| 8               | 9 to 10       | 20%                      |
| 8               | 11            | 0%                       |
| 9               | 10            | 20%                      |
| 9               | 11            | 0%                       |
| 10              | 11            | 0%                       |

"""

commodities_config = {
    "DeltaCommodities": {
        "BucketDefinitions": {
            1: {"CommodityBucket": "Energy - Solid combustibles", "Examples": ["Coal", "Charcoal", "Wood pellets", "Uranium"], "RiskWeight": 0.30},
            2: {"CommodityBucket": "Energy - Liquid combustibles", "Examples": ["Light-sweet crude oil", "Bioethanol", "Propane", "Jet fuel", "Diesel"], "RiskWeight": 0.35},
            3: {"CommodityBucket": "Energy - Electricity and carbon trading", "Examples": ["Spot electricity", "Renewable energy certificates"], "RiskWeight": 0.60},
            4: {"CommodityBucket": "Freight", "Examples": ["Capesize", "Panamax", "Handysize", "Supramax", "Suezmax", "Aframax"], "RiskWeight": 0.80},
            5: {"CommodityBucket": "Metals – Non-precious", "Examples": ["Aluminium", "Copper", "Lead", "Nickel", "Zinc", "Steel billet", "Cobalt"], "RiskWeight": 0.40},
            6: {"CommodityBucket": "Gaseous combustibles", "Examples": ["Natural gas", "Liquefied natural gas"], "RiskWeight": 0.45},
            7: {"CommodityBucket": "Precious metals (including gold)", "Examples": ["Gold", "Silver", "Platinum", "Palladium"], "RiskWeight": 0.20},
            8: {"CommodityBucket": "Grains and oilseed", "Examples": ["Corn", "Wheat", "Soybean seed", "Palm oil", "Canola", "Barley", "Rice"], "RiskWeight": 0.35},
            9: {"CommodityBucket": "Livestock and dairy", "Examples": ["Live cattle", "Feeder cattle", "Hog", "Poultry", "Milk", "Cheese"], "RiskWeight": 0.25},
            10: {"CommodityBucket": "Softs and other agriculturals", "Examples": ["Cocoa", "Arabica coffee", "Tea", "Orange juice", "Potatoes", "Sugar", "Cotton", "Wool", "Rubber"], "RiskWeight": 0.35},
            11: {"CommodityBucket": "Other commodity", "Examples": ["Potash", "Fertilizer", "Phosphate rocks", "Rare earths", "Terephthalic acid", "Flat glass"], "RiskWeight": 0.50}
        },
        "IntraBucketCorrelations": {
            1: 0.55,
            2: 0.95,
            3: 0.40,
            4: 0.80,
            5: 0.60,
            6: 0.65,
            7: 0.55,
            8: 0.45,
            9: 0.15,
            10: 0.40,
            11: 0.15
        },
        "InterBucketCorrelations": {
            1: {2: 0.20, 3: 0.20, 4: 0.20, 5: 0.20, 6: 0.20, 7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            2: {3: 0.20, 4: 0.20, 5: 0.20, 6: 0.20, 7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            3: {4: 0.20, 5: 0.20, 6: 0.20, 7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            4: {5: 0.20, 6: 0.20, 7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            5: {6: 0.20, 7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            6: {7: 0.20, 8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            7: {8: 0.20, 9: 0.20, 10: 0.20, 11: 0.00},
            8: {9: 0.20, 10: 0.20, 11: 0.00},
            9: {10: 0.20, 11: 0.00},
            10: {11: 0.00},
            11: {}
        }
    }
}
