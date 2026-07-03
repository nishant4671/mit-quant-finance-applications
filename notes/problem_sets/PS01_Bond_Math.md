# Problem Set 1: Bond Math

**MIT 18.642 — Topics in Mathematics with Applications in Finance**

---

## Preamble

This problem set covers the foundational mathematics of fixed-income securities, corresponding to **Lecture 1: Bond Math**. You will work through the core mechanics that every quantitative finance practitioner must master — from time-value-of-money arithmetic to full-curve bootstrapping and duration-based hedging.

### Topics Covered

- Compounding conventions (discrete and continuous)
- Present value, future value, and discount factors
- Zero-coupon and coupon bond pricing
- Yield to maturity (YTM) and its limitations
- Bootstrapping the spot rate curve from market data
- Macaulay Duration and Modified Duration
- Convexity and the Taylor series approximation for price changes
- Duration-based hedging and portfolio risk management

### Recommended Reading

- [L01_Bond_Math.md](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/lecture_notes/L01_Bond_Math.md) — Theory notes for Lecture 1
- MIT OCW 18.642 Lecture 1 materials
- Tuckman & Serrat, *Fixed Income Securities* — Chapters 1–4

---

## Rules & Instructions

1. **Show all work.** Partial credit is awarded for correct methodology even if the final answer contains arithmetic errors.
2. **State your assumptions** clearly (e.g., day-count conventions, compounding frequency).
3. **Use Python** for any numerical computations (bisection, Newton-Raphson, etc.). Include code snippets or pseudocode where appropriate.
4. **Express rates as percentages** to 4 decimal places (e.g., 5.2347%) unless otherwise instructed.
5. **Express prices in dollars** to 2 decimal places unless otherwise instructed.
6. **Difficulty ratings** are indicated by stars:
   - ⭐ = Foundational — tests core definitions and formulas
   - ⭐⭐ = Intermediate — requires multi-step reasoning and calculation
   - ⭐⭐⭐ = Advanced — integrates multiple concepts into a single pipeline
7. **Companion solutions** will be provided in `PS01_Bond_Math_Solutions.md` after you have attempted all problems.

---

## Problem 1 ⭐ — Compounding Frequency Showdown

You invest \$50,000 at a **nominal annual rate** of 8%.

**(a)** Compute the **future value** after 10 years under each compounding frequency:

| Frequency       | $m$ (periods/year) |
|-----------------|---------------------|
| Annual          | 1                   |
| Semi-annual     | 2                   |
| Quarterly       | 4                   |
| Monthly          | 12                  |
| Daily           | 365                 |
| Continuous      | $m \to \infty$      |

Use the formula:

$$FV = PV \cdot \left(1 + \frac{r}{m}\right)^{m \cdot t}$$

and for continuous compounding:

$$FV = PV \cdot e^{r \cdot t}$$

**(b)** What is the **absolute dollar difference** between annual and continuous compounding over this 10-year period?

**(c)** Derive the **Effective Annual Rate (EAR)** formula:

$$EAR = \left(1 + \frac{r}{m}\right)^m - 1$$

What does EAR converge to as $m \to \infty$? (Hint: recall the definition of $e$.)

---

## Problem 2 ⭐ — The Breakeven Investment

A company offers you two payment options:

- **Option A:** Receive \$25,000 today.
- **Option B:** Receive \$32,000 in 4 years.

**(a)** At what **continuously compounded annual rate** are the two options equivalent? (i.e., find the breakeven rate $r^*$ such that $PV(\text{Option B}) = \$25{,}000$.)

**(b)** If your personal discount rate is 7% (continuously compounded), which option do you prefer? Quantify the advantage in **today's dollars**.

**(c)** Suppose instead of a single payment, Option B pays \$8,000 per year for 4 years (at year-end). At a 7% continuously compounded rate, what is the **present value** of this annuity version of Option B? Which option wins now?

(Hint: For continuous discounting, each cash flow at time $t$ is discounted by $e^{-rt}$.)

---

## Problem 3 ⭐⭐ — Zero-Coupon Bond Pricing

Consider three **zero-coupon bonds** with face value \$1,000:

| Bond   | Maturity | Current Price |
|--------|----------|---------------|
| Bond A | 2 years  | \$925.00      |
| Bond B | 5 years  | \$780.00      |
| Bond C | 10 years | \$550.00      |

**(a)** Compute the **annual yield (YTM)** of each bond using annual compounding:

$$P = \frac{F}{(1 + y)^T} \implies y = \left(\frac{F}{P}\right)^{1/T} - 1$$

**(b)** Compute the **continuously compounded yield** of each bond:

$$P = F \cdot e^{-y_c \cdot T} \implies y_c = -\frac{1}{T} \ln\left(\frac{P}{F}\right)$$

**(c)** Is this yield curve **normal**, **flat**, or **inverted**? Explain what this shape implies about market expectations for future interest rates and economic conditions.

---

## Problem 4 ⭐⭐ — Coupon Bond Pricing & YTM

