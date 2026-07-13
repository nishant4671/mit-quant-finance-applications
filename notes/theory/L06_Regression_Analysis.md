# Regression Analysis & Regularization

---

## 🕒 Lesson 6.1: Ordinary Least Squares (OLS)

> [!NOTE]
> **Summary in 1 Sentence:**
> Ordinary Least Squares fits a linear relationship by minimizing the sum of squared differences between observed values and predictions.

### 1. Intuition (ELIF5)
Imagine you want to predict a student's test score based on how many hours they studied. You plot the data points on a graph and use a ruler to draw a straight line through the middle of them. To make it the "best" line, you measure the vertical distance from each point to your line, square those distances (so positive and negative errors don't cancel out), and adjust the line until that total sum is as small as possible.

### 2. Formulas
We fit $y = Xeta + \epsilon$ by solving:
$$\min_{eta} \|y - Xeta\|^2$$
The closed-form OLS solution is:
$$\hat{eta} = (X^T X)^{-1} X^T y$$

---

## 🕒 Lesson 6.2: Regularization: Ridge & Lasso

> [!NOTE]
> **Summary in 1 Sentence:**
> Regularization prevents overfitting by adding a penalty term to the OLS loss function based on the magnitude of the model coefficients.

### 1. Intuition (ELIF5)
If you give a model too many variables (like predicting stock price using height of the CEO, weather in London, and interest rates), it will try to find patterns in the noise. Regularization is like a speed limit or a leash:
* **Ridge ($L_2$):** Shinks all coefficients toward zero, preventing any single variable from dominating.
* **Lasso ($L_1$):** Completely zeros out less important variables, acting as a built-in feature filter.

### 2. Formulas
* **Ridge (L2 Penalty):**
  $$\min_{eta} \|y - Xeta\|^2 + \lambda \|eta\|_2^2 = \min_{eta} \sum_{i=1}^n (y_i - x_i^T eta)^2 + \lambda \sum_{j=1}^p eta_j^2$$
* **Lasso (L1 Penalty):**
  $$\min_{eta} \|y - Xeta\|^2 + \lambda \|eta\|_1 = \min_{eta} \sum_{i=1}^n (y_i - x_i^T eta)^2 + \lambda \sum_{j=1}^p |eta_j|$$
