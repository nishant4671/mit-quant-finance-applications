# Stochastic Calculus & Stochastic Differential Equations (SDEs)

---

## 🕒 Lesson 24.1: Itô's Lemma

### 1. Intuition (ELIF5)
In standard calculus, the change in a function is the slope times the step size. But when the input wiggles randomly (like Brownian motion), the wiggles are so violent that their squared wiggles $(dW_t)^2$ accumulate over time. If the function is curved, this wiggling creates an extra drift term. Itô's Lemma is the mathematical formula that accounts for this extra drift.

### 2. Mathematical Formulations
For $dX_t = \mu_t dt + \sigma_t dW_t$, and a function $f(t, X_t)$:
$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial X} + \frac{1}{2} \sigma_t^2 \frac{\partial^2 f}{\partial X^2} \right) dt + \sigma_t \frac{\partial f}{\partial X} dW_t$$

```text
Algorithm: Euler-Maruyama GBM Simulation
Input: Initial Price S_0, Drift mu, Volatility sigma, Time horizon T, Steps N
Output: Simulated price path vector S of size N+1

dt = T / N
S[0] = S_0
for t = 1 to N:
    dW = sample normal N(0, dt)
    S[t] = S[t-1] + mu * S[t-1] * dt + sigma * S[t-1] * dW
return S
```

---

## 🕒 Lesson 24.2: Stochastic Differential Equations (SDEs)

### 1. Intuition (ELIF5)
An SDE describes a random path in terms of its average direction (drift) and its random wiggle (diffusion) at each point in time.

### 2. Mathematical Formulations
The Ornstein-Uhlenbeck (mean-reverting) SDE is:
$$dX_t = \theta(\mu - X_t) dt + \sigma dW_t$$
where $\theta$ is the speed of mean reversion, and $\mu$ is the long-term mean.
