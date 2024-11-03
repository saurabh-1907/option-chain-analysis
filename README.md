Options Chain Analysis Tool
A Python-based tool for analyzing options data and calculating margins using the Upstox API, presented through an interactive Streamlit dashboard.

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
This project provides an intuitive, interactive tool for analyzing options chain data from Indian markets using the Upstox API. It allows users to fetch options chain data for major indices and individual stocks, calculate margins and premiums, and visualize results in an organized dashboard.

Features
Real-time Options Chain Data: Fetches real-time data for options chains using the Upstox API.
Support for Both Calls (CE) and Puts (PE): Analyze both call and put options.
Flexible Expiry Date Selection: Allows the user to select expiry dates for options.
Automatic Margin Calculation: Calculates margin requirements for options based on selected criteria.
Premium Earned Calculation: Calculates potential premiums earned from selling options.
Summary Statistics Display: Provides clear, concise summaries of key data points.
Interactive, User-Friendly Interface: Streamlit-based UI for ease of use and accessibility.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/saurabh-1907/option-chain-analysis.git
cd option-chain-analysis
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up API Credentials:

Create a .env file in the project directory and add your Upstox API credentials:

plaintext
Copy code
UPSTOX_ACCESS_TOKEN=your_access_token_here
Usage
Start the Streamlit Application:

bash
Copy code
streamlit run streamlit_app.py
Open the Application:

Navigate to http://localhost:8501 in your web browser.

Select Analysis Parameters:

Choose an instrument (e.g., Nifty 50, Bank Nifty, Reliance).
Select an expiry date.
Choose the option type (CE for Call or PE for Put).
Fetch Data:

Click on "Fetch Data" to retrieve and analyze options data, view calculated margins, and visualize the results.

Project Structure
plaintext
Copy code
options-chain-analysis/
├── streamlit_app.py          # Main Streamlit application
├── option_chain.py           # Option chain data fetching module
├── margin_calculator.py      # Margin and premium calculations
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (not in repo)
└── README.md                 # Project documentation
Explanation of Key Files
streamlit_app.py: Implements the Streamlit web interface, handles user input, parameter selection, data fetching, calculations, and displays results in an organized, interactive dashboard.
option_chain.py: Manages communication with the Upstox API, processes raw API responses into structured data, and includes error handling and data validation.
margin_calculator.py: Calculates margin requirements and premiums based on selected options data.
Implementation Details
streamlit_app.py:

Implements the Streamlit interface for a responsive, interactive layout.
Handles user input, parameter selection, data fetching, and calculations.
Displays results with formatted numerical displays and an organized, easy-to-navigate layout.
option_chain.py:

Handles communication with the Upstox API.
Processes raw API responses into a structured DataFrame for analysis.
Implements error handling and validation to ensure reliable data.
margin_calculator.py:

Calculates margin requirements for each option, using data from the Upstox API.
Calculates premium earned based on the bid/ask prices and lot size.
Uses a configurable framework for margin and premium calculations.
Development Process & AI Usage
AI tools such as ChatGPT were utilized to optimize and streamline the development process in the following ways:

Code Structure Planning: ChatGPT provided guidance on the optimal project structure, including function signatures and docstrings.
API Integration: Assisted in understanding Upstox API documentation and generating sample API request/response handling code.
Data Processing: Provided guidance on pandas DataFrame operations and optimized data transformation logic.
Error Handling: Generated comprehensive error-handling scenarios and improved exception handling patterns.
Known Limitations
Margin calculations are simplified and may not match exact broker requirements.
Limited to instruments available through the Upstox API.
Weekly expiry dates might not align perfectly with market holidays.
No historical data analysis capabilities currently.
Future Improvements
Support for multiple brokers' APIs.
Historical data analysis for trend insights.
Advanced analytics and visualization options.
Position sizing recommendations based on risk management strategies.
Strategy backtesting capabilities for evaluating option strategies.