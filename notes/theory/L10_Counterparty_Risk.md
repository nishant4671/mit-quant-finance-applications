# Counterparty Credit Risk & Event Trading

---

## 🕒 Lesson 10.1: Counterparty Exposure & Default

> [!NOTE]
> **Summary in 1 Sentence:**
> Counterparty Credit Risk is the risk that a counterparty defaults prior to the final settlement of a contract's cash flows.

### 1. Intuition (ELIF5)
Imagine you pay a store $1,000 today to deliver a TV next month. The risk is not that the TV breaks, but that the store goes out of business and closes down before they ship your TV. In financial markets, when you trade derivatives, you face this exact risk with your trading partners.

### 2. Formulas
* **Exposure at default (positive replacement value):**
  $$E(t) = \max(V(t), 0)$$
  Where $V(t)$ is the current market value of the contract.

---

## 🕒 Lesson 10.2: Credit Valuation Adjustment (CVA)

> [!NOTE]
> **Summary in 1 Sentence:**
> CVA is the market price of counterparty credit risk, calculated as the expected loss discounted to the present day.

### 1. Intuition (ELIF5)
If you buy an investment from a risky bank, you shouldn't pay full price. You should demand a discount to cover the risk that they might default. **CVA** is the mathematical calculation of that discount. It takes into account:
1. How much they owe you over time (Exposure).
2. How likely they are to default (Probability of Default).
3. What percentage of your money you can recover in bankruptcy court (Recovery Rate).

### 2. Formulas
$$	ext{CVA} = (1 - R) \int_0^T D(0, t) \cdot 	ext{EE}(t) \cdot d	ext{PD}(t)$$
Where:
* $R$ = Recovery rate
* $D(0, t)$ = Risk-free discount factor
* $	ext{EE}(t)$ = Expected Exposure at time $t$
* $	ext{PD}(t)$ = Probability of default function
