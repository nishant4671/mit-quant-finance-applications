import os

def write_chapters():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    os.makedirs(theory_dir, exist_ok=True)

    chapters = {
        "L01_Bond_Math.md": r"""# Financial Terms, Concepts, and Bond Math

---

## 🕒 Lesson 1.1: Time Value of Money & Compounding

### 1. Intuition (ELIF5)
Imagine you have $100 today. You can deposit this money in a bank account, and the bank will pay you a fee for borrowing your cash over time. This fee is called interest. If you choose to receive $100 five years from now instead of today, you lose the opportunity to earn interest during those five years. Therefore, money today is worth more than the same amount of money in the future. The Present Value (PV) represents the current worth of a future cash flow, while the Future Value (FV) represents what that current sum will grow into over time.

### 2. Mathematical Formulations
If interest is compounded $m$ times per year at an annual nominal rate $r$, the Future Value after $t$ years is given by:
$$FV = PV \left(1 + \frac{r}{m}\right)^{m \cdot t}$$
Conversely, the Present Value is computed by discounting the Future Value back to the present:
$$PV = \frac{FV}{\left(1 + \frac{r}{m}\right)^{m \cdot t}}$$
In quantitative finance, we frequently assume interest is compounded continuously (i.e., $m \to \infty$). In this limit, the formulations simplify to:
$$FV = PV \cdot e^{r \cdot t}$$
$$PV = FV \cdot e^{-r \cdot t}$$

---

## 🕒 Lesson 1.2: Bond Pricing Mechanics

### 1. Intuition (ELIF5)
A bond is essentially a loan agreement between an investor and a borrower (such as a corporation or government). When you buy a bond, you lend money to the issuer. In return, the issuer promises to make periodic interest payments, known as coupons, and to return the original loan amount, called the face value or principal, when the bond matures. The fair price of a bond today is simply the sum of all its expected future cash flows, discounted back to the present using an appropriate discount rate.

### 2. Mathematical Formulations
For a zero-coupon bond (which pays no intermediate coupons and only returns the face value $F$ at maturity $T$), the price under continuous compounding is:
$$P_{\text{zcb}} = F \cdot e^{-y \cdot T}$$
For a coupon-bearing bond paying a periodic coupon $C$ $m$ times a year, the price $P$ is the sum of the discounted cash flows:
$$P = \sum_{k=1}^{n} \frac{C}{\left(1 + \frac{y}{m}\right)^k} + \frac{F}{\left(1 + \frac{y}{m}\right)^n}$$
where $y$ is the Yield to Maturity (YTM) and $n = m \cdot T$ is the total number of periods. The YTM is the single constant interest rate that equates the present value of the bond's cash flows to its current market price. Since this equation cannot be solved algebraically for $y$, numerical root-finding algorithms (such as the Newton-Raphson method) are required.

```text
Algorithm: Newton-Raphson YTM Solver
Input: Market Price P, Face Value F, Coupon C, Periods n, Annual Frequency m, Initial Guess y_0, Tolerance tol
Output: Yield to Maturity (YTM) y

y = y_0
repeat:
    P_est = sum( (C / m) / (1 + y/m)^t for t = 1 to n ) + F / (1 + y/m)^n
    dPes_dy = sum( -t * (C / m) / (1 + y/m)^(t+1) for t = 1 to n ) - n * F / (1 + y/m)^(n+1)
    y_new = y - (P_est - P) / dPes_dy
    if |y_new - y| < tol:
        return y_new
    y = y_new
```

---

## 🕒 Lesson 1.3: Yield Curves & Spot Rates

### 1. Intuition (ELIF5)
If you borrow money for one day, one year, or ten years, the interest rate you pay is usually different. Lenders generally demand higher interest rates for longer loans to compensate for the risk of locking up their capital. A Yield Curve is a graphical plot of the interest rates of bonds with similar credit quality across different maturities. 
A Spot Rate is the interest rate applicable to a single, isolated cash flow occurring at a specific future date. While the Yield to Maturity represents a weighted average of discount rates over a bond's life, spot rates are the true rates used to discount individual cash flows.

### 2. Mathematical Formulations
The Discount Factor $d(t)$ represents the present value of $1 received at time $t$. Under continuous compounding, it is defined as:
$$d(t) = e^{-r(t) \cdot t}$$
where $r(t)$ is the spot rate for maturity $t$. Given a set of liquid coupon bond prices, we can recursively determine the spot rates using a method called bootstrapping. For the first period, the spot rate is derived directly from the short-term zero-coupon rate. For subsequent periods, the price of the bond is expressed as the sum of discounted coupons using previously calculated spot rates, plus the final payment discounted at the new spot rate, which is then solved algebraically.

```text
Algorithm: Spot Rate Bootstrapping
Input: Prices of bonds P_i, maturities T_i, coupon payments C_i
Output: Spot rates r(T_i) for each maturity i

r = empty list of size N
for i = 1 to N:
    if T_i is first period:
        r[1] = ln( (F + C_1) / P_1 ) / T_1
    else:
        sum_prev_cf = sum( C_i * exp(-r[k] * T_k) for k = 1 to i-1 )
        r[i] = -ln( (P_i - sum_prev_cf) / (F + C_i) ) / T_i
return r
```

---

## 🕒 Lesson 1.4: Risk Sensitivity: Duration

### 1. Intuition (ELIF5)
Duration measures a bond's sensitivity to changes in interest rates. Imagine balancing a plank on your shoulder with weights distributed along it representing the cash flows. The Macaulay Duration represents the balance point or center of gravity of these cash flows. The Modified Duration measures the actual percentage change in the bond's price for a given change in interest rates. A higher duration means the bond's price will fluctuate more violently when interest rates move.

### 2. Mathematical Formulations
The Macaulay Duration ($D_{\text{mac}}$) is the weighted average time to receive all cash flows, where the weights are the present values of the cash flows:
$$D_{\text{mac}} = \frac{\sum_{t} t \cdot CF_t \cdot e^{-y \cdot t}}{P}$$
The Modified Duration ($D_{\text{mod}}$) measures the price sensitivity and is related to the derivative of price with respect to yield:
$$D_{\text{mod}} = -\frac{1}{P} \frac{dP}{dy}$$
Under discrete compounding, the relationship is:
$$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + \frac{y}{m}}$$
For small changes in yield $\Delta y$, the percentage price change is approximated linearly by:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y$$

---

## 🕒 Lesson 1.5: Risk Sensitivity: Convexity

### 1. Intuition (ELIF5)
Because the relationship between a bond's price and interest rates is curved (convex) rather than linear, a straight-line duration estimate becomes inaccurate for larger interest rate shocks. Convexity measures the curvature of this relationship. It describes how the duration of a bond changes as interest rates fluctuate. For plain bonds, convexity is positive, meaning that when interest rates fall, the price rises faster than duration predicts, and when rates rise, the price falls slower. This is the "convexity bonus" enjoyed by bondholders.

### 2. Mathematical Formulations
Convexity ($C$) is proportional to the second derivative of the bond price with respect to the yield:
$$C = \frac{1}{P} \frac{d^2 P}{dy^2}$$
Under discrete compounding, the formula is:
$$C = \frac{1}{P \cdot (1 + y/m)^2} \sum_{k=1}^{n} \frac{k(k+1) \cdot CF_k}{m^2 \cdot (1 + y/m)^k}$$
To obtain a highly accurate estimate of the percentage price change for a large yield shock $\Delta y$, we use the second-order Taylor series approximation:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2$$
""",

        "L02_Linear_Algebra.md": r"""# Applied Linear Algebra in Quantitative Finance

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
""",

        "L03_Quant_Equity.md": r"""# Quantitative Equity Investing & Portfolio Optimization

---

## 🕒 Lesson 3.1: Modern Portfolio Theory (MPT)

### 1. Intuition (ELIF5)
Suppose you are putting together a portfolio. If you put all your money into one stock, you risk losing everything if that company fails. By spreading your money across different companies that operate in different sectors, you reduce your overall risk. MPT provides the mathematical framework for this diversification, showing that you can maximize expected returns for a given level of risk by combining assets that are not perfectly correlated.

### 2. Mathematical Formulations
Let $R_f$ be the risk-free rate, and $E[R]$ be the vector of expected asset returns. For a portfolio weight vector $w$, the expected return is:
$$E[R_p] = w^T E[R]$$
The portfolio volatility is $\sigma_p = \sqrt{w^T \Sigma w}$. The Sharpe Ratio, which measures the excess return per unit of risk, is:
$$\text{Sharpe} = \frac{E[R_p] - R_f}{\sigma_p}$$

---

## 🕒 Lesson 3.2: Mean-Variance Optimization & The Efficient Frontier

### 1. Intuition (ELIF5)
The Efficient Frontier is a curve representing the set of optimal portfolios that offer the highest expected return for each level of risk. An investor wants to construct a portfolio that lies on this frontier. Portfolios below the frontier are sub-optimal because you could achieve a higher return for the same risk, or lower risk for the same return.

### 2. Mathematical Formulations
To find the weights $w$ of the optimal portfolio on the efficient frontier, we solve the quadratic optimization problem:
$$\max_{w} \left( w^T E[R] - \frac{\lambda}{2} w^T \Sigma w \right)$$
subject to:
$$w^T \mathbf{1} = 1$$
where $\lambda$ is the investor's risk aversion parameter.

```text
Algorithm: Mean-Variance Portfolio Frontier
Input: Expected Returns E_R, Covariance Matrix Sigma, Target Return R_target
Output: Optimal Weights w

Formulate quadratic programming problem:
    minimize w^T * Sigma * w
    subject to:
        w^T * E_R = R_target
        w^T * 1 = 1
Solve using Lagrange multipliers:
    Solve linear system:
    [ 2*Sigma  -E_R   -1  ] [ w ]   [ 0 ]
    [  E_R^T     0     0  ] [L_1] = [R_target]
    [   1^T      0     0  ] [L_2]   [ 1 ]
return w
```
""",

        "L04_Probability_Theory.md": r"""# Probability Theory & Random Variables

---

## 🕒 Lesson 4.1: Random Variables & Probability Distributions

### 1. Intuition (ELIF5)
A random variable is a mathematical variable that takes on different values based on the outcome of a random event. For example, the return of a stock tomorrow is a random variable. A probability distribution describes how likely the variable is to take on different values.

### 2. Mathematical Formulations
For a continuous random variable $X$ with probability density function (PDF) $f(x)$, the expected value (mean $\mu$) is:
$$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
The variance ($\sigma^2$) measures the dispersion of the random variable around its mean:
$$\text{Var}(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) dx$$

---

## 🕒 Lesson 4.2: Normal vs. Log-Normal Distributions

### 1. Intuition (ELIF5)
A normal distribution is symmetric and bell-shaped, allowing values to be negative. However, stock prices cannot drop below zero. To resolve this, we model stock returns (which can be positive or negative) as normally distributed, which implies that the stock prices themselves follow a log-normal distribution (always positive).

### 2. Mathematical Formulations
If the log-returns $x_t = \ln(S_t/S_0)$ follow a normal distribution $N(\mu, \sigma^2)$, then the stock price $S_t$ follows a log-normal distribution with PDF:
$$f(s) = \frac{1}{s \sigma \sqrt{2\pi}} e^{-\frac{(\ln s - \mu)^2}{2\sigma^2}} \quad (s > 0)$$

```text
Algorithm: Log-Normal Price Paths
Input: Initial Price S_0, Drift mu, Volatility sigma, Time horizon T, Time steps N, Number of paths M
Output: Simulated stock price matrix S of size M x (N+1)

dt = T / N
for path i = 1 to M:
    S[i, 0] = S_0
    for t = 1 to N:
        Z = sample standard normal N(0, 1)
        S[i, t] = S[i, t-1] * exp( (mu - 0.5 * sigma^2)*dt + sigma * sqrt(dt) * Z )
return S
```
""",

        "L05_Stochastic_Processes_I.md": r"""# Stochastic Processes I & Asset Return Modeling

---

## 🕒 Lesson 5.1: Random Walks & The Markov Property

### 1. Intuition (ELIF5)
A stochastic process is a sequence of random variables indexed by time, representing how a random system evolves. A random walk is a simple process where each step is random. The Markov Property states that the future path of the process depends only on its current state today, not on the path it took to get there. It is a "memoryless" process.

### 2. Mathematical Formulations
A discrete-time stochastic process $\{X_t\}$ satisfies the Markov property if:
$$P(X_{t+1} = x_{t+1} \mid X_t = x_t, X_{t-1} = x_{t-1}, \dots, X_0 = x_0) = P(X_{t+1} = x_{t+1} \mid X_t = x_t)$$

```text
Algorithm: Simulating a Random Walk
Input: Initial Value X_0, Steps N, Up probability p, Up step size u, Down step size d
Output: Path vector X of size N+1

X[0] = X_0
for t = 1 to N:
    U = sample uniform U(0, 1)
    if U < p:
        X[t] = X[t-1] + u
    else:
        X[t] = X[t-1] - d
return X
```

---

## 🕒 Lesson 5.2: Martingales (Fair Games)

### 1. Intuition (ELIF5)
A martingale is a mathematical model of a fair game. If you are betting on a series of fair coin flips, your expected wealth after the next flip, given everything you know about the past flips, is exactly equal to your wealth right now. On average, you neither win nor lose money.

### 2. Mathematical Formulations
A stochastic process $\{X_t\}$ is a martingale with respect to the filtration (historical information) $\mathcal{F}_t$ if:
$$E[|X_t|] < \infty$$
$$E[X_{t+1} \mid \mathcal{F}_t] = X_t$$
""",

        "L06_Regression_Analysis.md": r"""# Regression Analysis & Regularization

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
""",

        "L07_Linear_Rates.md": r"""# Linear Rates, Swaps, and Short-Rate Models

---

## 🕒 Lesson 7.1: Benchmark Rates & Forward Rates

### 1. Intuition (ELIF5)
Interest rates are the cost of borrowing money. A Forward Rate is an interest rate that you agree on today for a loan that will start at a specific date in the future.

### 2. Mathematical Formulations
The continuously compounded forward rate $f(0, T_1, T_2)$ locked in at time 0 for a period between $T_1$ and $T_2$ is:
$$f(0, T_1, T_2) = \frac{r(0, T_2) T_2 - r(0, T_1) T_1}{T_2 - T_1}$$

---

## 🕒 Lesson 7.2: Interest Rate Swaps (IRS)

### 1. Intuition (ELIF5)
Imagine you have a loan with a floating interest rate that changes every month. You want stability, so you agree to swap payments with a bank: you pay them a fixed rate, and they pay your floating rate. This contract is an Interest Rate Swap.

### 2. Mathematical Formulations
The swap rate $S_n$ that sets the initial market value of the swap to zero is:
$$S_n = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \alpha_i P(0, T_i)}$$
where $P(0, T_i)$ is the discount factor and $\alpha_i$ is the day-count fraction.

```text
Algorithm: Swap Rate Valuation
Input: Spot Curve r(t), Payment dates T_1 to T_n, Day-count fractions alpha_1 to alpha_n
Output: Swap Rate S_n

sum_pv = 0
for i = 1 to n:
    P_i = exp( -r(T_i) * T_i )
    sum_pv = sum_pv + alpha_i * P_i
P_n = exp( -r(T_n) * T_n )
S_n = (1 - P_n) / sum_pv
return S_n
```
""",

        "L08_Time_Series.md": r"""# Time Series Analysis & Volatility Forecasting

---

## 🕒 Lesson 8.1: Stationarity & ARMA Models

### 1. Intuition (ELIF5)
A time series is a sequence of data points recorded at regular time intervals. For our statistical models to work, the data must be stationary, meaning its mean and variance do not change over time. 
* **AR (Autoregressive):** Predicts the next value based on previous values.
* **MA (Moving Average):** Predicts the next value based on past random surprises.

### 2. Mathematical Formulations
* **AR(1) Model:**
  $$X_t = c + \phi X_{t-1} + \epsilon_t$$
* **MA(1) Model:**
  $$X_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$$

---

## 🕒 Lesson 8.2: GARCH Volatility Modeling

### 1. Intuition (ELIF5)
In financial markets, high-volatility days tend to cluster together (volatility clustering). GARCH is a model that forecasts tomorrow's volatility based on yesterday's volatility and yesterday's return shock.

### 2. Mathematical Formulations
For a GARCH(1,1) model, the conditional variance $\sigma_t^2$ is:
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
where $\epsilon_{t-1}^2$ is the residual from the mean equation, and $\sigma_{t-1}^2$ is the previous variance forecast.

```text
Algorithm: GARCH(1,1) Volatility Forecast
Input: Returns R_1 to R_T, parameters omega, alpha, beta, initial variance sigma_0^2
Output: Forecasted variance sigma_next^2

sigma^2[0] = sigma_0^2
for t = 1 to T:
    epsilon[t] = R[t] - mean(R)
    sigma^2[t] = omega + alpha * epsilon[t-1]^2 + beta * sigma^2[t-1]
sigma_next^2 = omega + alpha * epsilon[T]^2 + beta * sigma^2[T]
return sigma_next^2
```
""",

        "L09_PCA.md": r"""# Principal Component Analysis (PCA) in Finance

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
""",

        "L10_Counterparty_Risk.md": r"""# Counterparty Credit Risk & Event Trading

---

## 🕒 Lesson 10.1: Counterparty Exposure

### 1. Intuition (ELIF5)
Counterparty risk is the risk that the party on the other side of a financial contract defaults before settling their obligations. The exposure is the amount of money you would lose if they defaulted today.

### 2. Mathematical Formulations
The exposure $E(t)$ of a derivative contract at time $t$ is:
$$E(t) = \max(V(t), 0)$$
where $V(t)$ is the market value of the contract.

```text
Algorithm: Expected Exposure Monte Carlo
Input: Pricing function V(t, S), Simulated stock paths S_t,i, Time steps N, Paths M
Output: Expected Exposure curve EE of size N+1

for t = 0 to N:
    sum_exposure = 0
    for path i = 1 to M:
        V_val = V(t, S_t,i)
        exposure = max(V_val, 0)
        sum_exposure = sum_exposure + exposure
    EE[t] = sum_exposure / M
return EE
```

---

## 🕒 Lesson 10.2: Credit Valuation Adjustment (CVA)

### 1. Intuition (ELIF5)
When trading with a counterparty that has default risk, you should discount the price of the contract to reflect this risk. CVA is the market value of this credit risk.

### 2. Mathematical Formulations
The CVA is computed as:
$$\text{CVA} = (1 - R) \int_0^T D(0, t) \cdot \text{EE}(t) \cdot d\text{PD}(t)$$
where $R$ is the recovery rate, $D(0,t)$ is the discount factor, $\text{EE}(t)$ is the expected exposure, and $\text{PD}(t)$ is the probability of default.
""",

        "L11_Portfolio_Management.md": r"""# Portfolio Management & Multi-Factor Models

---

## 🕒 Lesson 11.1: The Capital Asset Pricing Model (CAPM)

### 1. Intuition (ELIF5)
CAPM divides risk into systematic risk (which affects the entire market and cannot be avoided) and idiosyncratic risk (which affects only one company and can be diversified away). The model states that investors are only rewarded for taking systematic risk, which is measured by Beta ($\beta$).

### 2. Mathematical Formulations
The expected return of asset $i$ under CAPM is:
$$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$
where the systematic risk coefficient $\beta_i$ is defined as:
$$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

```text
Algorithm: Fama-French Regression
Input: Stock returns R_i, Risk-free rate R_f, Market factor MKT, Size factor SMB, Value factor HML
Output: Factor loadings (beta_MKT, beta_SMB, beta_HML)

1. Compute excess return: Y = R_i - R_f
2. Form design matrix X = [1, MKT, SMB, HML]
3. Solve OLS regression: beta = (X^T * X)^(-1) * X^T * Y
return beta[1], beta[2], beta[3]
```
""",

        "L14_Stochastic_Processes_II.md": r"""# Stochastic Processes II: Continuous Time

---

## 🕒 Lesson 14.1: Wiener Process (Brownian Motion)

### 1. Intuition (ELIF5)
Imagine a dust particle suspended in water. It wiggles randomly as it is hit by water molecules. This random path is a Wiener process. It is continuous, but extremely jagged and has no smooth slope anywhere.

### 2. Mathematical Formulations
A standard Wiener process $\{W_t\}$ satisfies:
1. $W_0 = 0$
2. The increments $W_t - W_s$ are normally distributed: $W_t - W_s \sim N(0, t-s)$
3. The increments are independent over non-overlapping intervals.

---

## 🕒 Lesson 14.2: Geometric Brownian Motion (GBM)

### 1. Intuition (ELIF5)
Standard Brownian motion can take negative values, which makes it unsuitable for stock prices. GBM resolves this by modeling the *percentage* change in the stock price as standard Brownian motion, ensuring the price remains positive.

### 2. Mathematical Formulations
The SDE for Geometric Brownian Motion is:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
where $\mu$ is the drift and $\sigma$ is the volatility.

```text
Algorithm: Euler-Maruyama OU Process
Input: Initial Value X_0, Speed theta, Mean mu, Volatility sigma, Time horizon T, Steps N
Output: Simulated path vector X of size N+1

dt = T / N
X[0] = X_0
for t = 1 to N:
    dW = sample normal N(0, dt)
    X[t] = X[t-1] + theta * (mu - X[t-1]) * dt + sigma * dW
return X
```
""",

        "L18_Biomedical_Portfolios.md": r"""# Applying Data Science and AI to Managing Biomedical Portfolios

---

## 🕒 Lesson 18.1: Drug Development Risk & Securitization

### 1. Intuition (ELIF5)
Developing a new medicine is extremely risky and expensive. Imagine going on a quest to find a rare flower in a vast forest where only 1 in 20 paths leads to the flower. If a single researcher takes one path, they will likely fail (95% chance). If we fund 100 researchers to explore 100 different paths at the same time, the chance that at least one of them finds the flower becomes nearly 100%. 
A **Biomedical Megafund** works on this exact principle. By pooling together dozens of independent drug development projects under one giant fund, we lower the overall risk. This allows us to issue bonds (debt) to fund scientific research, attracting large-scale conservative investors (like pension funds) who would never normally invest in early-stage biotechnology.

### 2. Mathematical Formulations
Let $p$ be the independent probability of success for a single clinical drug trial, and let $N$ be the number of independent trials in the portfolio. The probability that at least one drug is successfully approved is given by:
$$P(\text{at least one success}) = 1 - (1 - p)^N$$
To fund the megafund, we apply financial securitization. The cash flows from successful drug approvals are distributed to investors through tranches:
1. **Senior Debt:** Has the first claim on cash flows, offering low yield and very high safety.
2. **Mezzanine Debt:** Has the next claim, offering moderate yield and risk.
3. **Equity:** Receives the remaining cash flows, offering high potential returns but absorbing the first losses.

```text
Algorithm: Megafund Cash Flow Allocation
Input: Drug trial successes K, Drug value V_drug, Senior Debt D_senior, Mezzanine Debt D_mezz
Output: Payout to Senior, Mezzanine, and Equity tranches

Total_Cash = K * V_drug
Payout_Senior = min(Total_Cash, D_senior)
Remaining_Cash = Total_Cash - Payout_Senior
Payout_Mezz = min(Remaining_Cash, D_mezz)
Payout_Equity = Remaining_Cash - Payout_Mezz
return Payout_Senior, Payout_Mezz, Payout_Equity
```

---

## 🕒 Lesson 18.2: AI in Clinical Trial Forecasting

### 1. Intuition (ELIF5)
How do we know which drug projects are worth funding? We can use historical data from thousands of past clinical trials. AI models analyze patient sizes, chemical compound types, and the target diseases to predict whether a new drug will pass its trials, helping us select the best projects for our megafund.

### 2. Mathematical Formulations
We model the probability of trial success $p_k$ for drug $k$ using machine learning classification models (such as random forests or neural networks) trained on trial features $x_k$:
$$p_k = f(x_k; \theta) \in [0, 1]$$
We then optimize the portfolio weights $w_k$ to maximize expected portfolio value subject to value-at-risk limits.
""",

        "L19_Volatility_Modeling.md": r"""# Volatility Modeling & Volatility Term Structure

---

## 🕒 Lesson 19.1: Realized vs. Implied Volatility

### 1. Intuition (ELIF5)
* **Realized Volatility:** Measures how much stock prices actually fluctuated in the past (historical fact).
* **Implied Volatility:** backed out from option prices, reflecting the market's expectation of future volatility.

### 2. Mathematical Formulations
The annualized realized volatility over $N$ periods is:
$$\sigma_{\text{historical}} = \sqrt{\frac{252}{N-1} \sum_{i=1}^N (R_i - \bar{R})^2}$$
The implied volatility $\sigma_{\text{impl}}$ solves:
$$C_{\text{market}} - \text{BlackScholesCall}(S, K, T, r, \sigma_{\text{impl}}) = 0$$

```text
Algorithm: Implied Volatility Solver
Input: Option market price C_market, Spot S, Strike K, Expiry T, rate r, Initial Guess sigma_0, Tolerance tol
Output: Implied Volatility sigma

sigma = sigma_0
repeat:
    d1 = (ln(S/K) + (r + 0.5 * sigma^2)*T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    C_est = S * N(d1) - K * exp(-r * T) * N(d2)
    vega = S * sqrt(T) * pdf(d1)
    sigma_new = sigma - (C_est - C_market) / vega
    if |sigma_new - sigma| < tol:
        return sigma_new
    sigma = sigma_new
```
""",

        "L20_Event_Trading.md": r"""# Building a Regulated Exchange for Trading on Events

---

## 🕒 Lesson 20.1: Event Contracts & Prediction Markets

### 1. Intuition (ELIF5)
Imagine betting on whether a specific bill will pass in Congress next week. You can buy a ticket that pays out exactly $1 if the bill passes, and $0 if it does not. If the current price of this ticket in the market is $0.65, it implies that the collective wisdom of the market believes there is a 65% chance the bill passes. These are **Event Contracts** (also called binary options). Event exchanges (like Kalshi) let people trade these contracts to hedge against real-world risks (for example, a business hedging against interest rate hikes or new regulations).

### 2. Mathematical Formulations
The payoff of a binary contract $I_E$ on event $E$ at expiration $T$ is:
$$I_E(T) = \begin{cases} 1 & \text{if } E \text{ occurs} \\ 0 & \text{if } E \text{ does not occur} \end{cases}$$
The risk-neutral price $P_E(t)$ of the contract at time $t < T$ is:
$$P_E(t) = e^{-r(T-t)} E^{\mathbb{Q}}[I_E(T)] = e^{-r(T-t)} \mathbb{Q}(E)$$
where $\mathbb{Q}(E)$ is the market-implied probability of the event occurring, and $r$ is the risk-free rate.

---

## 🕒 Lesson 20.2: Exchange Mechanics & Market Making

### 1. Intuition (ELIF5)
For an exchange to work, there must be buyers and sellers. If you want to buy a ticket for a congress bill passing, but no one is selling, you can't trade. A market maker solves this by constantly posting both buy and sell prices. They make money on the tiny difference between the buy and sell prices (the spread).

### 2. Mathematical Formulations
The exchange matches buy orders (bids) and sell orders (asks) using a central limit order book. The market maker's spread is:
$$\text{Spread} = P_{\text{ask}} - P_{\text{bid}}$$
The exchange ensures risk constraints are met by requiring traders to fully collateralize their positions (since the maximum loss of a binary contract is capped).

```text
Algorithm: Order Matching Engine
Input: New buy limit order (Price P_buy, Quantity Q_buy), Order Book Ask side
Output: Executed trades and updated Order Book Ask side

while Q_buy > 0 and Ask side is not empty:
    Best_Ask = Ask side.cheapest()
    if P_buy >= Best_Ask.price:
        Execution_Price = Best_Ask.price
        Execution_Qty = min(Q_buy, Best_Ask.qty)
        execute_trade(Price=Execution_Price, Qty=Execution_Qty)
        Q_buy = Q_buy - Execution_Qty
        Best_Ask.qty = Best_Ask.qty - Execution_Qty
        if Best_Ask.qty == 0:
            Ask side.remove(Best_Ask)
    else:
        break
if Q_buy > 0:
    Bid side.add(Price=P_buy, Qty=Q_buy)
```
""",

        "L21_Black_Scholes.md": r"""# The Black-Scholes Model & Option Pricing

---

## 🕒 Lesson 21.1: Replicating Portfolios

### 1. Intuition (ELIF5)
Black and Scholes showed that you can replicate the payoff of an option by dynamically trading a specific combination of the underlying stock and risk-free bonds. The cost of this replicating portfolio is the fair price of the option.

### 2. Mathematical Formulations
The replicating portfolio value is:
$$V_{\text{portfolio}} = \Delta_t S_t + \psi_t B_t$$
where the stock weight $\Delta_t = \frac{\partial V}{\partial S}$ is the option's delta.

```text
Algorithm: Delta Hedging Strategy
Input: Stock price paths S_t, Option type, Strike K, Expiry T, Rate r, Volatility sigma, Steps N
Output: Hedging error (portfolio tracking error)

dt = T / N
delta = BS_Delta(S_0, K, T, r, sigma)
portfolio_value = BS_Price(S_0, K, T, r, sigma)
cash = portfolio_value - delta * S_0

for t = 1 to N:
    stock_value = delta * S_t
    portfolio_value = stock_value + cash * exp(r * dt)
    delta_new = BS_Delta(S_t, K, T - t*dt, r, sigma)
    cash = portfolio_value - delta_new * S_t
    delta = delta_new
    
option_payoff = max(S_N - K, 0)
tracking_error = portfolio_value - option_payoff
return tracking_error
```

---

## 🕒 Lesson 21.2: The Black-Scholes Formula

### 1. Intuition (ELIF5)
The Black-Scholes formula provides the exact price of European options by modeling stock prices as Geometric Brownian Motion.

### 2. Mathematical Formulations
The European call price is:
$$C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$
where:
$$d_1 = \frac{\ln(S_t/K) + \left(r + \sigma^2/2\right)(T-t)}{\sigma\sqrt{T-t}} \quad \text{and} \quad d_2 = d_1 - \sigma\sqrt{T-t}$$
""",

        "L22_Systematic_Trading.md": r"""# Systematic Trading Strategies

---

## 🕒 Lesson 22.1: Trend Following & Mean Reversion

### 1. Intuition (ELIF5)
Systematic trading rules execute trades automatically based on statistical signals:
* **Trend Following:** Buy assets that are rising, expecting them to keep rising.
* **Mean Reversion:** Buy assets that have fallen significantly below their historic average, expecting them to return to normal.

### 2. Mathematical Formulations
* **Moving Average Crossover Signal:**
  $$\text{Signal}_t = \text{sign}(\text{SMA}_{\text{fast}}(t) - \text{SMA}_{\text{slow}}(t))$$
* **Information Ratio (IR):**
  $$\text{IR} = \frac{\alpha}{\sigma_{\text{residual}}}$$

```text
Algorithm: SMA Crossover Strategy
Input: Historical price vector P, Fast window F, Slow window S
Output: Signal vector signal

signal = vector of zeros of size length(P)
for t = S to length(P):
    SMA_fast = mean(P[t-F+1 to t])
    SMA_slow = mean(P[t-S+1 to t])
    if SMA_fast > SMA_slow:
        signal[t] = 1
    else:
        signal[t] = -1
return signal
```
""",

        "L23_Machine_Learning.md": r"""# Machine Learning in Finance

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
""",

        "L24_Stochastic_Calculus.md": r"""# Stochastic Calculus & Stochastic Differential Equations (SDEs)

---

## 🕒 Lesson 24.1: Itô's Lemma

### 1. Intuition (ELIF5)
In standard calculus, the change in a function is the slope times the step size. But when the input wiggles randomly (like Brownian motion), the wiggles are so violent that their squared wiggles $(dW_t)^2$ accumulate over time. If the function is curved, this wiggling creates an extra drift term. Itô's Lemma is the mathematical formula that accounts for this extra drift.

### 2. Mathematical Formulations
For $dX_t = \mu_t dt + \sigma_t dW_t$, and a function $f(t, X_t)$:
$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial X} + \frac{1}{2} \sigma_t^2 \frac{\partial^2 f}{\partial X^2} \right) dt + \sigma_t \frac{\partial f}{\partial X} dW_t$$

```text
Algorithm: Euler-Maruyama GBM Simulation
Input: Initial Price S_0, Drift mu, Volatility sigma, Time horizon T, Steps N
Output: Simulated price path vector S of size N+1

dt = T / N
S[0] = S_0
for t = 1 to N:
    dW = sample normal N(0, dt)
    S[t] = S[t-1] + mu * S[t-1] * dt + sigma * S[t-1] * dW
return S
```

---

## 🕒 Lesson 24.2: Stochastic Differential Equations (SDEs)

### 1. Intuition (ELIF5)
An SDE describes a random path in terms of its average direction (drift) and its random wiggle (diffusion) at each point in time.

### 2. Mathematical Formulations
The Ornstein-Uhlenbeck (mean-reverting) SDE is:
$$dX_t = \theta(\mu - X_t) dt + \sigma dW_t$$
where $\theta$ is the speed of mean reversion, and $\mu$ is the long-term mean.
"""
    }

    for filename, content in chapters.items():
        file_path = os.path.join(theory_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    write_chapters()
