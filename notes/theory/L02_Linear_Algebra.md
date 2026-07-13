# Applied Linear Algebra in Quantitative Finance

---

## 🕒 Lesson 2.1: Matrices as Transformations

> [!NOTE]
> **Summary in 1 Sentence:**
> Matrices act as geometric operators that rotate, scale, or project vector spaces, allowing us to translate coordinate systems to find the natural axes of data.

### 1. Intuition (ELIF5)
Imagine you are looking at a 3D statue. If you look at it from the front, it looks like a flat circle. If you look from the side, it looks like a rectangle. By rotating the statue (or moving your camera), you change your perspective.
In finance, a matrix is a tool that takes a set of stock returns and transforms them (rotates or scales them) into a new perspective. Instead of looking at 500 individual stocks, we can rotate our view to align with the overall movements of the market.

### 2. Formulas
A matrix $A$ transforms a vector $x$ into a new vector $y$:
$$y = A x$$

---

## 🕒 Lesson 2.2: Eigenvalues & Eigenvectors

> [!NOTE]
> **Summary in 1 Sentence:**
> Eigenvectors are the directions that remain unchanged in orientation when transformed by a matrix, and eigenvalues measure the scale of stretch along those directions.

### 1. Intuition (ELIF5)
Imagine blowing up a balloon. Most points on the balloon's surface move in different directions. However, there are usually a few lines of points (like the vertical axis from the knot to the top) that point in the exact same direction before and after inflation—they just got stretched.
* The **Eigenvector** is that line which did not change its direction.
* The **Eigenvalue** is the factor by which that line stretched (e.g., it doubled in length, so eigenvalue = 2).

In finance, if $A$ is the covariance matrix of asset returns, the eigenvector with the largest eigenvalue represents the direction of the market's maximum volatility (the "Market Factor").

### 2. Formulas
An eigenvector $v$ and its corresponding eigenvalue $\lambda$ for a square matrix $A$ satisfy:
$$A v = \lambda v$$
To solve for eigenvalues, we find the roots of the characteristic equation:
$$\det(A - \lambda I) = 0$$

---

## 🕒 Lesson 2.3: Covariance Matrices & Quadratic Forms

> [!NOTE]
> **Summary in 1 Sentence:**
> Covariance matrices capture the joint variability of assets, and quadratic forms allow us to compute aggregate portfolio variance from asset weights.

### 1. Intuition (ELIF5)
If you own two stocks, their combined risk isn't just the sum of their individual risks. You also need to know if they move together (covariance). 
* Positive covariance: they rise and fall together (like two tech stocks).
* Negative covariance: one rises when the other falls (like gold and tech).
A **Covariance Matrix** is a grid of numbers showing the relationship between every pair of stocks. A **quadratic form** is the mathematical operation of weighting these relationships to calculate your portfolio's total risk.

### 2. Formulas
For a portfolio with weight vector $w$ and asset covariance matrix $\Sigma$:
$$\sigma_p^2 = w^T \Sigma w = \sum_{i=1}^n \sum_{j=1}^n w_i w_j 	ext{Cov}(R_i, R_j)$$
