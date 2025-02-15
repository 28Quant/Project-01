import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

st.title("Black-Scholes Option Pricing Tool")

S = st.number_input("Stock Price (S0)", value=100.0)
K = st.number_input("Strike Price (K)", value=100.0)
T = st.number_input("Time to Maturity (T in years)", value=1.0)
r = st.number_input("Risk-free Rate (r)", value=0.05)
sigma = st.number_input("Volatility (σ)", value=0.2)
option_type = st.selectbox("Option Type", ["call", "put"])

if st.button("Calculate"):
    price = black_scholes(S, K, T, r, sigma, option_type)
    st.success(f"The {option_type} option price is: {price:.2f}")
```
