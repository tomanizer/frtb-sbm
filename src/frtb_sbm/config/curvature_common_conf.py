curvature_common_config = {
    "CurvatureCommon": {
        "IntraBucketCorrelationsMethod": "SquareDeltaCorrelations",  # Method for intra-bucket correlations
        "InterBucketCorrelationsMethod": "SquareDeltaCorrelations",  # Method for inter-bucket correlations
        "CurvatureRiskWeightMethod": "UseDeltaRiskWeight",           # General method for determining curvature risk weights
        "FXAdjustmentFactor": 1.5,                                   # Scalar for FX curvature adjustments
        "ParallelShiftMethod": "UseHighestDeltaRiskWeight",          # Method for parallel shifts (GIRR, CSR, Commodities)
        "UseAdjustedFXWeights": True,                                # Option to adjust FX curvature using the scalar
        "HighLowCorrelationScenario": {
            "IntraBucketCorrelations": "ApplySquaredCorrelations",   # Apply squared correlations in high/low scenarios
            "InterBucketCorrelations": "ApplySquaredCorrelations"    # Apply squared correlations in high/low scenarios
        }
    }
}

gir_config = {
    "CurvatureGIRR": {
        "UseCommon": True,
        "SpecificRiskWeights": {
            "BucketDefinitions": {
                1: {"Currency": "USD", "HighestDeltaRiskWeight": 1.7},
                2: {"Currency": "EUR", "HighestDeltaRiskWeight": 1.7},
                # Continue for other currencies
            }
        }
    }
}
