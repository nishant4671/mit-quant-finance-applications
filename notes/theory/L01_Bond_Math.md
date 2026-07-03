# 📓 Lecture 1: Financial Terms, Concepts, and Bond Math

This chapter covers the foundations of bond math and fixed-income analytics, which form the bedrock of quantitative finance.

---

## 🕒 Lesson 1.1: Time Value of Money & Compounding

> [!NOTE]
> **Summary in 1 Sentence:** 
> Money has a time value because you can earn interest on it; therefore, a dollar today is worth more than a dollar tomorrow.

### 1. Intuition (ELIF5)
If you have **$100 today**, you can put it in a bank. The bank pays you "rent" to borrow your money. This rent is called **interest**. 

If you choose to receive that $100 five years from now instead, you lose out on 5 years of interest. 

* **Future Value (FV):** What your money grows into over time.
* **Present Value (PV):** What a future payment is worth to you right now (discounted to today).

### 2. Formulas

#### Discrete Compounding
Interest calculated at regular intervals $m$ times a year (e.g., quarterly $m=4$, semi-annually $m=2$, monthly $m=12$).
$$FV = PV \left(1 + \frac{r}{m}\right)^{m \cdot t}$$
$$PV = \frac{FV}{\left(1 + \frac{r}{m}\right)^{m \cdot t}}$$

#### Continuous Compounding
Interest calculated every infinitesimally small instant. Quants prefer continuous compounding because it makes calculus and derivative pricing much cleaner.
$$FV = PV \cdot e^{r \cdot t}$$
$$PV = FV \cdot e^{-r \cdot t}$$

---

## 🎟️ Lesson 1.2: Bond Pricing Mechanics

> [!NOTE]
> **Summary in 1 Sentence:**
> The fair price of a bond is simply the sum of all its future cash flows (coupons and principal repayment) discounted back to today using a chosen discount rate.

### 1. Intuition (ELIF5)
A bond is a loan certificate. If you buy a bond from a company or government, you are lending them money. In return, they promise to do two things:
1. Pay you regular "thank you" payments (called **coupons**).
2. Give you back your original loan amount (called the **face value** or **principal**) when the bond expires (**maturity**).

To figure out how much you should pay for this bond *today*, you just need to estimate what all those future cash flows are worth to you right now, and add them up.

### 2. Types of Bonds

* **Zero-Coupon Bonds (ZCBs):** These do not pay any coupons. They are sold at a discount (less than face value) and pay the full face value at maturity.
  $$P_{zcb} = \frac{F}{(1 + y/m)^{m \cdot T}} \quad \text{(Discrete)}$$
  $$P_{zcb} = F \cdot e^{-y \cdot T} \quad \text{(Continuous)}$$

* **Coupon-Bearing Bonds:** These make periodic coupon payments $C$ and pay the face value $F$ at maturity.
  $$P = \sum_{k=1}^{n} \frac{C}{\left(1 + \frac{y}{m}\right)^k} + \frac{F}{\left(1 + \frac{y}{m}\right)^n}$$
  Where:
  * $P$ = Bond Price
  * $C$ = Periodic coupon payment ($C = \frac{\text{Annual Coupon Rate} \times F}{m}$)
  * $F$ = Face Value (usually \$1,000 or \$100)
  * $y$ = Yield to Maturity (YTM)
  * $m$ = Number of coupon payments per year
  * $n$ = Total number of remaining coupon payments ($m \times T$)

