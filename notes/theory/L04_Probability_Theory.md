# Probability Theory & Random Variables

---

## 🕒 Lesson 4.1: Random Variables & Distributions

> [!NOTE]
> **Summary in 1 Sentence:**
> Random variables model uncertain numerical outcomes, and probability density functions (PDFs) map the relative likelihood of these outcomes.

### 1. Intuition (ELIF5)
Imagine rolling a die. Before you roll, you don't know the number, but you know it must be 1, 2, 3, 4, 5, or 6, and each has a 1-in-6 chance. A **random variable** is the mathematical placeholder for this rolling die. The **probability distribution** is the rulebook that tells you how likely each outcome is.

### 2. Formulas
* **Expected Value (Mean $\mu$):**
  $$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
* **Variance ($\sigma^2$):**
  $$	ext{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

---

## 🕒 Lesson 4.2: Normal vs. Log-Normal Distributions in Finance

> [!NOTE]
> **Summary in 1 Sentence:**
> Financial models assume asset returns are normally distributed (can be positive or negative) and asset prices are log-normally distributed (bounded below by zero).

### 1. Intuition (ELIF5)
A normal distribution (bell curve) goes off to infinity in both directions. However, a stock price cannot drop below zero (companies have limited liability; you can't owe money just for holding stock).
Therefore, we assume:
* **Asset Returns** follow a Normal distribution (you can lose -10% or gain +10%).
* **Asset Prices** follow a Log-Normal distribution (always positive, ranging from 0 to infinity).

### 2. Formulas
If $\ln(S_t) \sim N(\mu, \sigma^2)$, then $S_t$ is log-normally distributed with PDF:
$$f(s) = rac{1}{s \sigma \sqrt{2\pi}} e^{-rac{(\ln s - \mu)^2}{2\sigma^2}} \quad (s > 0)$$
