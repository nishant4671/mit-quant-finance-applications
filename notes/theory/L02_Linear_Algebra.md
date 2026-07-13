# Applied Linear Algebra in Quantitative Finance

---

## 🕒 Lesson 2.1: Matrices as Linear Transformations

### 1. Intuition (ELIF5)
Imagine you are looking at a 3D object on a screen. When you rotate the camera, the object's shape changes on the screen. The rotation of the camera is a transformation of the coordinates. In quantitative finance, we treat portfolios of assets similarly. A matrix is a mathematical tool that rotates and scales asset returns, transforming them from one coordinate system (individual stocks) into a new coordinate system (underlying risk factors).

### 2. Mathematical Formulations
A square matrix $A$ of size $n \times n$ maps an input vector $x \in \mathbb{R}^n$ to an output vector $y \in \mathbb{R}^n$:
$$y = A x$$
This operation represents a linear combination of the columns of $A$ scaled by the elements of $x$.

---

## 🕒 Lesson 2.2: Eigenvalues & Eigenvectors

### 1. Intuition (ELIF5)
Imagine blowing up a balloon. Most points on the balloon's surface move in different directions. However, there are specific axes (like the line pointing straight up from the tie) that stretch but point in the exact same direction as before. In linear algebra, these special axes are eigenvectors, and the factor by which they stretch is the eigenvalue. In finance, if the matrix represents the covariance of stock returns, the eigenvector with the largest eigenvalue points in the direction of the market's primary risk driver.

### 2. Mathematical Formulations
For a square matrix $A$, a non-zero vector $v$ is an eigenvector if:
$$A v = \lambda v$$
where $\lambda$ is the eigenvalue. We solve for $\lambda$ by finding the roots of the characteristic equation:
$$\det(A - \lambda I) = 0$$

```text
Algorithm: Power Iteration for Principal Eigenvector
Input: Symmetric Matrix A, Initial Guess Vector v_0, Max Iterations max_iter, Tolerance tol
Output: Eigenvector v, Eigenvalue lambda

v = v_0 / ||v_0||
for k = 1 to max_iter:
    w = A * v
    lambda = v^T * w
    v_new = w / ||w||
    if ||v_new - v|| < tol:
        return v_new, lambda
    v = v_new
return v, lambda
```

---

## 🕒 Lesson 2.3: Covariance Matrices & Quadratic Forms

### 1. Intuition (ELIF5)
The risk of a portfolio is not simply the sum of the risks of its individual assets. We must account for how the assets move together. This joint risk is stored in a grid called a Covariance Matrix. A positive covariance means the assets move together, while a negative covariance means they move in opposite directions. We use a quadratic form to calculate the total portfolio variance from the covariance matrix and the portfolio weights.

### 2. Mathematical Formulations
Let $\Sigma$ be the $n \times n$ covariance matrix of $n$ assets, where the entry $\Sigma_{ij} = \text{Cov}(R_i, R_j)$. The variance of a portfolio with weight vector $w \in \mathbb{R}^n$ is computed via the quadratic form:
$$\sigma_p^2 = w^T \Sigma w = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \Sigma_{ij}$$
Because $\Sigma$ is symmetric and positive semi-definite, the portfolio variance is guaranteed to be non-negative for all weight vectors:
$$w^T \Sigma w \ge 0$$
