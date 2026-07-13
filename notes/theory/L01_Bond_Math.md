# Financial Terms, Concepts, and Bond Math

---

## 🕒 Lesson 1.1: Time Value of Money & Compounding

### 1. Intuition (ELIF5)
Imagine you have $100 today. You can deposit this money in a bank account, and the bank will pay you a fee for borrowing your cash over time. This fee is called interest. If you choose to receive $100 five years from now instead of today, you lose the opportunity to earn interest during those five years. Therefore, money today is worth more than the same amount of money in the future. The Present Value (PV) represents the current worth of a future cash flow, while the Future Value (FV) represents what that current sum will grow into over time.

### 2. Mathematical Formulations
If interest is compounded $m$ times per year at an annual nominal rate $r$, the Future Value after $t$ years is given by:
$$FV = PV \left(1 + \frac{r}{m}\right)^{m \cdot t}$$
Conversely, the Present Value is computed by discounting the Future Value back to the present:
$$PV = \frac{FV}{\left(1 + \frac{r}{m}\right)^{m \cdot t}}$$
In quantitative finance, we frequently assume interest is compounded continuously (i.e., $m \to \infty$). In this limit, the formulations simplify to:
$$FV = PV \cdot e^{r \cdot t}$$
$$PV = FV \cdot e^{-r \cdot t}$$

---

## 🕒 Lesson 1.2: Bond Pricing Mechanics

### 1. Intuition (ELIF5)
A bond is essentially a loan agreement between an investor and a borrower (such as a corporation or government). When you buy a bond, you lend money to the issuer. In return, the issuer promises to make periodic interest payments, known as coupons, and to return the original loan amount, called the face value or principal, when the bond matures. The fair price of a bond today is simply the sum of all its expected future cash flows, discounted back to the present using an appropriate discount rate.

### 2. Mathematical Formulations
For a zero-coupon bond (which pays no intermediate coupons and only returns the face value $F$ at maturity $T$), the price under continuous compounding is:
$$P_{\text{zcb}} = F \cdot e^{-y \cdot T}$$
For a coupon-bearing bond paying a periodic coupon $C$ $m$ times a year, the price $P$ is the sum of the discounted cash flows:
$$P = \sum_{k=1}^{n} \frac{C}{\left(1 + \frac{y}{m}\right)^k} + \frac{F}{\left(1 + \frac{y}{m}\right)^n}$$
where $y$ is the Yield to Maturity (YTM) and $n = m \cdot T$ is the total number of periods. The YTM is the single constant interest rate that equates the present value of the bond's cash flows to its current market price. Since this equation cannot be solved algebraically for $y$, numerical root-finding algorithms (such as the Newton-Raphson method) are required.

```text
Algorithm: Newton-Raphson YTM Solver
Input: Market Price P, Face Value F, Coupon C, Periods n, Annual Frequency m, Initial Guess y_0, Tolerance tol
Output: Yield to Maturity (YTM) y

y = y_0
repeat:
    P_est = sum( (C / m) / (1 + y/m)^t for t = 1 to n ) + F / (1 + y/m)^n
    dPes_dy = sum( -t * (C / m) / (1 + y/m)^(t+1) for t = 1 to n ) - n * F / (1 + y/m)^(n+1)
    y_new = y - (P_est - P) / dPes_dy
    if |y_new - y| < tol:
        return y_new
    y = y_new
```

---

## 🕒 Lesson 1.3: Yield Curves & Spot Rates

### 1. Intuition (ELIF5)
If you borrow money for one day, one year, or ten years, the interest rate you pay is usually different. Lenders generally demand higher interest rates for longer loans to compensate for the risk of locking up their capital. A Yield Curve is a graphical plot of the interest rates of bonds with similar credit quality across different maturities. 
A Spot Rate is the interest rate applicable to a single, isolated cash flow occurring at a specific future date. While the Yield to Maturity represents a weighted average of discount rates over a bond's life, spot rates are the true rates used to discount individual cash flows.

### 2. Mathematical Formulations
The Discount Factor $d(t)$ represents the present value of $1 received at time $t$. Under continuous compounding, it is defined as:
$$d(t) = e^{-r(t) \cdot t}$$
where $r(t)$ is the spot rate for maturity $t$. Given a set of liquid coupon bond prices, we can recursively determine the spot rates using a method called bootstrapping. For the first period, the spot rate is derived directly from the short-term zero-coupon rate. For subsequent periods, the price of the bond is expressed as the sum of discounted coupons using previously calculated spot rates, plus the final payment discounted at the new spot rate, which is then solved algebraically.

```text
Algorithm: Spot Rate Bootstrapping
Input: Prices of bonds P_i, maturities T_i, coupon payments C_i
Output: Spot rates r(T_i) for each maturity i

r = empty list of size N
for i = 1 to N:
    if T_i is first period:
        r[1] = ln( (F + C_1) / P_1 ) / T_1
    else:
        sum_prev_cf = sum( C_i * exp(-r[k] * T_k) for k = 1 to i-1 )
        r[i] = -ln( (P_i - sum_prev_cf) / (F + C_i) ) / T_i
return r
```

---

## 🕒 Lesson 1.4: Risk Sensitivity: Duration

### 1. Intuition (ELIF5)
Duration measures a bond's sensitivity to changes in interest rates. Imagine balancing a plank on your shoulder with weights distributed along it representing the cash flows. The Macaulay Duration represents the balance point or center of gravity of these cash flows. The Modified Duration measures the actual percentage change in the bond's price for a given change in interest rates. A higher duration means the bond's price will fluctuate more violently when interest rates move.

### 2. Mathematical Formulations
The Macaulay Duration ($D_{\text{mac}}$) is the weighted average time to receive all cash flows, where the weights are the present values of the cash flows:
$$D_{\text{mac}} = \frac{\sum_{t} t \cdot CF_t \cdot e^{-y \cdot t}}{P}$$
The Modified Duration ($D_{\text{mod}}$) measures the price sensitivity and is related to the derivative of price with respect to yield:
$$D_{\text{mod}} = -\frac{1}{P} \frac{dP}{dy}$$
Under discrete compounding, the relationship is:
$$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + \frac{y}{m}}$$
For small changes in yield $\Delta y$, the percentage price change is approximated linearly by:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y$$

---

## 🕒 Lesson 1.5: Risk Sensitivity: Convexity

### 1. Intuition (ELIF5)
Because the relationship between a bond's price and interest rates is curved (convex) rather than linear, a straight-line duration estimate becomes inaccurate for larger interest rate shocks. Convexity measures the curvature of this relationship. It describes how the duration of a bond changes as interest rates fluctuate. For plain bonds, convexity is positive, meaning that when interest rates fall, the price rises faster than duration predicts, and when rates rise, the price falls slower. This is the "convexity bonus" enjoyed by bondholders.

### 2. Mathematical Formulations
Convexity ($C$) is proportional to the second derivative of the bond price with respect to the yield:
$$C = \frac{1}{P} \frac{d^2 P}{dy^2}$$
Under discrete compounding, the formula is:
$$C = \frac{1}{P \cdot (1 + y/m)^2} \sum_{k=1}^{n} \frac{k(k+1) \cdot CF_k}{m^2 \cdot (1 + y/m)^k}$$
To obtain a highly accurate estimate of the percentage price change for a large yield shock $\Delta y$, we use the second-order Taylor series approximation:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2$$
