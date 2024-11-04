import streamlit as st
import pandas as pd
from datetime import date, timedelta
from option_chain import get_option_chain_data
from margin_calculator import calculate_margin_and_premium

def main():
    st.set_page_config(page_title="Option Chain Analysis", layout="wide")
    st.title("Option Chain Analysis")
    
    # Sidebar for inputs
    st.sidebar.header("Parameters")
    
    instrument_options = {
        "Nifty 50": "NSE_INDEX|Nifty 50",
        "Bank Nifty": "NSE_INDEX|Nifty Bank",
        "Reliance": "NSE|RELIANCE"
    }
    
    selected_instrument = st.sidebar.selectbox(
        "Select Instrument",
        list(instrument_options.keys())
    )
    
    # Calculate next few expiry dates (weekly for indexes)
    today = date.today()
    expiry_dates = [
        today + timedelta(days=x) for x in range(30) 
        if (today + timedelta(days=x)).weekday() == 3  # Thursday
    ]
    
    expiry_date = st.sidebar.date_input(
        "Select Expiry Date",
        min_value=today,
        value=expiry_dates[0],
        max_value=today + timedelta(days=90)
    )
    
    option_type = st.sidebar.selectbox(
        "Select Option Type",
        ["CE", "PE"]
    )
    
    if st.sidebar.button("Fetch Data"):
        try:
            with st.spinner("Fetching option chain data..."):
                # Get option chain data
                df = get_option_chain_data(
                    instrument_options[selected_instrument],
                    expiry_date.strftime("%Y-%m-%d"),
                    option_type
                )
                
                # Calculate margins and premiums
                result_df = calculate_margin_and_premium(df)
                
                # Display results
                st.header("Option Chain Analysis Results")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Option Chain Data")
                    st.dataframe(
                        result_df.style.format({
                            'strike_price': '{:.2f}',
                            'bid/ask': '{:.2f}',
                            'margin_required': '{:.2f}',
                            'premium_earned': '{:.2f}'
                        })
                    )
                
                with col2:
                    st.subheader("Summary Statistics")
                    stats = {
                        "Total Premium": result_df['premium_earned'].sum(),
                        "Average Premium": result_df['premium_earned'].mean(),
                        "Total Margin Required": result_df['margin_required'].sum(),
                        "Avg Margin/Premium Ratio": (
                            result_df['margin_required'].sum() / 
                            result_df['premium_earned'].sum()
                        )
                    }
                    
                    for key, value in stats.items():
                        st.metric(key, f"₹{value:,.2f}")
        
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Please check your API credentials and try again.")

if __name__ == "__main__":
    main()