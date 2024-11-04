# **Options Chain Analysis Tool**

A Python-based tool for analyzing options data and calculating margins using the **Upstox API** on an interactive **Streamlit dashboard**. Deployed on Streamlit Cloud for easy access.

---

## **Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Local Setup](#local-setup)
4. [Cloud Deployment](#cloud-deployment)
5. [Project Structure](#project-structure)
6. [Implementation Details](#implementation-details)
7. [Development Process & AI Usage](#development-process--ai-usage)
8. [Known Limitations](#known-limitations)
9. [Future Improvements](#future-improvements)

---

## **Overview**

This project provides an interactive tool to analyze **options chain data from Indian markets**. It utilizes the **Upstox API** to fetch options data for **major indices and individual stocks**, calculates **margins and premiums**, and displays the results in an organized **Streamlit dashboard**.

---

## **Features**

- **Real-time Options Chain Data**: Fetch real-time data for options chains using the Upstox API
- **Support for Call (CE) and Put (PE) Options**: Analyze both call and put options
- **Flexible Expiry Date Selection**: Choose from available expiry dates
- **Automatic Margin Calculation**: Calculates margin requirements for options
- **Premium Earned Calculation**: Calculates potential premiums
- **Summary Statistics Display**: Provides key data points concisely
- **Interactive User Interface**: Built on Streamlit for an intuitive, accessible experience
- **Cloud Deployment**: Easily deployable on Streamlit Cloud

---

## **Local Setup**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/option-chain-analysis.git
    cd option-chain-analysis
    ```

2. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Streamlit Secrets**:
    Create `.streamlit/secrets.toml` in your project directory:
    ```toml
    UPSTOX_ACCESS_TOKEN = "your_access_token_here"
    ```

4. **Run Locally**:
    ```bash
    streamlit run main.py
    ```

---

## **Cloud Deployment**

1. **Prepare for Deployment**:
   - Ensure your code is in a GitHub repository
   - Make sure `.streamlit/secrets.toml` is in `.gitignore`
   - Verify all dependencies are in `requirements.txt`

2. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set up your secrets in Streamlit Cloud:
     - Navigate to your app's settings
     - Add your `UPSTOX_ACCESS_TOKEN` in the Secrets section
   - Deploy your app

3. **Access Your App**:
   - Your app will be available at a custom Streamlit URL
   - Share the URL with your team or users

---

## **Project Structure**
```plaintext
option-chain-analysis/
├── .gitignore                # Git ignore file
├── .streamlit/              
│   └── secrets.toml         # Local secrets (not in repo)
├── main.py                  # Main Streamlit application
├── option_chain.py          # Option chain data fetching module
├── margin_calculator.py     # Margin and premium calculations
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

### **Explanation of Key Files**

- **`main.py`**: Implements the **Streamlit interface** and handles **user input** and **data display**
- **`option_chain.py`**: Communicates with **Upstox API**, processes API responses, and includes **error handling**
- **`margin_calculator.py`**: Calculates **margin requirements** and **premium earnings** based on the selected options data
- **`.streamlit/secrets.toml`**: Stores sensitive configuration (local development only)

---

## **Implementation Details**

1. **`main.py`**
   - **Implements Streamlit Interface** for an interactive layout
   - **Handles User Input** and **Displays Results** with an organized layout
   - Uses Streamlit secrets for secure configuration

2. **`option_chain.py`**
   - **Fetches and Structures Options Data** using the **Upstox API**
   - **Error Handling** and **Data Validation** ensure reliable data
   - Accesses API token securely via Streamlit secrets

3. **`margin_calculator.py`**
   - **Calculates Margins and Premiums** for each option contract
   - **Configurable Framework** for flexible margin calculations

---

## **Development Process & AI Usage**

**AI tools** like **ChatGPT** were used to:
- Design the project structure and generate initial code
- Implement Streamlit best practices
- Optimize data processing with pandas
- Implement comprehensive error handling
- Set up secure cloud deployment

---

## **Known Limitations**

- **Simplified Margin Calculations**: May not fully align with broker requirements
- **Limited Instrument Availability**: Restricted to instruments supported by the Upstox API
- **Weekly Expiry Dates**: May not consider all market holidays
- **No Historical Data Analysis**: Currently focused on real-time data

---

## **Future Improvements**

- **Multi-Broker API Support**: Extend support to other brokers' APIs
- **Historical Data Analysis**: Add functionality for historical data
- **Advanced Analytics and Visualization**: Introduce more in-depth analysis tools
- **Position Sizing and Strategy Recommendations**: Guide users on trade sizing
- **Backtesting Capabilities**: Implement a backtesting module
- **Enhanced Security Features**: Implement additional security measures
- **User Authentication**: Add user-specific settings and API keys

---

## **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

