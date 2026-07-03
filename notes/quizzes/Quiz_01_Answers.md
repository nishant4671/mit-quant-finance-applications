# 📝 Quiz 1 Answers: Lecture 1 (Bond Math)

> ⚠️ **DO NOT READ THIS FILE** until you have completed `Quiz_01_Bond_Math.md` and submitted your answers.

---

## Part A: Conceptual Answers

**A1:** Money has a time value because it can be invested to earn a return (interest). A dollar today can be put in a bank or invested, and it will grow over time. For example, $100 deposited at 5% annual interest becomes $105 after one year. Therefore, receiving $100 today is *more valuable* than receiving $100 a year from now, because you lose out on that earning potential.

**A2:** A **zero-coupon bond (ZCB)** pays no coupons; you buy it at a discount and receive the face value at maturity. A **coupon-bearing bond** pays periodic interest payments (coupons) plus the face value at maturity. The ZCB *always* has a longer duration than a coupon bond with the same maturity, because its Macaulay Duration equals its maturity (all cash flow is at the end), while coupon payments pull the duration of a coupon bond toward the present.

**A3:** Continuous compounding uses the exponential function ($e^{rt}$), which is infinitely differentiable and has clean derivatives ($\frac{d}{dt} e^{rt} = r \cdot e^{rt}$). This makes calculus-based derivations (pricing derivatives, computing duration, modeling stochastic processes) much simpler. There are no messy $(1 + r/m)$ terms to deal with.

**A4:** A **spot rate** $r(t)$ is the interest rate for a single, isolated cash flow at time $t$. **YTM** is a single rate that, when used to discount *all* of a bond's cash flows, gives its market price. YTM is essentially a weighted average of spot rates across all coupon dates. It's "misleading" because it assumes all coupons can be reinvested at the same YTM rate, which is generally not true. Two bonds with the same YTM but different coupon structures can have very different risk profiles.

**A5:** Positive convexity means the bond's price-yield curve is "bowed" (convex upward). For the bondholder, this is always beneficial: when rates *fall*, the bond price rises *faster* than a straight-line (duration-only) estimate would predict. When rates *rise*, the bond price falls *slower* than predicted. So the bondholder gets more upside and less downside than duration alone would suggest.

---

## Part B: Computation Answers

**A6:** 
$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \times t} = 5000 \times \left(1 + \frac{0.04}{4}\right)^{4 \times 8} = 5000 \times (1.01)^{32}$$

$(1.01)^{32} \approx 1.3749$

$$FV \approx 5000 \times 1.3749 = \$6,874.50$$

**A7:**
$$P = F \times e^{-r \times t} = 100 \times e^{-0.06 \times 5} = 100 \times e^{-0.30}$$

$e^{-0.30} \approx 0.7408$

$$P \approx 100 \times 0.7408 = \$74.08$$

**A8:**

(a) **Duration only:**
$$\frac{\Delta P}{P} \approx -D_{mod} \times \Delta y = -7.2 \times 0.015 = -0.108 = -10.80\%$$

(b) **Duration + Convexity:**
$$\frac{\Delta P}{P} \approx -D_{mod} \times \Delta y + \frac{1}{2} C \times (\Delta y)^2$$
$$= -7.2 \times 0.015 + \frac{1}{2} \times 68 \times (0.015)^2$$
$$= -0.108 + 0.5 \times 68 \times 0.000225$$
$$= -0.108 + 0.00765 = -0.10035 = -10.04\%$$

The convexity correction reduces the estimated loss by about 0.77 percentage points, making the estimate more accurate.

---

## Part C: Reasoning Answers

**A9:** SVB held a large portfolio of long-dated bonds (10+ year Treasuries and mortgage-backed securities). Long-dated bonds have **high duration**, meaning their prices are extremely sensitive to interest rate changes. When the Fed raised rates by ~500bps in 2022–2023:
- Using duration: If the portfolio had a Modified Duration of ~8, a 5% rate rise implies roughly $-8 \times 0.05 = -40\%$ in price decline.
- The convexity term provides some cushion, but for very large rate moves, even convexity doesn't fully capture the loss.
- **What they could have done:** (1) **Hedge duration** using interest rate swaps or Treasury futures to reduce the portfolio's net duration, (2) **Shorten maturity** by holding shorter-dated bonds, (3) **Immunize** by matching the duration of assets to the duration of liabilities (depositor claims).

**A10:** Bootstrapping works step-by-step:
1. **Year 1:** Bond A is a 1-year bond. Its only cash flow is the coupon + face value at Year 1. Since we know its price, we can directly solve for the 1-year spot rate $r_1$.
2. **Year 2:** Bond B pays a coupon at Year 1 and (coupon + face) at Year 2. We already know $r_1$, so we discount the Year 1 coupon using it. The remaining price must come from the Year 2 payment, which lets us solve for $r_2$.
3. **Year 3:** Bond C pays coupons at Years 1, 2, and 3. We discount the Year 1 and Year 2 coupons using $r_1$ and $r_2$. The remainder reveals $r_3$.

**Key assumption:** The bonds have no credit risk (or identical credit quality), so the only difference between them is maturity. This means any price difference reflects pure time-value-of-money differences, which is what the spot rates capture.
