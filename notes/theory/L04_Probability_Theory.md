# Probability Theory & Random Variables

---

## 🕒 Lesson 4.1: Random Variables & Probability Distributions

### 1. Intuition (ELIF5)
A random variable is a mathematical variable that takes on different values based on the outcome of a random event. For example, the return of a stock tomorrow is a random variable. A probability distribution describes how likely the variable is to take on different values.

### 2. Mathematical Formulations
For a continuous random variable $X$ with probability density function (PDF) $f(x)$, the expected value (mean $\mu$) is:
$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
The variance ($\sigma^2$) measures the dispersion of the random variable around its mean:
$$\text{Var}(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx$$

---

## 🕒 Lesson 4.2: Normal vs. Log-Normal Distributions

### 1. Intuition (ELIF5)
A normal distribution is symmetric and bell-shaped, allowing values to be negative. However, stock prices cannot drop below zero. To resolve this, we model stock returns (which can be positive or negative) as normally distributed, which implies that the stock prices themselves follow a log-normal distribution (always positive).

### 2. Mathematical Formulations
If the log-returns $x_t = \ln(S_t/S_0)$ follow a normal distribution $N(\mu, \sigma^2)$, then the stock price $S_t$ follows a log-normal distribution with PDF:
$$f(s) = \frac{1}{s \sigma \sqrt{2\pi}} e^{-\frac{(\ln s - \mu)^2}{2\sigma^2}} \quad (s > 0)$$

```text
Algorithm: Log-Normal Price Paths
Input: Initial Price S_0, Drift mu, Volatility sigma, Time horizon T, Time steps N, Number of paths M
Output: Simulated stock price matrix S of size M x (N+1)

dt = T / N
for path i = 1 to M:
    S[i, 0] = S_0
    for t = 1 to N:
        Z = sample standard normal N(0, 1)
        S[i, t] = S[i, t-1] * exp( (mu - 0.5 * sigma^2)*dt + sigma * sqrt(dt) * Z )
return S
```
