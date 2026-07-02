# 📓 Lecture 1: Financial Terms, Concepts, and Bond Math

---

## 🕒 Lesson 1.1: Time Value of Money & Compounding

> [!NOTE]
> **Summary in 1 Sentence:** 
> Money has a time value because you can earn interest on it; therefore, a dollar today is worth more than a dollar tomorrow.

---

### 1. Intuition (ELIF5)
If you have **$100 today**, you can put it in a bank. The bank pays you "rent" to borrow your money. This rent is called **interest**. 

If you choose to receive that $100 five years from now instead, you lose out on 5 years of interest. 

* **Future Value (FV):** What your money grows into over time.
* **Present Value (PV):** What a future payment is worth to you right now (discounted to today).

---

### 2. The Formulas (Simplified)

#### Option A: Discrete Compounding (Interest calculated monthly, quarterly, etc.)
The bank calculates interest at regular intervals $m$ times a year.

* **Plain Text Formula:**
  `FV = PV * (1 + r/m)**(m * t)`
* **Variables:**
  * `PV` = Present Value (Starting money)
  * `r`  = Annual interest rate (e.g., 0.05 for 5%)
  * `m`  = Times compounded per year (12 for monthly, 4 for quarterly)
  * `t`  = Time in years

---

#### Option B: Continuous Compounding (Interest calculated every instant)
The bank calculates interest constantly, without stopping. This uses the mathematical constant `e` (approx 2.718).

* **Plain Text Formula:**
  `FV = PV * e**(r * t)`
* **Why Quants Use This:**
  It makes calculus easy. There are no abrupt steps or jumps in your returns; they flow along a smooth, predictable curve.

---

#### Option C: Discounting (Going backward in time)
Calculating what future money is worth to you today.

* **Plain Text Formula (Continuous):**
  `PV = FV * e**(-r * t)`

---

### 3. Cheat Sheet Table

| Frequency | Formula | Python Code |
| :--- | :--- | :--- |
| **Discrete (compounding)** | `FV = PV * (1 + r/m)**(m*t)` | `PV * (1 + r/m)**(m*t)` |
| **Continuous (compounding)** | `FV = PV * e**(r*t)` | `PV * np.exp(r * t)` |
| **Continuous (discounting)** | `PV = FV * e**(-r*t)` | `FV * np.exp(-r * t)` |

---

> [!TIP]
> **Quick Rule of 72:**
> To estimate how long it takes to double your money at a discrete interest rate `R%`, divide 72 by `R`. 
> * For 6% interest: `72 / 6 = 12 years` (approximate).
> * Using the exact continuous formula: `ln(2) / 0.06 = 11.55 years` (exact).
