import pandas as pd

def calculate_margin_and_premium(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate margin requirements and premium earned for option contracts.
    
    Args:
        data (pd.DataFrame): DataFrame containing option data with columns:
            instrument_name, strike_price, side, bid/ask
    
    Returns:
        pd.DataFrame: Input DataFrame with additional columns for margin and premium
    """
    if 'bid/ask' not in data.columns:
        raise ValueError("DataFrame must contain 'bid/ask' column")
    
    # Calculate margin
    def get_margin_required(row):
        strike_price = row['strike_price']
        price = row['bid/ask']
        return strike_price * 0.2 + price * 100  # Example calculation
    
    data['margin_required'] = data.apply(get_margin_required, axis=1)
    
    # Calculate premium earned (lot size is typically 50 for Nifty, 25 for BankNifty)
    LOT_SIZES = {
        "NSE_INDEX|Nifty 50": 50,
        "NSE_INDEX|Nifty Bank": 25
    }
    
    def calculate_premium(row):
        lot_size = LOT_SIZES.get(row['instrument_name'], 50)  # Default to 50 if unknown
        return row['bid/ask'] * lot_size
    
    data['premium_earned'] = data.apply(calculate_premium, axis=1)
    return data
