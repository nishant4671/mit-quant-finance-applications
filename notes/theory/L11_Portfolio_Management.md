# Portfolio Management & Multi-Factor Models

---

## 🕒 Lesson 11.1: The Capital Asset Pricing Model (CAPM)

### 1. Intuition (ELIF5)
CAPM divides risk into systematic risk (which affects the entire market and cannot be avoided) and idiosyncratic risk (which affects only one company and can be diversified away). The model states that investors are only rewarded for taking systematic risk, which is measured by Beta ($\beta$).

### 2. Mathematical Formulations
The expected return of asset $i$ under CAPM is:
$$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$
where the systematic risk coefficient $\beta_i$ is defined as:
$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

```text
Algorithm: Fama-French Regression
Input: Stock returns R_i, Risk-free rate R_f, Market factor MKT, Size factor SMB, Value factor HML
Output: Factor loadings (beta_MKT, beta_SMB, beta_HML)

1. Compute excess return: Y = R_i - R_f
2. Form design matrix X = [1, MKT, SMB, HML]
3. Solve OLS regression: beta = (X^T * X)^(-1) * X^T * Y
return beta[1], beta[2], beta[3]
```
