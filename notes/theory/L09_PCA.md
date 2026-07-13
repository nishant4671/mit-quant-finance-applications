# Principal Component Analysis (PCA) in Finance

---

## 🕒 Lesson 9.1: PCA as Dimensionality Reduction

### 1. Intuition (ELIF5)
Imagine looking at a complex multidimensional object. By projecting its shadow onto a wall, you can capture most of its details. PCA is the mathematical equivalent of finding the best angle to cast this shadow, reducing the number of variables we need to analyze while retaining as much variance as possible.

### 2. Mathematical Formulations
We compute the eigenvalues $\Lambda$ and eigenvectors $V$ of the covariance matrix $\Sigma$:
$$\Sigma = V \Lambda V^T$$
The principal components are given by:
$$Y = V^T X$$

```text
Algorithm: Yield Curve Factor PCA
Input: Yield data matrix X of size T x N (T days, N maturities)
Output: Factors (Level, Slope, Curvature)

1. Center the data: X_centered = X - mean(X)
2. Compute Covariance Matrix: Sigma = (1/T) * X_centered^T * X_centered
3. Compute Eigenvectors V and Eigenvalues L of Sigma
4. Sort V by corresponding eigenvalues in descending order
5. Select top 3 factors: V_3 = V[:, 1:3]
6. Compute factor loadings: Y_3 = X_centered * V_3
return V_3, Y_3
```

---

## 🕒 Lesson 9.2: Yield Curve Factors

### 1. Intuition (ELIF5)
When we apply PCA to interest rates across different maturities, we find that three main shapes explain almost all movements in the yield curve:
1. **Level:** The entire curve shifts up or down in parallel.
2. **Slope:** The curve tilts (short rates rise, long rates fall).
3. **Curvature:** The middle of the curve bends.

### 2. Mathematical Formulations
The first three principal components typically account for over 95% of the total variance of yield curve changes, allowing us to model the entire curve with just three factors.
