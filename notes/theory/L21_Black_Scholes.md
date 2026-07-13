# The Black-Scholes Model & Option Pricing

---

## 🕒 Lesson 21.1: Replicating Portfolios

### 1. Intuition (ELIF5)
Black and Scholes showed that you can replicate the payoff of an option by dynamically trading a specific combination of the underlying stock and risk-free bonds. The cost of this replicating portfolio is the fair price of the option.

### 2. Mathematical Formulations
The replicating portfolio value is:
$$V_{\text{portfolio}} = \Delta_t S_t + \psi_t B_t$$
where the stock weight $\Delta_t = \frac{\partial V}{\partial S}$ is the option's delta.

---

## 🕒 Lesson 21.2: The Black-Scholes Formula

### 1. Intuition (ELIF5)
The Black-Scholes formula provides the exact price of European options by modeling stock prices as Geometric Brownian Motion.

### 2. Mathematical Formulations
The European call price is:
$$C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$
where:
$$d_1 = \frac{\ln(S_t/K) + \left(r + \sigma^2/2\right)(T-t)}{\sigma\sqrt{T-t}} \quad \text{and} \quad d_2 = d_1 - \sigma\sqrt{T-t}$$
