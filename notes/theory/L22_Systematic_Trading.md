# Systematic Trading Strategies

---

## 🕒 Lesson 22.1: Trend Following & Mean Reversion

> [!NOTE]
> **Summary in 1 Sentence:**
> Systematic trading applies rule-based algorithms to capture market inefficiencies, categorized into trend-following (momentum) and mean-reversion strategies.

### 1. Intuition (ELIF5)
Systematic trading means taking the human emotion out of investing by writing a strict rulebook for a computer:
* **Trend Following:** "If a stock has been rising for a month, buy it because it has momentum." (Like hopping onto a moving train).
* **Mean Reversion:** "If a stock's price drops way lower than its historic average, buy it because it will likely snap back to normal." (Like stretching a rubber band).

### 2. Formulas
* **Simple Moving Average (SMA):**
  $$	ext{SMA}_n(t) = rac{1}{n} \sum_{i=0}^{n-1} S_{t-i}$$
* **Trading Signal (Crossover):**
  $$	ext{Signal}_t = 	ext{sign}(	ext{SMA}_{	ext{fast}}(t) - 	ext{SMA}_{	ext{slow}}(t))$$

---

## 🕒 Lesson 22.2: Strategy Evaluation Metrics

> [!NOTE]
> **Summary in 1 Sentence:**
> Quantitative strategies are evaluated on risk-adjusted metrics like the Sharpe ratio, Maximum Drawdown, and Information Ratio.

### 1. Intuition (ELIF5)
You shouldn't just look at how much money a trading bot made. If it made 50% but almost went bankrupt three times during the year, it is highly dangerous. We use metrics to judge if the returns were worth the stress:
* **Max Drawdown:** The biggest peak-to-trough drop in account value.
* **Sharpe Ratio:** Reward per unit of risk.

### 2. Formulas
* **Annualized Sharpe Ratio:**
  $$	ext{Sharpe} = rac{	ext{Mean Annualized Return} - R_f}{	ext{Standard Deviation of Annualized Returns}}$$
* **Maximum Drawdown (MDD):**
  $$	ext{MDD}_T = \max_{t \in [0, T]} \left( rac{\max_{s \in [0, t]} P_s - P_t}{\max_{s \in [0, t]} P_s} ight)$$
