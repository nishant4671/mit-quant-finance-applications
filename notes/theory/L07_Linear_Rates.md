# Linear Rates, Swaps, and Short-Rate Models

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
