# The Black-Scholes Model & Option Pricing

---

## 🕒 Lesson 21.1: Replicating Portfolios

### 1. Intuition (ELIF5)
Black and Scholes showed that you can replicate the payoff of an option by dynamically trading a specific combination of the underlying stock and risk-free bonds. The cost of this replicating portfolio is the fair price of the option.

### 2. Mathematical Formulations
The replicating portfolio value is:
$$V_{\text{portfolio}} = \Delta_t S_t + \psi_t B_t$$
where the stock weight $\Delta_t = \frac{\partial V}{\partial S}$ is the option's delta.

```text
Algorithm: Delta Hedging Strategy
Input: Stock price paths S_t, Option type, Strike K, Expiry T, Rate r, Volatility sigma, Steps N
Output: Hedging error (portfolio tracking error)

dt = T / N
delta = BS_Delta(S_0, K, T, r, sigma)
portfolio_value = BS_Price(S_0, K, T, r, sigma)
cash = portfolio_value - delta * S_0

for t = 1 to N:
    stock_value = delta * S_t
    portfolio_value = stock_value + cash * exp(r * dt)
    delta_new = BS_Delta(S_t, K, T - t*dt, r, sigma)
    cash = portfolio_value - delta_new * S_t
    delta = delta_new
    
option_payoff = max(S_N - K, 0)
tracking_error = portfolio_value - option_payoff
return tracking_error
```

---

## 🕒 Lesson 21.2: The Black-Scholes Formula

### 1. Intuition (ELIF5)
The Black-Scholes formula provides the exact price of European options by modeling stock prices as Geometric Brownian Motion.

### 2. Mathematical Formulations
The European call price is:
$$C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$
where:
$$d_1 = \frac{\ln(S_t/K) + \left(r + \sigma^2/2\right)(T-t)}{\sigma\sqrt{T-t}} \quad \text{and} \quad d_2 = d_1 - \sigma\sqrt{T-t}$$
