# Stochastic Processes II: Continuous Time

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
