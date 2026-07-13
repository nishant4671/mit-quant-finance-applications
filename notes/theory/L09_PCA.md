# Principal Component Analysis (PCA) in Finance

---

## 🕒 Lesson 9.1: PCA as Dimensionality Reduction

<h3>1. Intuition (ELIF5)</h3>
Imagine looking at a complex multidimensional object. By projecting its shadow onto a flat wall, you can capture most of its details. PCA is the mathematical equivalent of finding the best angle to cast this shadow, reducing the number of variables we need to analyze while retaining as much variance as possible.

### 2. Mathematical Formulations
We compute the eigenvalues $\Lambda$ and eigenvectors $V$ of the covariance matrix $\Sigma$:
$$\Sigma = V \Lambda V^T$$
The principal components are given by:
$$Y = V^T X$$

---

## 🕒 Lesson 9.2: Yield Curve Factors

<h3>1. Intuition (ELIF5)</h3>
When we apply PCA to interest rates across different maturities, we find that three main shapes explain almost all movements in the yield curve:
1. **Level:** The entire curve shifts up or down in parallel.
2. **Slope:** The curve tilts (short rates rise, long rates fall).
3. **Curvature:** The middle of the curve bends.

### 2. Mathematical Formulations
The first three principal components typically account for over 95% of the total variance of yield curve changes, allowing us to model the entire curve with just three factors.
