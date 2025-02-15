import streamlit as st
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price, d1, d2

st.title("Black-Scholes Option Pricing Tool")

S = st.number_input("Stock Price (S0)", value=100.0)
K = st.number_input("Strike Price (K)", value=100.0)
T = st.number_input("Time to Maturity (T in years)", value=1.0)
r = st.number_input("Risk-free Rate (r)", value=0.05)
sigma = st.number_input("Volatility (σ)", value=0.2)
option_type = st.selectbox("Option Type", ["call", "put"])

if st.button("Calculate"):
    price, d1, d2 = black_scholes(S, K, T, r, sigma, option_type)
    st.success(f"The {option_type} option price is: {price:.2f}")

    # Display Greeks
    st.write("### Option Greeks")
    st.write(f"Delta: {norm.cdf(d1) if option_type == 'call' else norm.cdf(d1)-1:.4f}")
    st.write(f"Gamma: {norm.pdf(d1) / (S * sigma * np.sqrt(T)):.4f}")
    st.write(f"Vega: {S * norm.pdf(d1) * np.sqrt(T):.4f}")

    # Plot Price vs. Strike
    strikes = np.linspace(K * 0.5, K * 1.5, 50)
    prices = [black_scholes(S, k, T, r, sigma, option_type)[0] for k in strikes]
    plt.figure()
    plt.plot(strikes, prices)
    plt.title("Option Price vs Strike Price")
    plt.xlabel("Strike Price")
    plt.ylabel("Option Price")
    st.pyplot(plt)
