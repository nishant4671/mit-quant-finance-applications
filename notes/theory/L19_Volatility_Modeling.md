# Volatility Modeling & The Term Structure of Volatility

---

## 🕒 Lesson 19.1: Realized vs. Implied Volatility

> [!NOTE]
> **Summary in 1 Sentence:**
> Realized volatility measures past price dispersion from historical data, whereas implied volatility reflects forward-looking market expectations backed out of option prices.

### 1. Intuition (ELIF5)
* **Realized Volatility:** Look at the weather records for the last 30 days and calculate how much the temperature fluctuated. This is historical fact.
* **Implied Volatility:** Look at the price of umbrellas being sold today. If umbrellas are expensive, people expect a storm soon. Implied volatility is what option prices tell us about the market's expectation of future volatility.

### 2. Formulas
* **Realized Volatility (Annualized):**
  $$\sigma_{	ext{historical}} = \sqrt{rac{252}{N-1} \sum_{i=1}^N (R_i - ar{R})^2}$$
* **Implied Volatility ($\sigma_{	ext{impl}}$):**
  Solved by finding the root:
  $$C_{	ext{market}} - 	ext{BlackScholesCall}(S, K, T, r, \sigma_{	ext{impl}}) = 0$$
