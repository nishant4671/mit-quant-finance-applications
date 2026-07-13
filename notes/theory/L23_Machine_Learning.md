# Machine Learning in Finance

---

## 🕒 Lesson 23.1: Supervised Learning & Overfitting

### 1. Intuition (ELIF5)
Machine learning models find complex non-linear patterns in data. However, because financial markets are noisy, models can easily overfit by memorizing historical noise, which leads to poor performance on new data.

### 2. Mathematical Formulations
To prevent overfitting, we minimize loss while penalizing model complexity:
$$\min_{\theta} \sum_{i=1}^n L(y_i, f(x_i; \theta)) + \lambda \|\theta\|_2^2$$
where $\lambda$ is the regularization strength.

```text
Algorithm: Mini-batch SGD for Financial Models
Input: Training data X, Labels y, Model parameters theta, Learning rate alpha, Batch size B, Max Iterations epochs
Output: Optimized parameters theta

for epoch = 1 to epochs:
    X_shuffled, y_shuffled = shuffle(X, y)
    for batch = 1 to num_batches:
        X_b, y_b = get_batch(X_shuffled, y_shuffled, batch, B)
        gradient = compute_gradient(loss_function(X_b, y_b; theta))
        theta = theta - alpha * gradient
return theta
```
