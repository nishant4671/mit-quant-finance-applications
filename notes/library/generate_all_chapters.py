import os

def write_chapters():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    os.makedirs(theory_dir, exist_ok=True)

    # Note: All string values are marked as raw strings (r""") to prevent Python from escaping backslashes like \f, \t, etc.
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

---

## 🕒 Lesson 1.3: Yield Curves & Spot Rates

### 1. Intuition (ELIF5)
If you borrow money for one day, one year, or ten years, the interest rate you pay is usually different. Lenders generally demand higher interest rates for longer loans to compensate for the risk of locking up their capital. A Yield Curve is a graphical plot of the interest rates of bonds with similar credit quality across different maturities. 
A Spot Rate is the interest rate applicable to a single, isolated cash flow occurring at a specific future date. While the Yield to Maturity represents a weighted average of discount rates over a bond's life, spot rates are the true rates used to discount individual cash flows.

### 2. Mathematical Formulations
The Discount Factor $d(t)$ represents the present value of $1 received at time $t$. Under continuous compounding, it is defined as:
$$d(t) = e^{-r(t) \cdot t}$$
where $r(t)$ is the spot rate for maturity $t$. Given a set of liquid coupon bond prices, we can recursively determine the spot rates using a method called bootstrapping. For the first period, the spot rate is derived directly from the short-term zero-coupon rate. For subsequent periods, the price of the bond is expressed as the sum of discounted coupons using previously calculated spot rates, plus the final payment discounted at the new spot rate, which is then solved algebraically.

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
""",

        "L05_Stochastic_Processes_I.md": r"""# Stochastic Processes I & Asset Return Modeling

---

## 🕒 Lesson 5.1: Random Walks & The Markov Property

### 1. Intuition (ELIF5)
A stochastic process is a sequence of random variables indexed by time, representing how a random system evolves. A random walk is a simple process where each step is random. The Markov Property states that the future path of the process depends only on its current state today, not on the path it took to get there. It is a "memoryless" process.

### 2. Mathematical Formulations
A discrete-time stochastic process $\{X_t\}$ satisfies the Markov property if:
$$P(X_{t+1} = x_{t+1} \mid X_t = x_t, X_{t-1} = x_{t-1}, \dots, X_0 = x_0) = P(X_{t+1} = x_{t+1} \mid X_t = x_t)$$

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

<h3>1. Intuition (ELIF5)</h3>
If you have too many variables in a model, it can overfit, meaning it memorizes the noise in the data and performs poorly on new data. Regularization adds a penalty to the OLS optimization to keep the coefficients small:
* **Ridge** shrinks all coefficients slightly.
* **Lasso** shrinks coefficients and forces the least important ones to exactly zero, acting as a variable filter.

### 2. Mathematical Formulations
* **Ridge Regression ($L_2$ Regularization):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \sum_{j=1}^p \beta_j^2$$
* **Lasso Regression ($L_1$ Regularization):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \sum_{j=1}^p |\beta_j|$$
""",

        "L07_Linear_Rates.md": r"""# Linear Rates, Swaps, and Short-Rate Models

---

## 🕒 Lesson 7.1: Benchmark Rates & Forward Rates

<h3>1. Intuition (ELIF5)</h3>
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
where $\epsilon_{t-1}^2$ is the squared residual from the mean equation, and $\sigma_{t-1}^2$ is the previous variance forecast.
""",

        "L09_PCA.md": r"""# Principal Component Analysis (PCA) in Finance

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
""",

        "L23_Machine_Learning.md": r"""# Machine Learning in Finance

---

## 🕒 Lesson 23.1: Supervised Learning & Overfitting

<h3>1. Intuition (ELIF5)</h3>
Machine learning models find complex non-linear patterns in data. However, because financial markets are noisy, models can easily overfit by memorizing historical noise, which leads to poor performance on new data.

### 2. Mathematical Formulations
To prevent overfitting, we minimize loss while penalizing model complexity:
$$\min_{\theta} \sum_{i=1}^n L(y_i, f(x_i; \theta)) + \lambda \|\theta\|_2^2$$
where $\lambda$ is the regularization strength.
""",

        "L24_Stochastic_Calculus.md": r"""# Stochastic Calculus & Stochastic Differential Equations (SDEs)

---

## 🕒 Lesson 24.1: Itô's Lemma

### 1. Intuition (ELIF5)
In standard calculus, the change in a function is the slope times the step size. But when the input wiggles randomly (like Brownian motion), the wiggles are so violent that their squared wiggles $(dW_t)^2$ accumulate over time. If the function is curved, this wiggling creates an extra drift term. Itô's Lemma is the mathematical formula that accounts for this extra drift.

### 2. Mathematical Formulations
For $dX_t = \mu_t dt + \sigma_t dW_t$, and a function $f(t, X_t)$:
$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial X} + \frac{1}{2} \sigma_t^2 \frac{\partial^2 f}{\partial X^2} \right) dt + \sigma_t \frac{\partial f}{\partial X} dW_t$$

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
