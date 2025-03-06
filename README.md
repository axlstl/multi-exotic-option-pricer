# multi-exotic-option-pricer

## **Overview**

This project serves as my first multi-file project and my first experience using GitHub for version control. I've been looking for a pricer like this for a long time, but I couldn't find a free tool that could both price exotic options and display Greeks in a clear way.  

The goal of this project is to develop a structured and efficient framework capable of:  

- **Pricing** a wide range of financial derivatives, from standard vanilla options (European calls/puts) to more complex exotic structures such as barrier, digital, basket, and Asian options.  
- **Computing and visualizing key risk sensitivities (Greeks)**, including first-order measures like Delta, Gamma, Vega, Theta, and Rho, as well as second-order sensitivities like Vanna and Volga.  
- **Implementing various quantitative pricing techniques**, from closed-form models (Black-Scholes) to Monte Carlo simulations and numerical approaches such as binomial trees.

The project is entirely written in **Python**, using **Streamlit** to create a simple and interactive interface. While primarily designed as a personal learning tool, it could also serve as a useful starting point for further exploration of option pricing and risk analysis.

## **Key Features**

- **Option Pricing**:

  - Vanilla European (Call/Put)
  - Digital (Cash-or-Nothing) (To be done)
  - Barrier (Knock-in/Knock-out) (To be done)
  - Asian (To be done)
  - Basket (To be done)



## **Project Structure**

```
multi-exotic-option-pricer/
├── pricing/
│   ├── closed_form.py
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
├── requirements.txt  # Python dependencies
└── streamlit_app.py  # Main Streamlit interface
```

## **Project Evolution**

06/03/2024 - Creation of the repository and folders structure

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/axlstl/multi-exotic-option-pricer.git
cd multi-exotic-option-pricer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```
