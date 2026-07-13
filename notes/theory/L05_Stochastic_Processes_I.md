# Stochastic Processes I & Asset Return Modeling

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
