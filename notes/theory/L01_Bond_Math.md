# 📓 Lecture 1: Financial Terms, Concepts, and Bond Math

---

## 🕒 Lesson 1.1: Time Value of Money & Compounding

### 1. The Core Intuition (ELIF5)
Imagine you have a slice of fresh bread. If you eat it today, it's delicious. If you wait a year to eat it, it will be moldy and worthless. 

Money is the opposite. If you have $100 today, you can buy things now. If you choose *not* to spend it and lend it to someone else (like a bank or a government) for a year, they have to pay you "rent" for using your money. That rent is **interest**. 

Because of this rent, **a dollar today is worth more than a dollar tomorrow**. 
* **Future Value (FV):** What your money will grow into if you let it gather interest.
* **Present Value (PV):** What a future payment promised to you is worth *right now* (we "discount" it because we have to wait for it).

---

### 2. The Mathematics

#### Discrete Compounding ($m$ times per year)
If you compound interest $m$ times a year (e.g., quarterly $m=4$, monthly $m=12$), the formula for Future Value after $n$ years is:

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \cdot n}$$

Where:
* $r$ = Annual interest rate (nominal rate)
* $m$ = Number of compounding periods per year
* $n$ = Number of years

#### Continuous Compounding ($m \to \infty$)
What if interest is compounded every day? Every second? Every instant? As $m$ goes to infinity, the math converges to the mathematical constant $e$ (Euler's number $\approx 2.71828$):

$$FV = PV \times e^{r \cdot n}$$

#### Why Quants Love Continuous Compounding
In the real world, bonds pay interest semi-annually or quarterly (discrete). But in quantitative finance, we almost always assume **continuous compounding** because:
1. **Calculus is clean:** The derivative of $e^{rx}$ is just $r e^{rx}$. It makes solving complex differential equations (like Black-Scholes) vastly simpler.
2. **Time transitions are smooth:** There are no sudden jumps in your portfolio value graph; it is a smooth, continuous curve.

---

### 3. Python Implementation

Let's write a simple implementation to compare how money grows under daily compounding versus continuous compounding.
