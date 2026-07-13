import os

def write_chapters():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    os.makedirs(theory_dir, exist_ok=True)

    chapters = {
        "L02_Linear_Algebra.md": """# Applied Linear Algebra in Quantitative Finance

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
$$\sigma_p^2 = w^T \Sigma w = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \text{Cov}(R_i, R_j)$$
""",

        "L03_Quant_Equity.md": """# Quantitative Equity Investing & Portfolio Optimization

---

## 🕒 Lesson 3.1: Modern Portfolio Theory (MPT)

> [!NOTE]
> **Summary in 1 Sentence:**
> Modern Portfolio Theory defines the optimal combination of risky assets that maximizes expected return for a given level of risk (variance).

### 1. Intuition (ELIF5)
Imagine you are packing a lunchbox. You want it to be as tasty as possible (high return) but with the lowest risk of causing an allergic reaction (low risk). Some ingredients taste great but are risky; others are safe but bland. MPT is a recipe that mixes these ingredients to give you the most delicious lunch possible for whatever level of risk you are willing to tolerate.

### 2. Formulas
* **Portfolio Return:**
  $$E[R_p] = w^T E[R]$$
* **Portfolio Variance:**
  $$\sigma_p^2 = w^T \Sigma w$$
* **Sharpe Ratio:**
  $$\text{Sharpe} = \frac{E[R_p] - R_f}{\sigma_p}$$

---

## 🕒 Lesson 3.2: Mean-Variance Optimization & The Efficient Frontier

> [!NOTE]
> **Summary in 1 Sentence:**
> The Efficient Frontier is the set of optimal portfolios that offer the highest expected return for defined risk levels, solved using quadratic programming.

### 1. Intuition (ELIF5)
If you plot all possible asset combinations on a chart with "Risk" on the bottom and "Return" on the side, you get a curved region. The top edge of this curve is the **Efficient Frontier**. Any portfolio on this line is optimal: you cannot get more return without taking more risk, and you cannot lower risk without giving up return.

### 2. Formulas
To find the weights $w$ of the optimal portfolio for risk aversion parameter $\lambda > 0$:
$$\max_{w} \left( w^T E[R] - \frac{\lambda}{2} w^T \Sigma w \right)$$
subject to:
$$w^T \mathbf{1} = 1 \quad \text{(Fully invested constraint)}$$
""",

        "L04_Probability_Theory.md": """# Probability Theory & Random Variables

---

## 🕒 Lesson 4.1: Random Variables & Distributions

> [!NOTE]
> **Summary in 1 Sentence:**
> Random variables model uncertain numerical outcomes, and probability density functions (PDFs) map the relative likelihood of these outcomes.

### 1. Intuition (ELIF5)
Imagine rolling a die. Before you roll, you don't know the number, but you know it must be 1, 2, 3, 4, 5, or 6, and each has a 1-in-6 chance. A **random variable** is the mathematical placeholder for this rolling die. The **probability distribution** is the rulebook that tells you how likely each outcome is.

### 2. Formulas
* **Expected Value (Mean $\mu$):**
  $$E[X] = \int_{-\infty}^{\infty} x f(x) dx$$
* **Variance ($\sigma^2$):**
  $$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$

---

## 🕒 Lesson 4.2: Normal vs. Log-Normal Distributions in Finance

> [!NOTE]
> **Summary in 1 Sentence:**
> Financial models assume asset returns are normally distributed (can be positive or negative) and asset prices are log-normally distributed (bounded below by zero).

### 1. Intuition (ELIF5)
A normal distribution (bell curve) goes off to infinity in both directions. However, a stock price cannot drop below zero (companies have limited liability; you can't owe money just for holding stock).
Therefore, we assume:
* **Asset Returns** follow a Normal distribution (you can lose -10% or gain +10%).
* **Asset Prices** follow a Log-Normal distribution (always positive, ranging from 0 to infinity).

### 2. Formulas
If $\ln(S_t) \sim N(\mu, \sigma^2)$, then $S_t$ is log-normally distributed with PDF:
$$f(s) = \frac{1}{s \sigma \sqrt{2\pi}} e^{-\frac{(\ln s - \mu)^2}{2\sigma^2}} \quad (s > 0)$$
""",

        "L05_Stochastic_Processes_I.md": """# Stochastic Processes I & Asset Return Modeling

---

## 🕒 Lesson 5.1: Random Walks & The Markov Property

> [!NOTE]
> **Summary in 1 Sentence:**
> A stochastic process is a sequence of random variables index by time, and the Markov property states that the future is conditionally independent of the past, given the present.

### 1. Intuition (ELIF5)
Imagine a frog jumping on lily pads. The frog's next jump depends only on the lily pad it is standing on *right now*. It doesn't matter if it traveled north, south, or did a flip to get there. The frog's path has no memory of the past. This memoryless rule is the **Markov Property**.

### 2. Formulas
For a sequence of states $X_0, X_1, X_2, \dots$:
$$P(X_{t+1} = x_{t+1} \mid X_t = x_t, X_{t-1} = x_{t-1}, \dots, X_0 = x_0) = P(X_{t+1} = x_{t+1} \mid X_t = x_t)$$

---

## 🕒 Lesson 5.2: Martingales (Fair Games)

> [!NOTE]
> **Summary in 1 Sentence:**
> A martingale is a stochastic model of a fair game where the expected future value, given all historical information, is equal to the current value.

### 1. Intuition (ELIF5)
Imagine playing a fair game of coin flipping with a friend. If you have $100 right now, and you bet $1 on each flip, on average you expect to have exactly $100 after the next flip because your chance of winning is 50/50. A **martingale** is any process where your best guess for the future is simply what you have right now.

### 2. Formulas
A process $X_t$ is a martingale with respect to information filtration $\mathcal{F}_t$ if:
$$E[|X_t|] < \infty$$
$$E[X_{t+1} \mid \mathcal{F}_t] = X_t$$
""",

        "L06_Regression_Analysis.md": """# Regression Analysis & Regularization

---

## 🕒 Lesson 6.1: Ordinary Least Squares (OLS)

> [!NOTE]
> **Summary in 1 Sentence:**
> Ordinary Least Squares fits a linear relationship by minimizing the sum of squared differences between observed values and predictions.

### 1. Intuition (ELIF5)
Imagine you want to predict a student's test score based on how many hours they studied. You plot the data points on a graph and use a ruler to draw a straight line through the middle of them. To make it the "best" line, you measure the vertical distance from each point to your line, square those distances (so positive and negative errors don't cancel out), and adjust the line until that total sum is as small as possible.

### 2. Formulas
We fit $y = X\beta + \epsilon$ by solving:
$$\min_{\beta} \|y - X\beta\|^2$$
The closed-form OLS solution is:
$$\hat{\beta} = (X^T X)^{-1} X^T y$$

---

## 🕒 Lesson 6.2: Regularization: Ridge & Lasso

> [!NOTE]
> **Summary in 1 Sentence:**
> Regularization prevents overfitting by adding a penalty term to the OLS loss function based on the magnitude of the model coefficients.

### 1. Intuition (ELIF5)
If you give a model too many variables (like predicting stock price using height of the CEO, weather in London, and interest rates), it will try to find patterns in the noise. Regularization is like a speed limit or a leash:
* **Ridge ($L_2$):** Shinks all coefficients toward zero, preventing any single variable from dominating.
* **Lasso ($L_1$):** Completely zeros out less important variables, acting as a built-in feature filter.

### 2. Formulas
* **Ridge (L2 Penalty):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \|\beta\|_2^2 = \min_{\beta} \sum_{i=1}^n (y_i - x_i^T \beta)^2 + \lambda \sum_{j=1}^p \beta_j^2$$
* **Lasso (L1 Penalty):**
  $$\min_{\beta} \|y - X\beta\|^2 + \lambda \|\beta\|_1 = \min_{\beta} \sum_{i=1}^n (y_i - x_i^T \beta)^2 + \lambda \sum_{j=1}^p |\beta_j|$$
""",

        "L07_Linear_Rates.md": """# Linear Rates, Swaps, and Short-Rate Models

---

## 🕒 Lesson 7.1: Libor, SOFR, and Forward Rates

> [!NOTE]
> **Summary in 1 Sentence:**
> Interest rate benchmarks represent the cost of borrowing cash, and forward rates are the implied future interest rates locked in today.

### 1. Intuition (ELIF5)
Imagine ordering a custom car today to be delivered in 1 year, and agreeing today on the price you will pay. A **Forward Rate** is the same thing for borrowing money: you lock in the interest rate today for a loan that starts in the future.

### 2. Formulas
The continuously compounded forward rate between $T_1$ and $T_2$ is:
$$f(0, T_1, T_2) = \frac{r(0, T_2) T_2 - r(0, T_1) T_1}{T_2 - T_1}$$

---

## 🕒 Lesson 7.2: Interest Rate Swaps (IRS)

> [!NOTE]
> **Summary in 1 Sentence:**
> An Interest Rate Swap is an agreement to exchange fixed-rate interest payments for floating-rate interest payments over a specified horizon.

### 1. Intuition (ELIF5)
Imagine you borrow money to buy a house with a mortgage that changes price every month based on market rates (floating rate). You get nervous about rates rising, so you make a deal with a bank: you pay them a fixed amount every month, and in return, they pay your changing mortgage bill. You have swapped a floating-rate risk for a stable fixed-rate.

### 2. Formulas
The swap rate $S_n$ that makes the initial value of the swap zero is:
$$S_n = \frac{1 - P(0, T_n)}{\sum_{i=1}^n \alpha_i P(0, T_i)}$$
Where $P(0, T_i)$ is the discount factor to time $T_i$, and $\alpha_i$ is the day-count fraction.
""",

        "L08_Time_Series.md": """# Time Series Analysis & Volatility Forecasting

---

## 🕒 Lesson 8.1: Stationarity & ARMA Models

> [!NOTE]
> **Summary in 1 Sentence:**
> Time series models analyze sequential data dependencies, requiring stationarity (constant mean and variance over time) to make stable forecasts.

### 1. Intuition (ELIF5)
Imagine you want to predict a child's height over time. If they are growing, the average height is constantly shifting upward (non-stationary). To model this, we look at the *change* in height from year to year, which is stable (stationary). 
* **Autoregressive (AR):** Uses past values to predict the future (e.g., if it rained yesterday, it might rain today).
* **Moving Average (MA):** Uses past random surprises (shocks) to adjust predictions.

### 2. Formulas
* **AR(1) Model:**
  $$X_t = c + \phi X_{t-1} + \epsilon_t$$
* **MA(1) Model:**
  $$X_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$$

---

## 🕒 Lesson 8.2: GARCH Volatility Modeling

> [!NOTE]
> **Summary in 1 Sentence:**
> GARCH models volatility clustering in financial returns, where high-volatility periods tend to feed into future high-volatility states.

### 1. Intuition (ELIF5)
Stock markets don't fluctuate at a constant speed. Instead, they have periods of relative calm and periods of extreme panic (volatility clustering). If the market was highly volatile yesterday, it is likely to remain volatile today. GARCH is the mathematical formula that models this "memory of volatility."

### 2. Formulas
For GARCH(1,1), the conditional variance $\sigma_t^2$ is modeled as:
$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
Where:
* $\omega$ = Baseline constant variance
* $\alpha$ = Sensitivity to yesterday's return shock ($\epsilon_{t-1}^2$)
* $\beta$ = Persistence of yesterday's volatility forecast ($\sigma_{t-1}^2$)
""",

        "L09_PCA.md": """# Principal Component Analysis (PCA) in Finance

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
""",

        "L10_Counterparty_Risk.md": """# Counterparty Credit Risk & Event Trading

---

## 🕒 Lesson 10.1: Counterparty Exposure & Default

> [!NOTE]
> **Summary in 1 Sentence:**
> Counterparty Credit Risk is the risk that a counterparty defaults prior to the final settlement of a contract's cash flows.

### 1. Intuition (ELIF5)
Imagine you pay a store $1,000 today to deliver a TV next month. The risk is not that the TV breaks, but that the store goes out of business and closes down before they ship your TV. In financial markets, when you trade derivatives, you face this exact risk with your trading partners.

### 2. Formulas
* **Exposure at default (positive replacement value):**
  $$E(t) = \max(V(t), 0)$$
  Where $V(t)$ is the current market value of the contract.

---

## 🕒 Lesson 10.2: Credit Valuation Adjustment (CVA)

> [!NOTE]
> **Summary in 1 Sentence:**
> CVA is the market price of counterparty credit risk, calculated as the expected loss discounted to the present day.

### 1. Intuition (ELIF5)
If you buy an investment from a risky bank, you shouldn't pay full price. You should demand a discount to cover the risk that they might default. **CVA** is the mathematical calculation of that discount. It takes into account:
1. How much they owe you over time (Exposure).
2. How likely they are to default (Probability of Default).
3. What percentage of your money you can recover in bankruptcy court (Recovery Rate).

### 2. Formulas
$$\text{CVA} = (1 - R) \int_0^T D(0, t) \cdot \text{EE}(t) \cdot d\text{PD}(t)$$
Where:
* $R$ = Recovery rate
* $D(0, t)$ = Risk-free discount factor
* $\text{EE}(t)$ = Expected Exposure at time $t$
* $\text{PD}(t)$ = Probability of default function
""",

        "L11_Portfolio_Management.md": """# Portfolio Management & Multi-Factor Models

---

## 🕒 Lesson 11.1: The Capital Asset Pricing Model (CAPM)

> [!NOTE]
> **Summary in 1 Sentence:**
> CAPM states that an asset's expected return is determined solely by its sensitivity to systematic market risk (Beta).

### 1. Intuition (ELIF5)
Imagine opening a business. You face two types of risk:
1. **Specific Risk:** The risk that your chef quits. You can fix this by hiring backup chefs (diversification). The market doesn't pay you extra for this risk because it's easy to avoid.
2. **Systemic Risk:** The risk of a major recession where no one goes out to eat. You cannot avoid this. The market rewards you with higher expected returns for taking this unavoidable risk.
**Beta ($\beta$)** measures how sensitive your business is to the general economy.

### 2. Formulas
* **Expected Return of Asset $i$:**
  $$E[R_i] = R_f + \beta_i (E[R_m] - R_f)$$
* **Beta Calculation:**
  $$\beta_i = \frac{\text{Cov}(R_i, R_m)}{\text{Var}(R_m)}$$

---

## 🕒 Lesson 11.2: Multi-Factor Risk Models

> [!NOTE]
> **Summary in 1 Sentence:**
> Multi-factor models decompose asset returns into exposures to multiple systematic risk factors plus an idiosyncratic residual.

### 1. Intuition (ELIF5)
Instead of saying a stock moves only because of the general market, we can use multiple factors to explain its return. For example, a stock might be sensitive to:
* The general stock market.
* Interest rate shifts.
* Oil prices.
* Inflation.
By identifying these "factors," we can build portfolios that are immune to specific risks (e.g., building a portfolio that doesn't care about oil price changes).

### 2. Formulas
$$R_i = \alpha_i + \beta_{i,1} F_1 + \beta_{i,2} F_2 + \dots + \beta_{i,k} F_k + \epsilon_i$$
Where $F_j$ are factor returns, $\beta_{i,j}$ are factor exposures (loadings), and $\epsilon_i$ is idiosyncratic noise.
""",

        "L14_Stochastic_Processes_II.md": """# Stochastic Processes II: Continuous Time

---

## 🕒 Lesson 14.1: Wiener Process (Brownian Motion)

> [!NOTE]
> **Summary in 1 Sentence:**
> A Wiener process is a continuous-time stochastic process characterized by stationary, independent, normally distributed increments.

### 1. Intuition (ELIF5)
Imagine a dust particle floating in a glass of water. It is hit constantly by tiny water molecules from random directions. The path of the dust particle is a **Wiener Process** (Brownian Motion). 
It is continuous (no teleporting), but it is so jagged that if you zoom in, it looks like a zigzag at every scale—it is nowhere differentiable (has no smooth slope).

### 2. Formulas
A process $W_t$ is a standard Wiener process if:
1. $W_0 = 0$
2. For any $t > s$, the increment $W_t - W_s \sim N(0, t-s)$
3. Increments are independent over non-overlapping intervals.
4. The path $t \mapsto W_t$ is continuous.

---

## 🕒 Lesson 14.2: Geometric Brownian Motion (GBM)

> [!NOTE]
> **Summary in 1 Sentence:**
> Geometric Brownian Motion models stock prices by assuming log-returns grow with a constant drift rate and random normal shocks.

### 1. Intuition (ELIF5)
We cannot use standard Brownian motion to model stock prices directly because:
1. A stock price cannot be negative.
2. A $1 change in a $100 stock is minor, but a $1 change in a $1 stock is huge.
**Geometric Brownian Motion** solves this: it models the *percentage* change in the stock price. It assumes the stock grows at a steady average rate (drift) plus a random wiggle that scales with the price of the stock.

### 2. Formulas
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
Where:
* $S_t$ = Stock price
* $\mu$ = Drift (expected annual growth rate)
* $\sigma$ = Volatility
* $dW_t$ = Standard Brownian motion increment
""",

        "L19_Volatility_Modeling.md": """# Volatility Modeling & The Term Structure of Volatility

---

## 🕒 Lesson 19.1: Realized vs. Implied Volatility

> [!NOTE]
> **Summary in 1 Sentence:**
> Realized volatility measures past price dispersion from historical data, whereas implied volatility reflects forward-looking market expectations backed out of option prices.

### 1. Intuition (ELIF5)
* **Realized Volatility:** Look at the weather records for the last 30 days and calculate how much the temperature fluctuated. This is historical fact.
* **Implied Volatility:** Look at the price of umbrellas being sold today. If umbrellas are expensive, people expect a storm soon. Implied volatility is what option prices tell us about the market's expectation of future volatility.

### 2. Formulas
* **Realized Volatility (Annualized):**
  $$\sigma_{\text{historical}} = \sqrt{\frac{252}{N-1} \sum_{i=1}^N (R_i - \bar{R})^2}$$
* **Implied Volatility ($\sigma_{\text{impl}}$):**
  Solved by finding the root:
  $$C_{\text{market}} - \text{BlackScholesCall}(S, K, T, r, \sigma_{\text{impl}}) = 0$$
""",

        "L21_Black_Scholes.md": """# The Black-Scholes Model & Option Pricing

---

## 🕒 Lesson 21.1: Replicating Portfolios & Delta Hedging

> [!NOTE]
> **Summary in 1 Sentence:**
> Option pricing relies on the principle of dynamic replication, where a derivative's payoff is matched by continuously adjusting a portfolio of stock and risk-free cash.

### 1. Intuition (ELIF5)
How do you price an option? Black and Scholes realized that you don't need to guess if the stock will go up or down. Instead, you can build a synthetic version of the option by buying a specific amount of the stock (called **Delta**) and borrowing cash. 
If the stock price rises, you buy a bit more stock; if it falls, you sell some. The price of the option is simply the initial cost of setting up this replicating portfolio.

### 2. Formulas
* **Replicating Portfolio Value:**
  $$V_{\text{portfolio}} = \Delta_t S_t + \psi_t B_t$$
  Where $\Delta_t = \frac{\partial V}{\partial S}$ is the option delta, and $B_t$ is the risk-free bond.

---

## 🕒 Lesson 21.2: The Black-Scholes Formula

> [!NOTE]
> **Summary in 1 Sentence:**
> The Black-Scholes formula provides the analytical price of European options under constant interest rates and log-normal asset volatility.

### 1. Intuition (ELIF5)
The Black-Scholes formula is a recipe to calculate the fair price of an option. It takes 5 inputs: stock price ($S$), strike price ($K$), time to maturity ($T$), interest rate ($r$), and volatility ($\sigma$). It outputs the exact price of the option by weighting the probability that the option will end up in-the-money.

### 2. Formulas
The European call price $C(S, t)$ is:
$$C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$$
Where:
* $d_1 = \frac{\ln(S_t/K) + \left(r + \sigma^2/2\right)(T-t)}{\sigma\sqrt{T-t}}$
* $d_2 = d_1 - \sigma\sqrt{T-t}$
* $N(x)$ = Cumulative normal distribution function
""",

        "L22_Systematic_Trading.md": """# Systematic Trading Strategies

---

## 🕒 Lesson 22.1: Trend Following & Mean Reversion

> [!NOTE]
> **Summary in 1 Sentence:**
> Systematic trading applies rule-based algorithms to capture market inefficiencies, categorized into trend-following (momentum) and mean-reversion strategies.

### 1. Intuition (ELIF5)
Systematic trading means taking the human emotion out of investing by writing a strict rulebook for a computer:
* **Trend Following:** "If a stock has been rising for a month, buy it because it has momentum." (Like hopping onto a moving train).
* **Mean Reversion:** "If a stock's price drops way lower than its historic average, buy it because it will likely snap back to normal." (Like stretching a rubber band).

### 2. Formulas
* **Simple Moving Average (SMA):**
  $$\text{SMA}_n(t) = \frac{1}{n} \sum_{i=0}^{n-1} S_{t-i}$$
* **Trading Signal (Crossover):**
  $$\text{Signal}_t = \text{sign}(\text{SMA}_{\text{fast}}(t) - \text{SMA}_{\text{slow}}(t))$$

---

## 🕒 Lesson 22.2: Strategy Evaluation Metrics

> [!NOTE]
> **Summary in 1 Sentence:**
> Quantitative strategies are evaluated on risk-adjusted metrics like the Sharpe ratio, Maximum Drawdown, and Information Ratio.

### 1. Intuition (ELIF5)
You shouldn't just look at how much money a trading bot made. If it made 50% but almost went bankrupt three times during the year, it is highly dangerous. We use metrics to judge if the returns were worth the stress:
* **Max Drawdown:** The biggest peak-to-trough drop in account value.
* **Sharpe Ratio:** Reward per unit of risk.

### 2. Formulas
* **Annualized Sharpe Ratio:**
  $$\text{Sharpe} = \frac{\text{Mean Annualized Return} - R_f}{\text{Standard Deviation of Annualized Returns}}$$
* **Maximum Drawdown (MDD):**
  $$\text{MDD}_T = \max_{t \in [0, T]} \left( \frac{\max_{s \in [0, t]} P_s - P_t}{\max_{s \in [0, t]} P_s} \right)$$
""",

        "L23_Machine_Learning.md": """# Machine Learning in Finance

---

## 🕒 Lesson 23.1: Supervised Learning & Overfitting in Finance

> [!NOTE]
> **Summary in 1 Sentence:**
> Machine learning identifies complex, non-linear relationships in financial data, but requires strict validation to prevent memorizing historical noise.

### 1. Intuition (ELIF5)
Financial data is incredibly noisy. If you give a highly flexible machine learning model free rein to predict tomorrow's stock price, it will memorize historical patterns that were pure coincidence (like "the stock always rises on rainy Tuesdays when the CEO wears blue"). This is **overfitting**. When you run the model on new data, it fails.

### 2. Formulas
We minimize training loss plus a complexity penalty (regularization):
$$\mathcal{L}(\theta) = \sum_{i=1}^n L(y_i, f(x_i; \theta)) + \Omega(\theta)$$

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
$$\hat{f}_{\text{rf}}(x) = \frac{1}{B} \sum_{b=1}^B T_b(x)$$
""",

        "L24_Stochastic_Calculus.md": """# Stochastic Calculus & Stochastic Differential Equations (SDEs)

---

## 🕒 Lesson 24.1: Itô's Lemma (The Core of Quant Math)

> [!NOTE]
> **Summary in 1 Sentence:**
> Itô's Lemma is the stochastic equivalent of the chain rule in calculus, introducing a second-order term to account for the quadratic variation of Brownian motion.

### 1. Intuition (ELIF5)
In normal calculus, if you have a function $f(x)$ and $x$ moves by a tiny step $dx$, the change in $f$ is just the slope times the step: $df = f'(x) dx$.
But if $x$ is a random, jittery path (like a stock price driven by Brownian motion), the jitters are so violent that their squared wiggles $(dx)^2$ actually add up over time. If your function is curved, these wiggles create an extra drift. **Itô's Lemma** is the formula that captures this extra drift (the curvature effect).

### 2. Formulas
If $dX_t = \mu_t dt + \sigma_t dW_t$, and $f(t, X_t)$ is twice-differentiable, then:
$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \mu_t \frac{\partial f}{\partial X} + \frac{1}{2} \sigma_t^2 \frac{\partial^2 f}{\partial X^2} \right) dt + \sigma_t \frac{\partial f}{\partial X} dW_t$$
Note that the extra term $\frac{1}{2} \sigma_t^2 \frac{\partial^2 f}{\partial X^2} dt$ arises because $(dW_t)^2 = dt$.

---

## 🕒 Lesson 24.2: Stochastic Differential Equations (SDEs)

> [!NOTE]
> **Summary in 1 Sentence:**
> SDEs model paths that evolve under a deterministic drift and a random diffusion term, solved using stochastic integration.

### 1. Intuition (ELIF5)
An SDE is like a recipe for a random path. It tells you:
1. **Drift:** Which direction the path wants to go on average (e.g., drift up by 5% per year).
2. **Diffusion:** How much random jitter to add at each step.
We use SDEs to model interest rates, asset prices, and volatility.

### 2. Formulas
A general SDE has the form:
$$dX_t = b(t, X_t) dt + \sigma(t, X_t) dW_t$$
Example: The **Ornstein-Uhlenbeck Process** (used to model mean-reverting interest rates or volatility):
$$dX_t = \theta(\mu - X_t) dt + \sigma dW_t$$
Where $\theta$ is the speed of mean reversion, and $\mu$ is the long-term mean.
"""
    }

    for filename, content in chapters.items():
        file_path = os.path.join(theory_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    write_chapters()