A 5-year **corporate bond** has:
- **Face value:** \$1,000
- **Coupon rate:** 6% annual, paid **semi-annually** (i.e., \$30 every 6 months)
- **Current market price:** \$965

**(a)** List all **10 cash flows** and their exact timing (in years). Present this as a table.

**(b)** Write the **bond pricing equation** explicitly, showing each discounted cash flow term:

$$P = \sum_{i=1}^{10} \frac{CF_i}{\left(1 + \frac{y}{2}\right)^i}$$

where $y$ is the annualized YTM under semi-annual compounding.

**(c)** Using **numerical methods** (e.g., bisection or Newton-Raphson in Python), find the bond's YTM to **4 decimal places** (semi-annual compounding convention). Report both the semi-annual rate $y/2$ and the annualized YTM $y$.

**(d)** If market rates **drop by 100 basis points** (i.e., use $y_{\text{new}} = y - 0.01$ as the new discount rate), what is the **new theoretical price** of this bond? What is the dollar gain?

---

## Problem 5 ⭐⭐ — Bootstrapping Spot Rates

You observe the following **par bonds** (bonds priced at face value = \$100) with annual coupons:

| Maturity | Coupon Rate |
|----------|-------------|
| 1 year   | 3.00%       |
| 2 years  | 3.50%       |
| 3 years  | 4.00%       |
| 4 years  | 4.25%       |

**(a)** **Bootstrap** the 1-year, 2-year, 3-year, and 4-year annual spot rates $r(1), r(2), r(3), r(4)$.

(Reminder: A par bond satisfies $P = F$. For the 1-year bond, $r(1)$ equals the coupon rate. For subsequent maturities, solve for $r(t)$ using previously determined spot rates.)

**(b)** Convert each spot rate to its **continuously compounded equivalent** $r_c(t)$:

$$r_c(t) = \ln\left(1 + r(t)\right)$$

**(c)** Compute the **discount factor** $d(t)$ for each maturity:

$$d(t) = \frac{1}{\left(1 + r(t)\right)^t}$$

**(d)** Using your bootstrapped spot rates, **price a NEW 4-year bond** with a 5% annual coupon and \$100 face value:

$$P = \sum_{t=1}^{4} \frac{C}{(1 + r(t))^t} + \frac{F}{(1 + r(4))^4}$$

---

## Problem 6 ⭐⭐ — Spot Rates vs. YTM: A Conceptual Challenge

*This problem tests your reasoning. Show your thinking clearly.*

**(a)** Explain in your own words why a bond's **YTM is NOT the same** as the spot rates for its maturity. Under what special condition would YTM and the spot rate be identical?

**(b)** Two 3-year bonds exist in the market:

- **Bond X:** Zero-coupon, priced at \$88.90, face value \$100
- **Bond Y:** 8% annual coupon, priced at \$108.00, face value \$100

Using Bond X, extract the **3-year spot rate** (annual compounding). Then explain: Is it valid to discount **ALL** of Bond Y's cash flows at this single 3-year spot rate? Why or why not?

**(c)** If the yield curve is **steeply upward-sloping**, will a coupon bond's YTM be **higher or lower** than the spot rate for its final maturity? Explain intuitively.

(Hint: Think about where the coupon payments fall on the yield curve relative to the final payment.)

---

## Problem 7 ⭐⭐ — Duration Deep Dive

Consider a 4-year bond with:
- **Face value:** \$1,000
- **Coupon rate:** 5% annual (paid annually)
- **YTM:** 6% (annual compounding)

**(a)** Calculate the **Macaulay Duration**. Show the full table with columns:

| $t$ | $CF_t$ | Discount Factor $(1+y)^{-t}$ | $PV(CF_t)$ | Weight $w_t = \frac{PV(CF_t)}{P}$ | $t \times w_t$ |
|-----|--------|-------------------------------|-------------|-------------------------------------|-----------------|

Sum the final column to get $D_{\text{Mac}}$.

**(b)** Calculate the **Modified Duration**:

$$D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y}$$

**(c)** Estimate the **percentage price change** if yields rise by 50 basis points ($\Delta y = +0.0050$), using duration only:

$$\frac{\Delta P}{P} \approx -D_{\text{Mod}} \cdot \Delta y$$

**(d)** If you hold a portfolio of **\$10,000,000 face value** of this bond and expect a parallel yield shift of **+75 bps**, estimate the **dollar change** in portfolio value.

(Note: First compute the market value of the portfolio at YTM = 6%, then apply the duration approximation.)

**(e)** A zero-coupon bond with the same maturity (4 years) has Macaulay Duration = 4.0. Explain **intuitively** why the coupon bond's duration is always less than its maturity.

---

## Problem 8 ⭐⭐ — Convexity and the Taylor Correction

*Using the same bond from Problem 7* (4-year, 5% coupon, 6% YTM, annual compounding):

**(a)** Calculate the **Convexity** of this bond. Show the full table with columns:

| $t$ | $CF_t$ | $PV(CF_t)$ | $t(t+1) \cdot PV(CF_t)$ |
|-----|--------|-------------|--------------------------|

Then compute:

