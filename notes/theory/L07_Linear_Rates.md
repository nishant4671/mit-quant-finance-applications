# Linear Rates, Swaps, and Short-Rate Models

---

## 🕒 Lesson 7.1: Libor, SOFR, and Forward Rates

> [!NOTE]
> **Summary in 1 Sentence:**
> Interest rate benchmarks represent the cost of borrowing cash, and forward rates are the implied future interest rates locked in today.

### 1. Intuition (ELIF5)
Imagine ordering a custom car today to be delivered in 1 year, and agreeing today on the price you will pay. A **Forward Rate** is the same thing for borrowing money: you lock in the interest rate today for a loan that starts in the future.

### 2. Formulas
The continuously compounded forward rate between $T_1$ and $T_2$ is:
$$f(0, T_1, T_2) = rac{r(0, T_2) T_2 - r(0, T_1) T_1}{T_2 - T_1}$$

---

## 🕒 Lesson 7.2: Interest Rate Swaps (IRS)

> [!NOTE]
> **Summary in 1 Sentence:**
> An Interest Rate Swap is an agreement to exchange fixed-rate interest payments for floating-rate interest payments over a specified horizon.

### 1. Intuition (ELIF5)
Imagine you borrow money to buy a house with a mortgage that changes price every month based on market rates (floating rate). You get nervous about rates rising, so you make a deal with a bank: you pay them a fixed amount every month, and in return, they pay your changing mortgage bill. You have swapped a floating-rate risk for a stable fixed-rate.

### 2. Formulas
The swap rate $S_n$ that makes the initial value of the swap zero is:
$$S_n = rac{1 - P(0, T_n)}{\sum_{i=1}^n lpha_i P(0, T_i)}$$
Where $P(0, T_i)$ is the discount factor to time $T_i$, and $lpha_i$ is the day-count fraction.
