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
└── README.md                 # Project documentation
