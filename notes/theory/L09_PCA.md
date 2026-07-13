# Principal Component Analysis (PCA) in Finance

---

## 🕒 Lesson 9.1: PCA as Dimensionality Reduction

> [!NOTE]
> **Summary in 1 Sentence:**
> PCA identifies orthogonal linear combinations of variables that capture the maximum variance in a high-dimensional dataset.

### 1. Intuition (ELIF5)
Imagine you want to describe a model airplane. You could list the 3D coordinates of 1,000 points on its surface. Or, you could describe its length, wingspan, and height. By focusing on the directions of greatest variation, you reduce the description from 1,000 coordinates to just 3 core dimensions. PCA is the mathematical tool that finds these key dimensions for complex data.

### 2. Formulas
We compute the eigenvalues $\Lambda$ and eigenvectors $V$ of the covariance matrix $\Sigma$:
$$\Sigma = V \Lambda V^T$$
The transformed principal components are:
$$Y = V^T X$$

---

## 🕒 Lesson 9.2: Yield Curve Factors (Level, Slope, Curvature)

> [!NOTE]
> **Summary in 1 Sentence:**
> Applying PCA to bond yields reveals three principal components that explain over 95% of yield curve movements: level shifts, slope twists, and belly curvature.

### 1. Intuition (ELIF5)
Instead of tracking 30 different interest rates (from 1-month to 30-year yields), PCA tells us that yield curves move in three main patterns:
1. **Level (PC1 ~90%):** The entire curve moves up or down in parallel.
2. **Slope (PC2 ~5-8%):** The curve tilts (short rates drop, long rates rise, or vice versa).
3. **Curvature (PC3 ~1-2%):** The middle of the curve bulges or flattens while the ends remain stable.
