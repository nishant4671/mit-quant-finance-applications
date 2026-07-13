# Stochastic Calculus & Stochastic Differential Equations (SDEs)

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
$$df(t, X_t) = \left( rac{\partial f}{\partial t} + \mu_t rac{\partial f}{\partial X} + rac{1}{2} \sigma_t^2 rac{\partial^2 f}{\partial X^2} ight) dt + \sigma_t rac{\partial f}{\partial X} dW_t$$
Note that the extra term $rac{1}{2} \sigma_t^2 rac{\partial^2 f}{\partial X^2} dt$ arises because $(dW_t)^2 = dt$.

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
$$dX_t = 	heta(\mu - X_t) dt + \sigma dW_t$$
Where $	heta$ is the speed of mean reversion, and $\mu$ is the long-term mean.
