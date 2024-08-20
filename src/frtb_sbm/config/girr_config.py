delta_girr_config = {
    "DeltaGIRR": {
        "BucketDefinitions": {
            "description": "Each currency is a separate delta GIRR bucket, grouping risk factors in risk-free yield curves.",
            "buckets": "Currencies are treated as separate buckets."
        },
        "RiskWeights": {
            "Standard": {
                "3M": 0.017,
                "6M": 0.017,
                "1Y": 0.016,
                "2Y": 0.013,
                "3Y": 0.012,
                "5Y": 0.011,
                "10Y": 0.011,
                "15Y": 0.011,
                "20Y": 0.011,
                "30Y": 0.011,
                "Inflation": 0.016,
                "Cross_Currency_Basis": 0.016
            },
            "AdjustmentForSpecifiedCurrencies": 0.707
        },
        "IntraBucketCorrelations": {
            "SameTenorDifferentCurve": 0.999,
            "DifferentTenorSameCurve": {
                "correlations": {
                    "3M": {"3M": 1.000, "6M": 0.970, "1Y": 0.914, "2Y": 0.811, "3Y": 0.719, "5Y": 0.566, "10Y": 0.400, "15Y": 0.400, "20Y": 0.400, "30Y": 0.400},
                    "6M": {"3M": 0.970, "6M": 1.000, "1Y": 0.970, "2Y": 0.914, "3Y": 0.861, "5Y": 0.763, "10Y": 0.566, "15Y": 0.419, "20Y": 0.400, "30Y": 0.400},
                    "1Y": {"3M": 0.914, "6M": 0.970, "1Y": 1.000, "2Y": 0.970, "3Y": 0.942, "5Y": 0.887, "10Y": 0.763, "15Y": 0.657, "20Y": 0.566, "30Y": 0.419},
                    "2Y": {"3M": 0.811, "6M": 0.914, "1Y": 0.970, "2Y": 1.000, "3Y": 0.985, "5Y": 0.956, "10Y": 0.887, "15Y": 0.823, "20Y": 0.763, "30Y": 0.657},
                    "3Y": {"3M": 0.719, "6M": 0.861, "1Y": 0.942, "2Y": 0.985, "3Y": 1.000, "5Y": 0.980, "10Y": 0.932, "15Y": 0.887, "20Y": 0.844, "30Y": 0.763},
                    "5Y": {"3M": 0.566, "6M": 0.763, "1Y": 0.887, "2Y": 0.956, "3Y": 0.980, "5Y": 1.000, "10Y": 0.970, "15Y": 0.942, "20Y": 0.914, "30Y": 0.861},
                    "10Y": {"3M": 0.400, "6M": 0.566, "1Y": 0.763, "2Y": 0.887, "3Y": 0.932, "5Y": 0.970, "10Y": 1.000, "15Y": 0.985, "20Y": 0.970, "30Y": 0.942},
                    "15Y": {"3M": 0.400, "6M": 0.419, "1Y": 0.657, "2Y": 0.823, "3Y": 0.887, "5Y": 0.942, "10Y": 0.985, "15Y": 1.000, "20Y": 0.990, "30Y": 0.970},
                    "20Y": {"3M": 0.400, "6M": 0.400, "1Y": 0.566, "2Y": 0.763, "3Y": 0.844, "5Y": 0.914, "10Y": 0.970, "15Y": 0.990, "20Y": 1.000, "30Y": 0.985},
                    "30Y": {"3M": 0.400, "6M": 0.400, "1Y": 0.419, "2Y": 0.657, "3Y": 0.763, "5Y": 0.861, "10Y": 0.942, "15Y": 0.970, "20Y": 0.985, "30Y": 1.000}
                }
            }
        },
        "InterBucketCorrelations": {
            "InflationToYieldCurve": 0.40,
            "CrossCurrencyBasisToYieldCurve": 0.00,
            "CrossCurrencyBasisToInflationCurve": 0.00,
            "CrossCurrencyBasisToCrossCurrencyBasis": 0.00,
            "DifferentCurrencies": 0.50
        }
    }
}