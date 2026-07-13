import os

def write_missing():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    os.makedirs(theory_dir, exist_ok=True)

    chapters = {
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

---

## 🕒 Lesson 18.2: AI in Clinical Trial Forecasting

### 1. Intuition (ELIF5)
How do we know which drug projects are worth funding? We can use historical data from thousands of past clinical trials. AI models analyze patient sizes, chemical compound types, and the target diseases to predict whether a new drug will pass its trials, helping us select the best projects for our megafund.

### 2. Mathematical Formulations
We model the probability of trial success $p_k$ for drug $k$ using machine learning classification models (such as random forests or neural networks) trained on trial features $x_k$:
$$p_k = f(x_k; \theta) \in [0, 1]$$
We then optimize the portfolio weights $w_k$ to maximize expected portfolio value subject to value-at-risk limits.
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
"""
    }

    for filename, content in chapters.items():
        file_path = os.path.join(theory_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    write_missing()
