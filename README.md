# **Options Chain Analysis Tool**

A Python-based tool for analyzing options data and calculating margins using the **Upstox API** on an interactive **Streamlit dashboard**.

---

## **Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
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

- **Real-time Options Chain Data**: Fetch real-time data for options chains using the Upstox API.
- **Support for Call (CE) and Put (PE) Options**: Analyze both call and put options.
- **Flexible Expiry Date Selection**: Choose from available expiry dates.
- **Automatic Margin Calculation**: Calculates margin requirements for options.
- **Premium Earned Calculation**: Calculates potential premiums.
- **Summary Statistics Display**: Provides key data points concisely.
- **Interactive User Interface**: Built on Streamlit for an intuitive, accessible experience.

---

## **Installation**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/saurabh-1907/option-chain-analysis.git
    cd option-chain-analysis
    ```

2. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Credentials**:

    Create a `.env` file in the project directory with your **Upstox API credentials**:

    ```plaintext
    UPSTOX_ACCESS_TOKEN=your_access_token_here
    ```

---

## **Usage**

1. **Start the Streamlit Application**:

    ```bash
    streamlit run streamlit_app.py
    ```

2. **Open the Application**:

    Navigate to **[http://localhost:8501](http://localhost:8501)** in your web browser.

3. **Select Analysis Parameters**:

    - **Instrument** (e.g., Nifty 50, Bank Nifty, Reliance)
    - **Expiry Date**
    - **Option Type** (CE for Call or PE for Put)

4. **Fetch Data**:

    Click on **"Fetch Data"** to retrieve and analyze options data, including **margins** and **premiums**.

---

## **Project Structure**

```plaintext
options-chain-analysis/
├── streamlit_app.py          # Main Streamlit application
├── option_chain.py           # Option chain data fetching module
├── margin_calculator.py      # Margin and premium calculations
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (not in repo)
└── README.md                 # Project documentation```


 ###**Explanation of Key Files**

- **`streamlit_app.py`**: Implements the **Streamlit interface** and handles **user input** and **data display**.
- **`option_chain.py`**: Communicates with **Upstox API**, processes API responses, and includes **error handling**.
- **`margin_calculator.py`**: Calculates **margin requirements** and **premium earnings** based on the selected options data.

---

### **Implementation Details**

1. **`streamlit_app.py`**
   - **Implements Streamlit Interface** for an interactive layout.
   - **Handles User Input** and **Displays Results** with an organized layout and formatted numerical displays.

2. **`option_chain.py`**
   - **Fetches and Structures Options Data** using the **Upstox API**.
   - **Error Handling** and **Data Validation** ensure reliable data.

3. **`margin_calculator.py`**
   - **Calculates Margins and Premiums** for each option contract.
   - **Configurable Framework** for flexible margin calculations based on market rates and contract size.

---

### **Development Process & AI Usage**

**AI tools** like **ChatGPT** were used to:

- Discuss project structure and generate initial function signatures.
- Assist with understanding the **Upstox API documentation**.
- Optimize data processing steps with **pandas**.
- Implement comprehensive **error handling** strategies.

---

### **Known Limitations**

- **Simplified Margin Calculations**: May not fully align with broker requirements.
- **Limited Instrument Availability**: Restricted to instruments supported by the Upstox API.
- **Weekly Expiry Dates**: May not consider all market holidays.
- **No Historical Data Analysis**: Currently focused on real-time data.

---

### **Future Improvements**

- **Multi-Broker API Support**: Extend support to other brokers' APIs.
- **Historical Data Analysis**: Add functionality for historical data.
- **Advanced Analytics and Visualization**: Introduce more in-depth analysis tools.
- **Position Sizing and Strategy Recommendations**: Guide users on trade sizing and option strategies.
- **Backtesting Capabilities**: Implement a backtesting module for strategy analysis.
