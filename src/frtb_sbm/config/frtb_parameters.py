frtb_parameters = {
    "sa.equity.spot-to-repo.correlation": {
        "description": "ρkl in  ",
        "default_value": 0.999
    },
    "sa.equity.large-emerging-market.correlation": {
        "description": "ρkl for Large Market Cap, Emerging Economy buckets in  (a)",
        "default_value": 0.15
    },
    "sa.equity.large-advanced.correlation": {
        "description": "ρkl for Large Market Cap, Advanced Economy buckets in  (b)",
        "default_value": 0.25
    },
    "sa.equity.small-emerging-market.correlation": {
        "description": "ρkl for Small Market Cap, Emerging Economy buckets in  (c)",
        "default_value": 0.075
    },
    "sa.equity.small-advanced.correlation": {
        "description": "ρkl for Small Market Cap, Advanced Economy buckets in  (d)",
        "default_value": 0.125
    },
    "sa.equity.index.correlation": {
        "description": "ρkl for Index buckets in  (e)",
        "default_value": 0.8
    },
    "sa.equity.spot-to-repo.different-issuer.correlation": {
        "description": "ρkl multiplier for Spot × Repo risk-factors in  ",
        "default_value": 0.999
    },
    "sa.equity.delta.gamma.correlation": {
        "description": "γbc between buckets 1-10 in  ",
        "default_value": 0.15
    },
    "sa.equity.delta.gamma.index.correlation": {
        "description": "γbc between index buckets in  ",
        "default_value": 0.75
    },
    "sa.equity.delta.gamma.index-cross.correlation": {
        "description": "γbc between buckets in 1-10 and index buckets in  ",
        "default_value": 0.45
    },
    "sa.vega.rw": {
        "description": "RWσ in [MAR21.92]",
        "default_value": 0.55
    },
    "sa.vega.rw.rounding-dp": {
        "description": "Decimal places in RWk in [MAR21.92]",
        "default_value": 4
    },
    "sa.vega.rho-option-maturity.alpha": {
        "description": "α in  (a)",
        "default_value": 0.01
    }
}

# Example of how to access a parameter and its details
parameter = frtb_parameters["sa.equity.large-advanced.correlation"]
print(f"Description: {parameter['description']}, Default Value: {parameter['default_value']}")
