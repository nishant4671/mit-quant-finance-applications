# Time Series Analysis & Volatility Forecasting

---

## 🕒 Lesson 8.1: Stationarity & ARMA Models

> [!NOTE]
> **Summary in 1 Sentence:**
> Time series models analyze sequential data dependencies, requiring stationarity (constant mean and variance over time) to make stable forecasts.

### 1. Intuition (ELIF5)
Imagine you want to predict a child's height over time. If they are growing, the average height is constantly shifting upward (non-stationary). To model this, we look at the *change* in height from year to year, which is stable (stationary). 
* **Autoregressive (AR):** Uses past values to predict the future (e.g., if it rained yesterday, it might rain today).
* **Moving Average (MA):** Uses past random surprises (shocks) to adjust predictions.

### 2. Formulas
* **AR(1) Model:**
  $$X_t = c + \phi X_{t-1} + \epsilon_t$$
* **MA(1) Model:**
  $$X_t = \mu + \epsilon_t + 	heta \epsilon_{t-1}$$

---

## 🕒 Lesson 8.2: GARCH Volatility Modeling

> [!NOTE]
> **Summary in 1 Sentence:**
> GARCH models volatility clustering in financial returns, where high-volatility periods tend to feed into future high-volatility states.

### 1. Intuition (ELIF5)
Stock markets don't fluctuate at a constant speed. Instead, they have periods of relative calm and periods of extreme panic (volatility clustering). If the market was highly volatile yesterday, it is likely to remain volatile today. GARCH is the mathematical formula that models this "memory of volatility."

### 2. Formulas
For GARCH(1,1), the conditional variance $\sigma_t^2$ is modeled as:
$$\sigma_t^2 = \omega + lpha \epsilon_{t-1}^2 + eta \sigma_{t-1}^2$$
Where:
* $\omega$ = Baseline constant variance
* $lpha$ = Sensitivity to yesterday's return shock ($\epsilon_{t-1}^2$)
* $eta$ = Persistence of yesterday's volatility forecast ($\sigma_{t-1}^2$)
