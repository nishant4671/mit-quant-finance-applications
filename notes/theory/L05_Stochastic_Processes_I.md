# Stochastic Processes I & Asset Return Modeling

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
