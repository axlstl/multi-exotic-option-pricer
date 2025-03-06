# multi-exotic-option-pricer
Quantitative pricing tool covering a wide range of financial options (Vanilla, Barrier, Digital, Asian, Basket) and comprehensive Greeks analysis using Python, Monte Carlo simulations, Black-Scholes formulas, and Streamlit.

ExoticOptionPricer

Quantitative pricing tool covering a wide range of financial options (Vanilla, Barrier, Digital, Asian, Basket) with comprehensive Greeks analysis.

📌 Overview

This project provides accurate pricing and detailed Greeks calculation for various types of options, including both simple (Vanilla, Digital) and exotic options (Barrier, Asian, Basket). The tool leverages powerful quantitative methods:

Black-Scholes (closed-form solutions)

Monte Carlo Simulations

Binomial/Trinomial Trees (optional)

The project also includes interactive visualization of Greeks (Delta, Gamma, Vega, Theta, Rho, Vanna, Volga) to provide deep insights into options sensitivities.

🔧 Key Features

Option Pricing:

Vanilla European (Call/Put)

Digital (Cash-or-Nothing)

Barrier (Knock-in/Knock-out)

Asian (Average Price/Average Strike)

Basket (Multiple underlyings)

Greeks Analysis:

Delta, Gamma, Vega, Theta, Rho

Advanced Greeks: Vanna, Volga

Interactive graphical visualizations

Quantitative Methods:

Closed-form (Black-Scholes)

Monte Carlo simulations

Binomial/Trinomial trees

📊 Interface

Built using Python

Streamlit application for user-friendly and interactive experience

🚀 Installation

Clone the repository:

git clone https://github.com/tonpseudo/ExoticOptionPricer.git
cd ExoticOptionPricer

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run streamlit_app.py

📁 Project Structure

ExoticOptionPricer/
├── pricing/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   └── binomial_tree.py
│
├── greeks/
│   ├── greeks.py
│   └── visualisation.py
│
├── utils/
│   └── market_data.py
│
├── data/             # Temporary and external data
├── tests/            # Unit tests
├── docs/             # Documentation
├── requirements.txt  # Python dependencies
└── streamlit_app.py  # Main Streamlit interface

📖 Potential Enhancements

Dynamic hedging backtesting with historical data

Real-time integration with Bloomberg or other market APIs

🎯 Why this Project?

Demonstrates strong quantitative and programming skills

Relevant for careers in quantitative finance, trading, and risk management

Ideal showcase for interviews and professional portfolios

Developed by [Your Name]📧 [Your Email] | 🌐 [Your LinkedIn]

