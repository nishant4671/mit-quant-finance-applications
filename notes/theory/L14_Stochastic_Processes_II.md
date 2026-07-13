# Stochastic Processes II: Continuous Time

---

## 🕒 Lesson 14.1: Wiener Process (Brownian Motion)

### 1. Intuition (ELIF5)
Imagine a dust particle suspended in water. It wiggles randomly as it is hit by water molecules. This random path is a Wiener process. It is continuous, but extremely jagged and has no smooth slope anywhere.

### 2. Mathematical Formulations
A standard Wiener process $\{W_t\}$ satisfies:
1. $W_0 = 0$
2. The increments $W_t - W_s$ are normally distributed: $W_t - W_s \sim N(0, t-s)$
3. The increments are independent over non-overlapping intervals.

---

## 🕒 Lesson 14.2: Geometric Brownian Motion (GBM)

### 1. Intuition (ELIF5)
Standard Brownian motion can take negative values, which makes it unsuitable for stock prices. GBM resolves this by modeling the *percentage* change in the stock price as standard Brownian motion, ensuring the price remains positive.

### 2. Mathematical Formulations
The SDE for Geometric Brownian Motion is:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
where $\mu$ is the drift and $\sigma$ is the volatility.
