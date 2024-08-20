
"""
### Explanation

- **Risk Class ("Equity")**: The top level of the dictionary is based on the Risk Class, which in this case is "Equity".
- **Market Cap**: The next level differentiates between "Large" and "Small" market cap equities.
- **Liquidity Horizon**: Specifies the Liquidity Horizon (in days) for each Market Cap type. "Large" market cap equities have a Liquidity Horizon of 20 days, while "Small" market cap equities have a Liquidity Horizon of 60 days.
- **Description**: Provides a brief description of each entry for easy reference.
"""

frtb_vega_liquidity_horizons = {
    "Equity": {
        "Large": {
            "LiquidityHorizon": 20,
            "Description": "Large Market Cap Equity with a Liquidity Horizon of 20 days"
        },
        "Small": {
            "LiquidityHorizon": 60,
            "Description": "Small Market Cap Equity with a Liquidity Horizon of 60 days"
        }
    }
}

# Example of how to access a specific liquidity horizon and its details
large_equity_horizon = frtb_vega_liquidity_horizons["Equity"]["Large"]["LiquidityHorizon"]
print(f"Large Market Cap Equity Liquidity Horizon: {large_equity_horizon} days")

small_equity_horizon = frtb_vega_liquidity_horizons["Equity"]["Small"]["LiquidityHorizon"]
print(f"Small Market Cap Equity Liquidity Horizon: {small_equity_horizon} days")
