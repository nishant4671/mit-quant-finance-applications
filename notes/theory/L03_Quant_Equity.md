# Quantitative Equity Investing & Portfolio Optimization

---

## 🕒 Lesson 3.1: Modern Portfolio Theory (MPT)

> [!NOTE]
> **Summary in 1 Sentence:**
> Modern Portfolio Theory defines the optimal combination of risky assets that maximizes expected return for a given level of risk (variance).

### 1. Intuition (ELIF5)
Imagine you are packing a lunchbox. You want it to be as tasty as possible (high return) but with the lowest risk of causing an allergic reaction (low risk). Some ingredients taste great but are risky; others are safe but bland. MPT is a recipe that mixes these ingredients to give you the most delicious lunch possible for whatever level of risk you are willing to tolerate.

### 2. Formulas
* **Portfolio Return:**
  $$E[R_p] = w^T E[R]$$
* **Portfolio Variance:**
  $$\sigma_p^2 = w^T \Sigma w$$
* **Sharpe Ratio:**
  $$	ext{Sharpe} = rac{E[R_p] - R_f}{\sigma_p}$$

---

## 🕒 Lesson 3.2: Mean-Variance Optimization & The Efficient Frontier

> [!NOTE]
> **Summary in 1 Sentence:**
> The Efficient Frontier is the set of optimal portfolios that offer the highest expected return for defined risk levels, solved using quadratic programming.

### 1. Intuition (ELIF5)
If you plot all possible asset combinations on a chart with "Risk" on the bottom and "Return" on the side, you get a curved region. The top edge of this curve is the **Efficient Frontier**. Any portfolio on this line is optimal: you cannot get more return without taking more risk, and you cannot lower risk without giving up return.

### 2. Formulas
To find the weights $w$ of the optimal portfolio for risk aversion parameter $\lambda > 0$:
$$\max_{w} \left( w^T E[R] - rac{\lambda}{2} w^T \Sigma w ight)$$
subject to:
$$w^T \mathbf{1} = 1 \quad 	ext{(Fully invested constraint)}$$
