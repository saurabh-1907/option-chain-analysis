Options Chain Analysis Tool

A Python-based tool for analyzing options data and calculating margins using the Upstox API

Table of Contents

Overview
Features
Installation
Usage
Project Structure
Implementation Details
Development Process & AI Usage
Known Limitations
Future Improvements

Overview
This project implements a Streamlit-based web application for analyzing options chain data from Indian markets. It allows users to fetch option chain data for various instruments (Nifty 50, Bank Nifty, and individual stocks), calculate margins and premiums, and visualize the results in an interactive dashboard.
Features

Real-time options chain data fetching using Upstox API
Support for both Call (CE) and Put (PE) options
Interactive date selection for option expiry
Automatic margin calculation
Premium earned calculations
Summary statistics display
Clean, user-friendly interface

Installation

Clone the repository:

bashCopygit clone https://github.com/saurabh-1907/option-chain-analysis.git
cd options-chain-analysis

Install required dependencies:

bashCopypip install -r requirements.txt

Create a .env file with your Upstox API credentials:

CopyUPSTOX_ACCESS_TOKEN=your_access_token_here
Usage

Start the Streamlit application:

bashCopystreamlit run main.py

Navigate to http://localhost:8501 in your web browser
Select parameters from the sidebar:

Choose an instrument (Nifty 50, Bank Nifty, or Reliance)
Select an expiry date
Choose option type (CE/PE)


Click "Fetch Data" to view the analysis

Project Structure
Copyoptions-chain-analysis/
├── main.py                 # Main Streamlit application
├── option_chain.py         # Option chain data fetching module
├── margin_calculator.py    # Margin and premium calculations
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not in repo)
└── README.md              # Project documentation
Implementation Details
main.py

Implements the Streamlit web interface
Handles user input and parameter selection
Coordinates data fetching and calculations
Displays results in an organized dashboard

Key features:

Responsive layout using Streamlit columns
Error handling for API failures
Dynamic expiry date calculation
Formatted numerical displays

option_chain.py

Handles communication with Upstox API
Processes raw API responses into structured DataFrame
Implements error handling and validation

Key features:

Type hints for better code reliability
Robust error handling for API issues
Data validation before processing

margin_calculator.py

Calculates margin requirements and premiums
Handles different lot sizes for different instruments
Implements business logic for margin calculations

Key features:

Configurable lot sizes per instrument
Extensible margin calculation framework
Premium calculation based on current market prices

Development Process & AI Usage
During development, AI tools were utilized in the following ways:

Code Structure Planning:

Used ChatGPT to discuss optimal project structure
Generated initial function signatures and docstrings


API Integration:

AI helped with understanding Upstox API documentation
Generated sample API request/response handling code


Data Processing:

Received guidance on pandas DataFrame operations
Optimized data transformation logic


Error Handling:

Generated comprehensive error handling scenarios
Improved exception handling patterns



Known Limitations

Margin calculations are simplified and may not match exact broker requirements
Limited to instruments available through Upstox API
Weekly expiry dates might not align perfectly with market holidays
No historical data analysis capabilities currently

Future Improvements

Add support for multiple brokers' APIs
Implement historical data analysis
Add advanced analytics and visualization options
Include position sizing recommendations
Implement strategy backtesting capabilities