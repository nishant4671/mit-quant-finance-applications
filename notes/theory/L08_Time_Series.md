# Time Series Analysis & Volatility Forecasting

---

## 🕒 Lesson 8.1: Stationarity & ARMA Models

### 1. Intuition (ELIF5)
A time series is a sequence of data points recorded at regular time intervals. For our statistical models to work, the data must be stationary, meaning its mean and variance do not change over time. 
* **AR (Autoregressive):** Predicts the next value based on previous values.
* **MA (Moving Average):** Predicts the next value based on past random surprises.

### 2. Mathematical Formulations
* **AR(1) Model:**
  $$X_t = c + \phi X_{t-1} + \epsilon_t$$
* **MA(1) Model:**
  $$X_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$$

---

## 🕒 Lesson 8.2: GARCH Volatility Modeling

### 1. Intuition (ELIF5)
In financial markets, high-volatility days tend to cluster together (volatility clustering). GARCH is a model that forecasts tomorrow's volatility based on yesterday's volatility and yesterday's return shock.

### 2. Mathematical Formulations
For a GARCH(1,1) model, the conditional variance $\sigma_t^2$ is:
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
where $\epsilon_{t-1}^2$ is the residual from the mean equation, and $\sigma_{t-1}^2$ is the previous variance forecast.

```text
Algorithm: GARCH(1,1) Volatility Forecast
Input: Returns R_1 to R_T, parameters omega, alpha, beta, initial variance sigma_0^2
Output: Forecasted variance sigma_next^2

sigma^2[0] = sigma_0^2
for t = 1 to T:
    epsilon[t] = R[t] - mean(R)
    sigma^2[t] = omega + alpha * epsilon[t-1]^2 + beta * sigma^2[t-1]
sigma_next^2 = omega + alpha * epsilon[T]^2 + beta * sigma^2[T]
return sigma_next^2
```
