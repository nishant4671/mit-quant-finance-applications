# Building a Regulated Exchange for Trading on Events

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
