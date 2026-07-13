# Regression Analysis & Regularization

---

## 🕒 Lesson 6.1: Ordinary Least Squares (OLS)

### 1. Intuition (ELIF5)
Regression analysis helps us find the relationship between variables. OLS is a method that fits a straight line through a scatter plot of data points. To find the "best" line, we measure the vertical distance from each point to the line, square these distances, and adjust the line's slope and intercept to minimize the total sum of these squared distances.

### 2. Mathematical Formulations
For the linear model $y = X\beta + \epsilon$, the OLS estimator minimizes the sum of squared residuals:
$$\min_{\beta} \|y - X\beta\|^2$$
The analytical solution is:
$$\hat{\beta} = (X^T X)^{-1} X^T y$$

---

## 🕒 Lesson 6.2: Regularization: Ridge & Lasso

### 1. Intuition (ELIF5)
If you have too many variables in a model, it can overfit, meaning it memorizes the noise in the data and performs poorly on new data. Regularization adds a penalty to the OLS optimization to keep the coefficients small:
* **Ridge** shrinks all coefficients slightly.
* **Lasso** shrinks coefficients and forces the least important ones to exactly zero, acting as a variable filter.

### 2. Mathematical Formulations
* **Ridge Regression ($L_2$ Regularization):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \sum_{j=1}^p \beta_j^2$$
* **Lasso Regression ($L_1$ Regularization):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \sum_{j=1}^p |\beta_j|$$

```text
Algorithm: Lasso Coordinate Descent
Input: Design Matrix X, Response Vector y, Penalty parameter lambda, Max Iterations max_iter, Tolerance tol
Output: Coefficient vector beta

Initialize beta = OLS estimator or 0
for k = 1 to max_iter:
    beta_old = beta
    for j = 1 to p:
        r_j = y - sum( X_i * beta_i for i != j )
        rho_j = X_j^T * r_j
        if rho_j < -lambda/2:
            beta[j] = (rho_j + lambda/2) / ||X_j||^2
        elif rho_j > lambda/2:
            beta[j] = (rho_j - lambda/2) / ||X_j||^2
        else:
            beta[j] = 0
    if ||beta - beta_old|| < tol:
        return beta
return beta
```
