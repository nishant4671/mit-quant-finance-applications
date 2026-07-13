# Machine Learning in Finance

---

## 🕒 Lesson 23.1: Supervised Learning & Overfitting in Finance

> [!NOTE]
> **Summary in 1 Sentence:**
> Machine learning identifies complex, non-linear relationships in financial data, but requires strict validation to prevent memorizing historical noise.

### 1. Intuition (ELIF5)
Financial data is incredibly noisy. If you give a highly flexible machine learning model free rein to predict tomorrow's stock price, it will memorize historical patterns that were pure coincidence (like "the stock always rises on rainy Tuesdays when the CEO wears blue"). This is **overfitting**. When you run the model on new data, it fails.

### 2. Formulas
We minimize training loss plus a complexity penalty (regularization):
$$\mathcal{L}(	heta) = \sum_{i=1}^n L(y_i, f(x_i; 	heta)) + \Omega(	heta)$$

---

## 🕒 Lesson 23.2: Ensemble Models & Decision Trees

> [!NOTE]
> **Summary in 1 Sentence:**
> Ensemble methods, such as Random Forests, aggregate predictions from multiple weak models (decision trees) to reduce variance and improve robustness.

### 1. Intuition (ELIF5)
A single decision tree makes predictions by asking yes/no questions (e.g., "Is interest rate > 5%?"). If you rely on one tree, it is easily tricked.
Instead, we use a **Random Forest**: we train 100 different trees on slightly different subsets of data. Each tree votes, and we take the average. It is much harder to trick a crowd of trees than a single tree.

### 2. Formulas
For a random forest of $B$ bootstrap-aggregated trees $T_b$:
$$\hat{f}_{	ext{rf}}(x) = rac{1}{B} \sum_{b=1}^B T_b(x)$$
