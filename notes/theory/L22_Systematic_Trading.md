# Systematic Trading Strategies

---

## 🕒 Lesson 22.1: Trend Following & Mean Reversion

### 1. Intuition (ELIF5)
Systematic trading rules execute trades automatically based on statistical signals:
* **Trend Following:** Buy assets that are rising, expecting them to keep rising.
* **Mean Reversion:** Buy assets that have fallen significantly below their historic average, expecting them to return to normal.

### 2. Mathematical Formulations
* **Moving Average Crossover Signal:**
  $$\text{Signal}_t = \text{sign}(\text{SMA}_{\text{fast}}(t) - \text{SMA}_{\text{slow}}(t))$$
* **Information Ratio (IR):**
  $$\text{IR} = \frac{\alpha}{\sigma_{\text{residual}}}$$
