# Machine Learning in Finance

---

## 🕒 Lesson 23.1: Supervised Learning & Overfitting

<h3>1. Intuition (ELIF5)</h3>
Machine learning models find complex non-linear patterns in data. However, because financial markets are noisy, models can easily overfit by memorizing historical noise, which leads to poor performance on new data.

### 2. Mathematical Formulations
To prevent overfitting, we minimize loss while penalizing model complexity:
$$\min_{\theta} \sum_{i=1}^n L(y_i, f(x_i; \theta)) + \lambda \|\theta\|_2^2$$
where $\lambda$ is the regularization strength.
