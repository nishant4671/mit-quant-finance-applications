# Volatility Modeling & Volatility Term Structure

---

## 🕒 Lesson 19.1: Realized vs. Implied Volatility

### 1. Intuition (ELIF5)
* **Realized Volatility:** Measures how much stock prices actually fluctuated in the past (historical fact).
* **Implied Volatility:** backed out from option prices, reflecting the market's expectation of future volatility.

### 2. Mathematical Formulations
The annualized realized volatility over $N$ periods is:
$$\sigma_{\text{historical}} = \sqrt{\frac{252}{N-1} \sum_{i=1}^N (R_i - \bar{R})^2}$$
The implied volatility $\sigma_{\text{impl}}$ solves:
$$C_{\text{market}} - \text{BlackScholesCall}(S, K, T, r, \sigma_{\text{impl}}) = 0$$