$$\text{Convexity} = \frac{1}{P \cdot (1+y)^2} \sum_{t=1}^{T} t(t+1) \cdot PV(CF_t)$$

**(b)** For a yield shock of $\Delta y = +200$ bps ($+0.0200$), estimate $\Delta P / P$ using:

- **(i)** Duration only:

$$\frac{\Delta P}{P} \approx -D_{\text{Mod}} \cdot \Delta y$$

- **(ii)** Duration + Convexity (full Taylor approximation):

$$\frac{\Delta P}{P} \approx -D_{\text{Mod}} \cdot \Delta y + \frac{1}{2} \cdot \text{Convexity} \cdot (\Delta y)^2$$

**(c)** Calculate the **exact new price** at YTM = 8%. Compare the actual $\Delta P / P$ to your estimates in (b). Which is more accurate, and by how much (in basis points of price error)?

**(d)** Repeat parts (b) and (c) for a yield shock of $\Delta y = -200$ bps (i.e., YTM = 4%).

Show that convexity benefits the bondholder **asymmetrically**: prices rise MORE than duration predicts when rates fall, and fall LESS than duration predicts when rates rise. This is why convexity is always desirable.

---

## Problem 9 ⭐⭐⭐ — Full Pipeline: Bootstrap → Price → Hedge

The following market data is observed for **annual-coupon bonds** (face value \$100):

| Bond | Maturity | Coupon | Price    |
|------|----------|--------|----------|
| 1    | 1 year   | 0%     | \$97.09  |
| 2    | 2 years  | 4%     | \$100.95 |
| 3    | 3 years  | 5%     | \$102.78 |
| 4    | 4 years  | 5.5%   | \$103.43 |
| 5    | 5 years  | 6%     | \$105.01 |

**(a)** **Bootstrap** all 5 spot rates $r(1)$ through $r(5)$ using annual compounding.

(Note: Bond 1 is a zero-coupon bond, so $r(1)$ can be extracted directly. For subsequent bonds, use the recursive bootstrapping procedure with previously extracted spot rates.)

**(b)** Using the spot rates from (a), **price a new 5-year bond** with an **8% annual coupon** and \$100 face value:

$$P = \sum_{t=1}^{5} \frac{8}{(1 + r(t))^t} + \frac{100}{(1 + r(5))^5}$$

**(c)** Find the **YTM** of this new bond (annual compounding), then compute its **Macaulay Duration** and **Modified Duration**.

(Use a numerical solver for YTM. Then build the standard duration table using the YTM as discount rate.)

**(d)** You want to **hedge** \$1,000,000 face value of this 8% coupon bond using a **5-year zero-coupon bond** (priced using the 5-year spot rate from part (a)).

Compute the **hedge ratio**: How much face value of the zero-coupon bond must you hold so that the **dollar durations** of your positions are equal and opposite?

$$\text{Dollar Duration} = D_{\text{Mod}} \times \text{Market Value}$$

$$\text{Hedge Ratio} = \frac{DD_{\text{coupon bond}}}{DD_{\text{zero-coupon bond}}} \times \text{Face Value}_{\text{zero}}$$

---

## Problem 10 ⭐⭐⭐ — The Grand Challenge: Rate Shift Scenario Analysis

*Using the spot rate curve from Problem 9:*

**(a)** A portfolio consists of:

- **\$5,000,000 face value** of the 8% coupon bond from Problem 9
- **\$3,000,000 face value** of a **2-year zero-coupon bond**

Compute:
1. The **total portfolio market value** (price each component using the spot rates from Problem 9)
2. The **portfolio duration** (dollar-duration-weighted average)
3. The **portfolio convexity** (dollar-convexity-weighted average)

**(b)** Compute the **estimated portfolio P&L** for the following parallel yield curve shifts using the full Duration + Convexity Taylor approximation:

| Scenario | Shift $\Delta y$ |
|----------|-------------------|
| Rally    | $-150$ bps        |
| Sell-off | $+150$ bps        |
| Stress   | $+300$ bps        |

$$\Delta V \approx -DD \cdot \Delta y + \frac{1}{2} \cdot DC \cdot (\Delta y)^2$$

where $DD$ = portfolio dollar duration and $DC$ = portfolio dollar convexity.

**(c)** Compute the **exact portfolio values** under each scenario by **re-pricing each bond** with shifted spot rates (i.e., add $\Delta y$ to every spot rate). Compare to your Taylor estimates from (b).

Present results in a summary table:

| Scenario | Taylor Estimate $\Delta V$ | Exact $\Delta V$ | Approximation Error |
|----------|----------------------------|-------------------|---------------------|

**(d)** Discuss: For which scenario is the Taylor approximation **most inaccurate**, and why? What mathematical tool or technique would improve the approximation further?

(Hint: Think about higher-order terms in the Taylor expansion and the magnitude of $\Delta y$.)

---

> **📝 Note:** Companion solutions with full derivations and Python code will be provided in [`PS01_Bond_Math_Solutions.md`](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/problem_sets/PS01_Bond_Math_Solutions.md) after you have completed your attempt. Resist the temptation to peek — struggling with these problems is how the math becomes yours.
