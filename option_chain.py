import requests
import pandas as pd
import streamlit as st
from typing import Optional, Dict, Any

def get_option_chain_data(instrument_name: str, expiry_date: str, side: str) -> pd.DataFrame:
    """
    Fetch option chain data for a given instrument and expiry date.
    """
    ACCESS_TOKEN = st.secrets["UPSTOX_ACCESS_TOKEN"]
    
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': instrument_name,
        'expiry_date': expiry_date
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        entries = []
        for option in data.get('data', []):
            strike_price = option['strike_price']
            if side == "PE":
                price = option['put_options']['market_data']['bid_price']
            else:  # CE
                price = option['call_options']['market_data']['ask_price']
                
            entries.append({
                'instrument_name': data.get('underlying_key', instrument_name),
                'strike_price': strike_price,
                'side': side,
                'bid/ask': price
            })
        
        return pd.DataFrame(entries)
    
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch option chain data: {str(e)}")
