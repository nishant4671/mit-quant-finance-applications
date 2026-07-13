# Quantitative Equity Investing & Portfolio Optimization

---

## 🕒 Lesson 3.1: Modern Portfolio Theory (MPT)

### 1. Intuition (ELIF5)
Suppose you are putting together a portfolio. If you put all your money into one stock, you risk losing everything if that company fails. By spreading your money across different companies that operate in different sectors, you reduce your overall risk. MPT provides the mathematical framework for this diversification, showing that you can maximize expected returns for a given level of risk by combining assets that are not perfectly correlated.

### 2. Mathematical Formulations
Let $R_f$ be the risk-free rate, and $E[R]$ be the vector of expected asset returns. For a portfolio weight vector $w$, the expected return is:
$$E[R_p] = w^T E[R]$$
The portfolio volatility is $\sigma_p = \sqrt{w^T \Sigma w}$. The Sharpe Ratio, which measures the excess return per unit of risk, is:
$$\text{Sharpe} = \frac{E[R_p] - R_f}{\sigma_p}$$

---

## 🕒 Lesson 3.2: Mean-Variance Optimization & The Efficient Frontier

### 1. Intuition (ELIF5)
The Efficient Frontier is a curve representing the set of optimal portfolios that offer the highest expected return for each level of risk. An investor wants to construct a portfolio that lies on this frontier. Portfolios below the frontier are sub-optimal because you could achieve a higher return for the same risk, or lower risk for the same return.

### 2. Mathematical Formulations
To find the weights $w$ of the optimal portfolio on the efficient frontier, we solve the quadratic optimization problem:
$$\max_{w} \left( w^T E[R] - \frac{\lambda}{2} w^T \Sigma w \right)$$
subject to:
$$w^T \mathbf{1} = 1$$
where $\lambda$ is the investor's risk aversion parameter.
