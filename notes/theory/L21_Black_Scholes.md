# The Black-Scholes Model & Option Pricing

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
  $$V_{	ext{portfolio}} = \Delta_t S_t + \psi_t B_t$$
  Where $\Delta_t = rac{\partial V}{\partial S}$ is the option delta, and $B_t$ is the risk-free bond.

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
* $d_1 = rac{\ln(S_t/K) + \left(r + \sigma^2/2ight)(T-t)}{\sigma\sqrt{T-t}}$
* $d_2 = d_1 - \sigma\sqrt{T-t}$
* $N(x)$ = Cumulative normal distribution function