### 3. Yield to Maturity (YTM)
The **YTM** is the single interest rate $y$ that makes the present value of the bond's cash flows exactly equal to its current market price. 
* There is no algebraic way to solve for $y$ in a coupon bond formula. Instead, we use numerical methods (like Newton-Raphson or Brent's method in Python) to find it.

---

## 📈 Lesson 1.3: Yield Curves & Spot Rates

> [!NOTE]
> **Summary in 1 Sentence:**
> A yield curve shows how interest rates change across different horizons (maturities), and spot rates are the true interest rates for single cash flows at specific future dates.

### 1. Intuition (ELIF5)
Imagine buying tickets for a train. A 1-mile ticket, a 5-mile ticket, and a 10-mile ticket don't cost the same per mile. Similarly, the interest rate you get for lending money for 1 month, 1 year, or 10 years is usually different. 

* **Yield Curve:** A line graph showing the yields of bonds of similar credit quality across different maturities. Usually, it slopes upward because lenders want higher interest for locking their money away longer.
* **Spot Rate ($r_t$):** The rate of interest for a single, isolated cash flow occurring at time $t$. 
* **Why YTM is NOT a Spot Rate:** YTM is a weighted average of spot rates across all coupon dates of a bond. For precise pricing, we must discount each individual coupon using the spot rate corresponding to its exact payment date.

### 2. Discount Factors and Bootstrapping
A **Discount Factor** $d(t)$ is the present value of \$1 received at time $t$.
$$d(t) = e^{-r(t) \cdot t} \quad \text{(Continuous)}$$
$$d(t) = \frac{1}{(1 + r(t))^t} \quad \text{(Discrete Annual)}$$

If we know the market prices of liquid coupon bonds, we can use a process called **bootstrapping** to solve for the spot rates (or discount factors) step-by-step:
1. Start with the shortest maturity bond (which acts like a zero-coupon bond). Solve for its spot rate.
2. Move to the next shortest bond. Use the spot rate found in Step 1 to discount its first coupon, and solve for the new spot rate for its final payment.
3. Repeat recursively.

---

## ⚖️ Lesson 1.4: Risk Sensitivity: Duration

> [!NOTE]
> **Summary in 1 Sentence:**
> Duration measures how long it takes to get your money back from a bond, and serves as a gauge for how sensitive the bond's price is to interest rate changes.

### 1. Intuition (ELIF5)
Imagine you are balancing a long plank of wood on your shoulder. On the plank, there are buckets of water (cash flows) at different distances (years). 
* **Macaulay Duration** is the exact balance point (the center of gravity) of those buckets. If you get coupons early, the balance point is closer to you.
* **Modified Duration** is the sensitivity of the balance point to a wobble. It tells you: *"If interest rates go up by 1%, by what percentage will my bond price fall?"*
  * **Higher Duration = Higher Risk (Wobbliness).**

### 2. Mathematical Formulations

#### Macaulay Duration ($D_{\text{mac}}$)
The weighted average time until cash flows are received, where the weights are the present values of the cash flows.
$$D_{\text{mac}} = \frac{\sum_{t} t \cdot \text{PV}(CF_t)}{P} = \frac{\sum_{t} t \cdot CF_t \cdot e^{-y \cdot t}}{P}$$

#### Modified Duration ($D_{\text{mod}}$)
Measures the percentage change in price for a unit change in yield.
$$D_{\text{mod}} = -\frac{1}{P} \frac{dP}{dy}$$

* **Discrete Compounding Relationship:**
  $$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + \frac{y}{m}}$$
* **Continuous Compounding Relationship:**
  $$D_{\text{mod}} = D_{\text{mac}}$$

For small changes in yield $\Delta y$:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y$$

---

## 🌊 Lesson 1.5: Risk Sensitivity: Convexity

> [!NOTE]
> **Summary in 1 Sentence:**
> Convexity measures the curvature of the bond price-yield relationship, showing how duration changes as yields shift, and correcting the duration estimate for larger interest rate moves.

### 1. Intuition (ELIF5)
If you draw a graph of a bond's price against interest rates, it is not a straight line; it is a curved, smiley-face shape (convex).
* **Duration** is a straight tangent line at your current position. It is a good approximation for tiny steps, but if yields jump, the straight line drifts away from the actual curve.
* **Convexity** measures the curve itself. It tells us how much the duration changes when yields move.
* Because of this curve, when rates fall, prices go up *faster* than duration predicts. When rates rise, prices fall *slower* than duration predicts. **Convexity is always good for the bondholder.**

### 2. Formulas
Convexity ($C$) is proportional to the second derivative of the bond price with respect to the yield:
$$C = \frac{1}{P} \frac{d^2 P}{dy^2}$$

* **Continuous Compounding Formula:**
  $$C = \frac{1}{P} \sum_{t} t^2 \cdot CF_t \cdot e^{-y \cdot t}$$
* **Discrete Compounding Formula:**
  $$C = \frac{1}{P \cdot (1 + y/m)^2} \sum_{k=1}^{n} \frac{k(k+1) \cdot CF_k}{m^2 \cdot (1 + y/m)^k}$$

#### The Complete Taylor Approximation
To estimate the percentage price change of a bond for any yield shock $\Delta y$, we combine Duration and Convexity:
$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2$$
