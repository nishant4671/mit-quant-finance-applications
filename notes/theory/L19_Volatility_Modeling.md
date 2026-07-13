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

```text
Algorithm: Implied Volatility Solver
Input: Option market price C_market, Spot S, Strike K, Expiry T, rate r, Initial Guess sigma_0, Tolerance tol
Output: Implied Volatility sigma

sigma = sigma_0
repeat:
    d1 = (ln(S/K) + (r + 0.5 * sigma^2)*T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    C_est = S * N(d1) - K * exp(-r * T) * N(d2)
    vega = S * sqrt(T) * pdf(d1)
    sigma_new = sigma - (C_est - C_market) / vega
    if |sigma_new - sigma| < tol:
        return sigma_new
    sigma = sigma_new
```
