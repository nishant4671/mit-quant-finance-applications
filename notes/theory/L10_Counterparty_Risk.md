# Counterparty Credit Risk & Event Trading

---

## 🕒 Lesson 10.1: Counterparty Exposure

### 1. Intuition (ELIF5)
Counterparty risk is the risk that the party on the other side of a financial contract defaults before settling their obligations. The exposure is the amount of money you would lose if they defaulted today.

### 2. Mathematical Formulations
The exposure $E(t)$ of a derivative contract at time $t$ is:
$$E(t) = \max(V(t), 0)$$
where $V(t)$ is the market value of the contract.

---

## 🕒 Lesson 10.2: Credit Valuation Adjustment (CVA)

### 1. Intuition (ELIF5)
When trading with a counterparty that has default risk, you should discount the price of the contract to reflect this risk. CVA is the market value of this credit risk.

### 2. Mathematical Formulations
The CVA is computed as:
$$\text{CVA} = (1 - R) \int_0^T D(0, t) \cdot \text{EE}(t) \cdot d\text{PD}(t)$$
where $R$ is the recovery rate, $D(0,t)$ is the discount factor, $\text{EE}(t)$ is the expected exposure, and $\text{PD}(t)$ is the probability of default.
