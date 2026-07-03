# 📘 Problem Set 1 — Solutions Manual: Bond Math

> **Course:** MIT 18.642 — Topics in Mathematics with Applications in Finance  
> **Topic:** Bond Pricing, Yield Curves, Duration & Convexity  
> **Date:** July 2026

---

## Problem 1: Compounding Frequency Showdown

**Setup:** Invest $\text{PV} = \$50{,}000$ at $r = 8\%$ nominal for $t = 10$ years.

### Part (a): Future Value Under Each Compounding Frequency

The discrete compounding formula is:

$$FV = PV \left(1 + \frac{r}{m}\right)^{m \cdot t}$$

The continuous compounding formula is:

$$FV = PV \cdot e^{r \cdot t}$$

---

**Annual ($m = 1$):**

$$FV = 50{,}000 \times (1 + 0.08)^{10} = 50{,}000 \times (1.08)^{10}$$

Compute $(1.08)^{10}$:

$$
(1.08)^2 = 1.1664, \quad
(1.08)^4 = (1.1664)^2 = 1.36048896
$$
$$
(1.08)^8 = (1.36048896)^2 = 1.85093021, \quad
(1.08)^{10} = 1.85093021 \times 1.1664 = 2.15892500
$$

$$\boxed{FV_{\text{annual}} = 50{,}000 \times 2.15892500 = \$107{,}946.25}$$

---

**Semi-annual ($m = 2$):**

$$FV = 50{,}000 \times (1.04)^{20}$$

Compute $(1.04)^{20}$:

$$
(1.04)^2 = 1.0816, \quad
(1.04)^4 = 1.16985856, \quad
(1.04)^{10} = (1.04)^{8} \times (1.04)^{2}
$$
$$
(1.04)^{8} = (1.16985856)^2 = 1.36856905
$$
$$
(1.04)^{10} = 1.36856905 \times 1.0816 = 1.48024310
$$
$$
(1.04)^{20} = (1.48024310)^2 = 2.19111914
$$

$$\boxed{FV_{\text{semi}} = 50{,}000 \times 2.19111914 = \$109{,}555.96}$$

---

**Quarterly ($m = 4$):**

$$FV = 50{,}000 \times (1.02)^{40}$$

Compute $(1.02)^{40}$:

$$
(1.02)^2 = 1.0404, \quad
(1.02)^4 = 1.08243216, \quad
(1.02)^{8} = 1.17165938
$$
$$
(1.02)^{16} = 1.37278571, \quad
(1.02)^{32} = 1.88454483
$$
$$
(1.02)^{40} = 1.88454483 \times 1.17165938 = 2.20803966
$$

$$\boxed{FV_{\text{quarterly}} = 50{,}000 \times 2.20803966 = \$110{,}401.98}$$

---

**Monthly ($m = 12$):**

$$FV = 50{,}000 \times \left(1 + \frac{0.08}{12}\right)^{120} = 50{,}000 \times (1.00\overline{6})^{120}$$

Using logarithms: $\ln(1.006\overline{6}) = 0.0066445$, so $120 \times 0.0066445 = 0.79734$

$$(1.006\overline{6})^{120} = e^{0.79734} = 2.21964$$

$$\boxed{FV_{\text{monthly}} = 50{,}000 \times 2.21964 = \$110{,}982.01}$$

---

**Daily ($m = 365$):**

$$FV = 50{,}000 \times \left(1 + \frac{0.08}{365}\right)^{3650}$$

$\ln(1 + 0.08/365) = \ln(1.000219178) \approx 0.000219154$

$$3650 \times 0.000219154 = 0.799913$$

$$(1.000219178)^{3650} = e^{0.799913} = 2.22535$$

$$\boxed{FV_{\text{daily}} = 50{,}000 \times 2.22535 = \$111{,}267.65}$$

---

**Continuous ($m \to \infty$):**

$$FV = 50{,}000 \times e^{0.08 \times 10} = 50{,}000 \times e^{0.8}$$

$$e^{0.8} = 2.22554093$$

$$\boxed{FV_{\text{continuous}} = 50{,}000 \times 2.22554093 = \$111{,}277.05}$$

---

### Part (b): Difference Between Continuous and Annual

$$\Delta FV = FV_{\text{continuous}} - FV_{\text{annual}} = 111{,}277.05 - 107{,}946.25 = \boxed{\$3{,}330.80}$$

**Interpretation:** More frequent compounding earns "interest on interest" more often. The maximum benefit (continuous over annual) is about **\$3,331** on a \$50,000 investment over 10 years.

---

### Part (c): Effective Annual Rate (EAR)

$$\text{EAR} = \left(1 + \frac{r}{m}\right)^m - 1$$

| Frequency | $m$ | EAR Formula | EAR |
|-----------|-----|-------------|-----|
| Annual | 1 | $(1.08)^1 - 1$ | 8.0000% |
| Semi-annual | 2 | $(1.04)^2 - 1$ | 8.1600% |
| Quarterly | 4 | $(1.02)^4 - 1$ | 8.2432% |
| Monthly | 12 | $(1.00\overline{6})^{12} - 1$ | 8.2999% |
| Daily | 365 | $(1.000219)^{365} - 1$ | 8.3277% |
| Continuous | $\infty$ | $e^{0.08} - 1$ | 8.3287% |

As $m \to \infty$:

$$\left(1 + \frac{r}{m}\right)^m \to e^r \quad \Rightarrow \quad \text{EAR} \to e^r - 1 = e^{0.08} - 1 = 0.083287 = 8.3287\%$$

---

### Python Verification

```python
import numpy as np

PV, r, t = 50_000, 0.08, 10

# Part (a): Future values
freqs = {'Annual': 1, 'Semi-annual': 2, 'Quarterly': 4,
         'Monthly': 12, 'Daily': 365}

print("=" * 55)
print("Problem 1: Compounding Frequency Showdown")
print("=" * 55)

fv_values = {}
for name, m in freqs.items():
    fv = PV * (1 + r / m) ** (m * t)
    fv_values[name] = fv
    print(f"  {name:15s} (m={m:>3d}): FV = ${fv:,.4f}")

fv_cont = PV * np.exp(r * t)
fv_values['Continuous'] = fv_cont
print(f"  {'Continuous':15s} (m→∞) : FV = ${fv_cont:,.4f}")

# Part (b): Difference
diff = fv_cont - fv_values['Annual']
print(f"\n  Difference (continuous - annual): ${diff:,.4f}")

# Part (c): EAR
print("\n  Effective Annual Rates:")
for name, m in freqs.items():
    ear = (1 + r / m) ** m - 1
    print(f"    {name:15s}: EAR = {ear:.6%}")
ear_cont = np.exp(r) - 1
print(f"    {'Continuous':15s}: EAR = {ear_cont:.6%}")
```

---

> **Answer Summary — Problem 1**
>
> | Frequency | FV |
> |---|---|
> | Annual | $107,946.25 |
> | Semi-annual | $109,555.96 |
> | Quarterly | $110,401.98 |
> | Monthly | $110,982.01 |
> | Daily | $111,267.65 |
> | Continuous | $111,277.05 |
>
> Difference (continuous − annual) ≈ **$3,330.80**  
> Limiting EAR = $e^{0.08} - 1 = 8.3287\%$

---

## Problem 2: The Breakeven Investment

**Setup:** Option A pays \$25,000 today. Option B pays \$32,000 in 4 years. Continuous compounding.

### Part (a): Breakeven Continuously Compounded Rate

At breakeven, the present value of Option B equals Option A:

$$25{,}000 = 32{,}000 \cdot e^{-r \cdot 4}$$

Solve for $r$:

$$e^{-4r} = \frac{25{,}000}{32{,}000} = 0.78125$$

$$-4r = \ln(0.78125) = -0.24686$$

$$r = \frac{0.24686}{4} = \boxed{0.06172 = 6.172\%}$$

**Interpretation:** If your discount rate is below 6.172%, Option B (wait for \$32k) is better. Above 6.172%, take the \$25k now.

---

### Part (b): Which Option at $r = 7\%$?

$$PV_B = 32{,}000 \cdot e^{-0.07 \times 4} = 32{,}000 \cdot e^{-0.28}$$

Compute $e^{-0.28}$:

$$e^{-0.28} = \frac{1}{e^{0.28}} = \frac{1}{1.32313} = 0.75578$$

$$PV_B = 32{,}000 \times 0.75578 = \$24{,}185.09$$

Since $PV_B = \$24{,}185.09 < \$25{,}000 = PV_A$:

$$\boxed{\text{Option A is better at } r = 7\%}$$

This makes sense: 7% > 6.172% (breakeven), so we prefer the money now.

---

### Part (c): Annuity Version — \$8,000 Per Year for 4 Years at 7%

$$PV = \sum_{k=1}^{4} 8{,}000 \cdot e^{-0.07k}$$

Compute each term:

| $k$ | $e^{-0.07k}$ | $8{,}000 \times e^{-0.07k}$ |
|-----|-------------|---------------------------|
| 1 | $e^{-0.07} = 0.93239$ | $7{,}459.12$ |
| 2 | $e^{-0.14} = 0.86936$ | $6{,}954.88$ |
| 3 | $e^{-0.21} = 0.81058$ | $6{,}484.66$ |
| 4 | $e^{-0.28} = 0.75578$ | $6{,}046.27$ |

$$PV = 7{,}459.12 + 6{,}954.88 + 6{,}484.66 + 6{,}046.27 = \boxed{\$26{,}944.93}$$

Since $\$26{,}944.93 > \$25{,}000$, the annuity version (four payments of \$8,000) is **better** than Option A at $r = 7\%$ — even though the single \$32,000 lump sum was not!

The reason is that the annuity delivers cash earlier, reducing the discounting penalty.

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 2: The Breakeven Investment")
print("=" * 55)

# Part (a)
r_breakeven = np.log(32000 / 25000) / 4
print(f"  (a) Breakeven rate: r = {r_breakeven:.6f} = {r_breakeven*100:.4f}%")

# Part (b)
r = 0.07
pv_b = 32000 * np.exp(-r * 4)
print(f"  (b) PV of Option B at 7%: ${pv_b:,.4f}")
print(f"      Option A ($25,000) is {'better' if 25000 > pv_b else 'worse'}")

# Part (c)
pv_annuity = sum(8000 * np.exp(-r * k) for k in range(1, 5))
print(f"  (c) PV of annuity: ${pv_annuity:,.4f}")
print(f"      Annuity is {'better' if pv_annuity > 25000 else 'worse'} than Option A")
for k in range(1, 5):
    term = 8000 * np.exp(-r * k)
    print(f"        k={k}: 8000 × e^(-{r*k:.2f}) = ${term:,.4f}")
```

---

> **Answer Summary — Problem 2**
>
> (a) Breakeven rate: $r = \ln(1.28)/4 = 6.172\%$  
> (b) At 7%: $PV_B = \$24{,}185.09 < \$25{,}000$ → **Option A wins**  
> (c) Annuity PV = $\$26{,}944.93 > \$25{,}000$ → **Annuity wins** (earlier cash flows help)

---

## Problem 3: Zero-Coupon Bond Pricing

**Setup:** Three zero-coupon bonds, all with face value $F = \$1{,}000$:

| Bond | Price $P$ | Maturity $T$ |
|------|-----------|-------------|
| A | \$925 | 2 years |
| B | \$780 | 5 years |
| C | \$550 | 10 years |

### Part (a): Annual Compounding Yield

For a zero-coupon bond under annual compounding:

$$P = \frac{F}{(1+y)^T} \quad \Rightarrow \quad y = \left(\frac{F}{P}\right)^{1/T} - 1$$

**Bond A:**

$$y_A = \left(\frac{1000}{925}\right)^{1/2} - 1 = (1.08108)^{0.5} - 1$$

$$\sqrt{1.08108} = 1.03975$$

$$\boxed{y_A = 3.975\%}$$

**Bond B:**

$$y_B = \left(\frac{1000}{780}\right)^{1/5} - 1 = (1.28205)^{0.2} - 1$$

$\ln(1.28205) = 0.24846$, so $(1.28205)^{0.2} = e^{0.24846/5} = e^{0.04969} = 1.05095$

$$\boxed{y_B = 5.095\%}$$

**Bond C:**

$$y_C = \left(\frac{1000}{550}\right)^{1/10} - 1 = (1.81818)^{0.1} - 1$$

$\ln(1.81818) = 0.59784$, so $(1.81818)^{0.1} = e^{0.05978} = 1.06161$

$$\boxed{y_C = 6.161\%}$$

---

### Part (b): Continuous Compounding Yield

$$P = F \cdot e^{-r \cdot T} \quad \Rightarrow \quad r = \frac{\ln(F/P)}{T}$$

**Bond A:**

$$r_A = \frac{\ln(1000/925)}{2} = \frac{\ln(1.08108)}{2} = \frac{0.07796}{2} = \boxed{3.898\%}$$

**Bond B:**

$$r_B = \frac{\ln(1000/780)}{5} = \frac{0.24846}{5} = \boxed{4.969\%}$$

**Bond C:**

$$r_C = \frac{\ln(1000/550)}{10} = \frac{0.59784}{10} = \boxed{5.978\%}$$

---

### Part (c): Term Structure Shape

| Maturity | Annual Yield | Continuous Yield |
|----------|-------------|-----------------|
| 2 yr | 3.975% | 3.898% |
| 5 yr | 5.095% | 4.969% |
| 10 yr | 6.161% | 5.978% |

The yield curve is **upward-sloping (normal)**. Yields increase with maturity.

**Explanation:** This reflects two factors:
1. **Expectations Hypothesis:** The market expects future short-term rates to be higher than current short rates.
2. **Term Premium:** Investors demand extra compensation for holding longer-maturity bonds due to greater interest rate risk exposure and uncertainty.

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 3: Zero-Coupon Bond Pricing")
print("=" * 55)

F = 1000
bonds = [('A', 925, 2), ('B', 780, 5), ('C', 550, 10)]

print("\n  Part (a) & (b): Yields")
print(f"  {'Bond':<6} {'P':>6} {'T':>4} {'y_annual':>10} {'r_cont':>10}")
print("  " + "-" * 40)
for name, P, T in bonds:
    y_annual = (F / P) ** (1 / T) - 1
    r_cont = np.log(F / P) / T
    print(f"  {name:<6} {P:>6.0f} {T:>4d} {y_annual:>10.4%} {r_cont:>10.4%}")

print("\n  Part (c): Yields increase with maturity → NORMAL (upward-sloping) curve")
```

---

> **Answer Summary — Problem 3**
>
> | Bond | $y_{\text{annual}}$ | $r_{\text{continuous}}$ |
> |------|--------------------|-----------------------|
> | A (2yr) | 3.975% | 3.898% |
> | B (5yr) | 5.095% | 4.969% |
> | C (10yr) | 6.161% | 5.978% |
>
> Term structure: **Normal (upward-sloping)** — longer maturities demand higher yields.

---

## Problem 4: Coupon Bond Pricing & YTM

**Setup:** 5-year bond, $F = \$1{,}000$, 6% annual coupon paid **semi-annually**.

- Coupon per period: $C = 0.06 \times 1000 / 2 = \$30$
- Number of periods: $n = 5 \times 2 = 10$
- Market price: $P = \$965$

### Part (a): Cash Flow Schedule

| Period $k$ | Time (years) | Cash Flow |
|-----------|-------------|-----------|
| 1 | 0.5 | \$30 |
| 2 | 1.0 | \$30 |
| 3 | 1.5 | \$30 |
| 4 | 2.0 | \$30 |
| 5 | 2.5 | \$30 |
| 6 | 3.0 | \$30 |
| 7 | 3.5 | \$30 |
| 8 | 4.0 | \$30 |
| 9 | 4.5 | \$30 |
| 10 | 5.0 | \$30 + \$1,000 = **\$1,030** |

---

### Part (b): Pricing Formula

Let $y$ be the annual YTM, so the semi-annual yield is $y_s = y/2$.

$$P = \sum_{k=1}^{9} \frac{30}{(1+y_s)^k} + \frac{1{,}030}{(1+y_s)^{10}} = 965$$

Using the annuity formula:

$$P = 30 \times \frac{1 - (1+y_s)^{-10}}{y_s} + 1{,}000 \times (1+y_s)^{-10} = 965$$

---

### Part (c): Solve for YTM Numerically

**Trial at $y_s = 0.034$ ($y = 6.80\%$):**

$(1.034)^{10} = 1.39736$, so DF $= 1/1.39736 = 0.71564$

$P = 30 \times \frac{1 - 0.71564}{0.034} + 1000 \times 0.71564 = 30 \times 8.3635 + 715.64 = 250.91 + 715.64 = 966.54$

**Trial at $y_s = 0.035$ ($y = 7.00\%$):**

$(1.035)^{10} = 1.41060$, so DF $= 0.70892$

$P = 30 \times \frac{1 - 0.70892}{0.035} + 1000 \times 0.70892 = 30 \times 8.3166 + 708.92 = 249.50 + 708.92 = 958.42$

**Linear Interpolation:**

$$y_s = 0.034 + \frac{966.54 - 965}{966.54 - 958.42} \times 0.001 = 0.034 + \frac{1.54}{8.12} \times 0.001 = 0.034 + 0.000190 = 0.034190$$

$$\boxed{y \approx 2 \times 0.034190 = 6.838\%}$$

(Exact numerical solution via `scipy.optimize.brentq` below gives $y \approx 6.8388\%$.)

---

### Part (d): Price at $y_{\text{new}} = y - 0.01$

With $y_{\text{new}} \approx 5.8388\%$, so $y_s = 0.029194$:

$$(1.029194)^{10} = e^{10 \ln(1.029194)} = e^{10 \times 0.028775} = e^{0.28775} = 1.33346$$

$$\text{DF} = 1/1.33346 = 0.74993$$

$$P_{\text{new}} = 30 \times \frac{1 - 0.74993}{0.029194} + 1000 \times 0.74993 = 30 \times 8.5634 + 749.93 = 256.90 + 749.93 = \boxed{\$1{,}006.83}$$

A 100 bps drop in yield increases the price from \$965 to about \$1,007 — a gain of roughly **\$41.83** (4.33%).

---

### Python Verification

```python
import numpy as np
from scipy.optimize import brentq

print("=" * 55)
print("Problem 4: Coupon Bond Pricing & YTM")
print("=" * 55)

F, C, n, P_market = 1000, 30, 10, 965

# Part (a): Cash flows
print("\n  Part (a): Cash flows")
for k in range(1, n + 1):
    cf = C if k < n else C + F
    print(f"    Period {k:2d} (t={k*0.5:.1f}yr): ${cf:,.0f}")

# Part (c): Solve for YTM
def bond_price(y_s):
    return sum(C / (1 + y_s)**k for k in range(1, n)) + (C + F) / (1 + y_s)**n

def obj(y_s):
    return bond_price(y_s) - P_market

y_s_solution = brentq(obj, 0.001, 0.5)
ytm = 2 * y_s_solution
print(f"\n  Part (c): YTM = {ytm:.6f} = {ytm*100:.4f}%")
print(f"    Semi-annual yield = {y_s_solution:.6f}")
print(f"    Verification: P(YTM) = ${bond_price(y_s_solution):,.4f}")

# Part (d): Price at YTM - 100 bps
y_new = ytm - 0.01
y_s_new = y_new / 2
p_new = bond_price(y_s_new)
print(f"\n  Part (d): New yield = {y_new*100:.4f}%")
print(f"    New price = ${p_new:,.4f}")
print(f"    Price change = ${p_new - P_market:,.4f} ({(p_new - P_market)/P_market*100:+.4f}%)")
```

---

> **Answer Summary — Problem 4**
>
> (a) 10 semi-annual coupons of \$30; final payment includes \$1,000 principal.  
> (b) Pricing formula: $P = 30 \cdot \frac{1-(1+y/2)^{-10}}{y/2} + 1000 \cdot (1+y/2)^{-10}$  
> (c) **YTM ≈ 6.84%** (semi-annual yield ≈ 3.42%)  
> (d) Price at (YTM − 100 bps) ≈ **\$1,006.83**

---

## Problem 5: Bootstrapping Spot Rates

**Setup:** Four par bonds (price = 100) with annual coupons:

| Maturity | Coupon Rate |
|----------|------------|
| 1 year | 3.00% |
| 2 year | 3.50% |
| 3 year | 4.00% |
| 4 year | 4.25% |

### Part (a): Bootstrap Spot Rates

**1-Year Spot Rate $r_1$:**

$$100 = \frac{103}{1 + r_1} \quad \Rightarrow \quad 1 + r_1 = 1.03 \quad \Rightarrow \quad \boxed{r_1 = 3.0000\%}$$

---

**2-Year Spot Rate $r_2$:**

$$100 = \frac{3.5}{1 + r_1} + \frac{103.5}{(1 + r_2)^2}$$

$$100 = \frac{3.5}{1.03} + \frac{103.5}{(1 + r_2)^2}$$

$$100 = 3.39806 + \frac{103.5}{(1 + r_2)^2}$$

$$\frac{103.5}{(1 + r_2)^2} = 96.60194$$

$$(1 + r_2)^2 = \frac{103.5}{96.60194} = 1.07143$$

$$1 + r_2 = \sqrt{1.07143} = 1.03509$$

$$\boxed{r_2 = 3.5088\%}$$

---

**3-Year Spot Rate $r_3$:**

$$100 = \frac{4}{1.03} + \frac{4}{(1.03509)^2} + \frac{104}{(1 + r_3)^3}$$

$$= 3.88350 + \frac{4}{1.07143} + \frac{104}{(1 + r_3)^3}$$

$$= 3.88350 + 3.73333 + \frac{104}{(1 + r_3)^3}$$

$$= 7.61683 + \frac{104}{(1 + r_3)^3}$$

$$\frac{104}{(1 + r_3)^3} = 92.38317$$

$$(1 + r_3)^3 = \frac{104}{92.38317} = 1.12576$$

$$1 + r_3 = (1.12576)^{1/3} = e^{\ln(1.12576)/3} = e^{0.11862/3} = e^{0.03954} = 1.04033$$

$$\boxed{r_3 = 4.0330\%}$$

---

**4-Year Spot Rate $r_4$:**

$$100 = \frac{4.25}{1.03} + \frac{4.25}{(1.03509)^2} + \frac{4.25}{(1.04033)^3} + \frac{104.25}{(1 + r_4)^4}$$

Compute each PV:

$$\frac{4.25}{1.03} = 4.12621$$

$$\frac{4.25}{1.07143} = 3.96651$$

$$\frac{4.25}{1.12576} = 3.77484$$

$$\text{Sum} = 4.12621 + 3.96651 + 3.77484 = 11.86756$$

$$\frac{104.25}{(1 + r_4)^4} = 100 - 11.86756 = 88.13244$$

$$(1 + r_4)^4 = \frac{104.25}{88.13244} = 1.18287$$

$$1 + r_4 = (1.18287)^{1/4} = e^{\ln(1.18287)/4} = e^{0.16803/4} = e^{0.04201} = 1.04290$$

$$\boxed{r_4 = 4.2902\%}$$

---

### Part (b): Continuous Spot Rates

$$r_{\text{cont}} = \ln(1 + r_{\text{annual}})$$

| Maturity | $r_{\text{annual}}$ | $r_{\text{cont}} = \ln(1+r)$ |
|----------|--------------------|-----------------------------|
| 1 year | 3.0000% | $\ln(1.03) = 2.9559\%$ |
| 2 year | 3.5088% | $\ln(1.03509) = 3.4482\%$ |
| 3 year | 4.0330% | $\ln(1.04033) = 3.9533\%$ |
| 4 year | 4.2902% | $\ln(1.04290) = 4.1997\%$ |

---

### Part (c): Discount Factors

$$d(t) = \frac{1}{(1 + r(t))^t}$$

| $t$ | $r(t)$ | $d(t) = 1/(1+r)^t$ |
|-----|--------|---------------------|
| 1 | 3.0000% | $1/1.03 = 0.97087$ |
| 2 | 3.5088% | $1/1.07143 = 0.93333$ |
| 3 | 4.0330% | $1/1.12576 = 0.88826$ |
| 4 | 4.2902% | $1/1.18287 = 0.84544$ |

---

### Part (d): Price a 5% Annual Coupon 4-Year Bond

$$P = 5 \cdot d(1) + 5 \cdot d(2) + 5 \cdot d(3) + 105 \cdot d(4)$$

$$= 5(0.97087) + 5(0.93333) + 5(0.88826) + 105(0.84544)$$

$$= 4.85437 + 4.66667 + 4.44131 + 88.77136$$

$$= \boxed{\$102.7337}$$

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 5: Bootstrapping Spot Rates")
print("=" * 55)

coupons = [0.03, 0.035, 0.04, 0.0425]
spot_rates = []

for T, c in enumerate(coupons, start=1):
    # Cash flows: c*100 at each t, plus 100 at T
    pv_previous = sum(c * 100 / (1 + spot_rates[k])**(k+1) for k in range(T - 1))
    remaining = 100 - pv_previous  # PV of final cash flow
    final_cf = (1 + c) * 100
    r_T = (final_cf / remaining) ** (1 / T) - 1
    spot_rates.append(r_T)

print("\n  Part (a): Bootstrapped spot rates")
for i, r in enumerate(spot_rates):
    print(f"    r_{i+1} = {r:.6f} = {r*100:.4f}%")

# Part (b): Continuous rates
print("\n  Part (b): Continuous spot rates")
for i, r in enumerate(spot_rates):
    r_cont = np.log(1 + r)
    print(f"    r_{i+1}_cont = {r_cont:.6f} = {r_cont*100:.4f}%")

# Part (c): Discount factors
print("\n  Part (c): Discount factors")
d = []
for i, r in enumerate(spot_rates):
    df = 1 / (1 + r) ** (i + 1)
    d.append(df)
    print(f"    d({i+1}) = {df:.6f}")

# Part (d): Price 5% coupon bond
coupon_new = 5
price = sum(coupon_new * d[i] for i in range(4)) + 100 * d[3]
print(f"\n  Part (d): Price of 5% bond = ${price:,.4f}")
```

---

> **Answer Summary — Problem 5**
>
> | $t$ | $r(t)$ (annual) | $r(t)$ (continuous) | $d(t)$ |
> |-----|----------------|--------------------|----|
> | 1 | 3.0000% | 2.9559% | 0.97087 |
> | 2 | 3.5088% | 3.4482% | 0.93333 |
> | 3 | 4.0330% | 3.9533% | 0.88826 |
> | 4 | 4.2902% | 4.1997% | 0.84544 |
>
> Price of 5% 4-year bond = **\$102.73**

---

## Problem 6: Conceptual Challenge

### Part (a): YTM vs. Spot Rates

**Yield to Maturity (YTM)** is a *single* discount rate applied uniformly to *all* cash flows of a bond. It is the internal rate of return that equates the bond's price to the present value of its cash flows:

$$P = \sum_{k=1}^{n} \frac{CF_k}{(1 + y)^{t_k}}$$

**Spot rates** $r(t)$ are maturity-specific discount rates — each cash flow is discounted at the rate appropriate for its specific time horizon:

$$P = \sum_{k=1}^{n} \frac{CF_k}{(1 + r(t_k))^{t_k}}$$

**When would they be equal?**

1. **For a zero-coupon bond:** There is only one cash flow, so YTM = $r(T)$ exactly.
2. **When the yield curve is flat:** If $r(t) = r$ for all $t$, then YTM $= r$ for every bond.

---

### Part (b): Can We Use a Single Spot Rate for a Coupon Bond?

**Given:** Bond X is a 3-year zero-coupon bond priced at \$88.90 ($F = 100$).

$$r_3 = \left(\frac{100}{88.90}\right)^{1/3} - 1 = (1.12486)^{1/3} - 1$$

$\ln(1.12486)/3 = 0.11765/3 = 0.03922$

$$r_3 = e^{0.03922} - 1 = 0.04000 = \boxed{4.000\%}$$

**Can we use $r_3$ alone to price Bond Y (a 3-year coupon bond)?**

**No!** Bond Y has cash flows at $t = 1, 2, 3$. Each cash flow should be discounted at its own spot rate:
- The $t=1$ cash flow uses $r_1$
- The $t=2$ cash flow uses $r_2$
- The $t=3$ cash flow uses $r_3$

Using $r_3$ for all three would systematically misprice the bond. Only if the yield curve were perfectly flat (all spot rates equal to $r_3$) would this give the correct price.

---

### Part (c): YTM vs. Longest Spot Rate for a Coupon Bond

For a coupon bond in a normal (upward-sloping) yield curve environment, the **YTM will be lower than the longest-maturity spot rate** used.

**Why?** YTM is a *weighted average* of the spot rates, where the weights are the present values of each cash flow. The early coupon payments (at $t = 1, 2, \ldots$) are discounted at *lower* spot rates. These coupons "pull" the weighted average (YTM) down below $r_n$, the spot rate for the final maturity.

Mathematically, if $r_1 < r_2 < \cdots < r_n$, then:

$$r_1 < \text{YTM} < r_n$$

The YTM sits between the lowest and highest spot rates, closer to the highest because the final cash flow (principal + coupon) dominates.

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 6: Conceptual Challenge")
print("=" * 55)

# Part (b): 3-year ZCB yield
P_x, F_x, T_x = 88.90, 100, 3
r3 = (F_x / P_x) ** (1 / T_x) - 1
print(f"\n  Part (b): r_3 from Bond X = {r3:.6f} = {r3*100:.4f}%")

# Demonstration: mispricing a coupon bond with a single spot rate
# Suppose true spot rates
r1, r2 = 0.02, 0.03  # hypothetical
coupon = 5
cf = [coupon, coupon, coupon + 100]

# Correct pricing
p_correct = cf[0]/(1+r1) + cf[1]/(1+r2)**2 + cf[2]/(1+r3)**3
# Wrong pricing (using r3 for all)
p_wrong = sum(c / (1+r3)**(k+1) for k, c in enumerate(cf))

print(f"  Correct price (using r1={r1}, r2={r2}, r3={r3:.4f}): ${p_correct:.4f}")
print(f"  Wrong price (using r3 for all): ${p_wrong:.4f}")
print(f"  Error: ${abs(p_correct - p_wrong):.4f}")

# Part (c): Demonstrate YTM < longest spot rate
from scipy.optimize import brentq
spot_rates = [0.03, 0.035, 0.04]  # upward-sloping
coupon_rate = 0.05
cf = [coupon_rate*100, coupon_rate*100, (coupon_rate+1)*100]
P = sum(cf[k] / (1+spot_rates[k])**(k+1) for k in range(3))

ytm = brentq(lambda y: sum(cf[k]/(1+y)**(k+1) for k in range(3)) - P, 0.001, 0.5)
print(f"\n  Part (c): Spot rates = {[f'{r:.1%}' for r in spot_rates]}")
print(f"    Bond price = ${P:.4f}")
print(f"    YTM = {ytm:.4%}")
print(f"    Longest spot rate = {spot_rates[-1]:.4%}")
print(f"    YTM < r_3? {ytm < spot_rates[-1]}")
```

---

> **Answer Summary — Problem 6**
>
> (a) YTM = single flat rate; spot rates = maturity-specific. Equal for ZCBs or flat curves.  
> (b) $r_3 = 4.00\%$ from Bond X. Cannot use it alone for coupon bonds — need $r_1, r_2, r_3$.  
> (c) YTM < longest spot rate in an upward-sloping curve because early coupons pull the weighted average down.

---

## Problem 7: Duration Deep Dive

**Setup:** 4-year bond, 5% annual coupon, $F = \$1{,}000$, YTM = 6%.

Cash flows: $CF_1 = CF_2 = CF_3 = \$50$, $CF_4 = \$1{,}050$.

### Price Calculation

$$P = \frac{50}{1.06} + \frac{50}{(1.06)^2} + \frac{50}{(1.06)^3} + \frac{1050}{(1.06)^4}$$

Discount factors:

$$(1.06)^1 = 1.06, \quad (1.06)^2 = 1.1236, \quad (1.06)^3 = 1.191016, \quad (1.06)^4 = 1.262477$$

$$P = \frac{50}{1.06} + \frac{50}{1.1236} + \frac{50}{1.191016} + \frac{1050}{1.262477}$$

$$= 47.1698 + 44.4998 + 41.9810 + 831.8366$$

$$\boxed{P = \$965.4872}$$

Since $P < \$1{,}000$, the bond trades at a **discount** (coupon rate 5% < YTM 6%).

---

### Part (a): Macaulay Duration

$$D_{\text{mac}} = \frac{1}{P} \sum_{t=1}^{n} t \cdot PV(CF_t) = \sum_{t=1}^{n} t \cdot w_t$$

where $w_t = PV(CF_t) / P$ is the weight of each cash flow.

| $t$ | $CF_t$ | $DF = (1.06)^{-t}$ | $PV(CF_t)$ | $w_t = PV/P$ | $t \times w_t$ |
|-----|--------|---------------------|-----------|---------------|----------------|
| 1 | 50 | 0.943396 | 47.1698 | 0.048856 | 0.048856 |
| 2 | 50 | 0.889996 | 44.4998 | 0.046091 | 0.092183 |
| 3 | 50 | 0.839619 | 41.9810 | 0.043482 | 0.130447 |
| 4 | 1050 | 0.792094 | 831.8366 | 0.861570 | 3.446281 |
| **Σ** | | | **965.4872** | **1.000000** | **3.717767** |

$$\boxed{D_{\text{mac}} = 3.7178 \text{ years}}$$

**Interpretation:** The weighted-average time to receive the bond's cash flows is 3.72 years. Even though the bond matures in 4 years, the coupons pull the average closer to today.

---

### Part (b): Modified Duration

$$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + y/m} = \frac{3.7178}{1.06} = \boxed{3.5073 \text{ years}}$$

(Here $m = 1$ for annual compounding.)

---

### Part (c): Estimated % Price Change for +50 bps

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \times \Delta y = -3.5073 \times 0.005 = \boxed{-1.7537\%}$$

The bond price is expected to **decrease by about 1.75%** for a 50 basis point increase in yield.

---

### Part (d): Dollar Impact on \$10M Face Value Portfolio

**Portfolio market value:**

$$V = \frac{P}{1000} \times 10{,}000{,}000 = \frac{965.4872}{1000} \times 10{,}000{,}000 = \$9{,}654{,}872$$

**Dollar duration** (DV01 for a 1% move):

$$\text{Dollar Duration} = D_{\text{mod}} \times V = 3.5073 \times 9{,}654{,}872 = \$33{,}864{,}818 \text{ per 100\% change}$$

**Dollar change for +50 bps:**

$$\Delta V = -D_{\text{mod}} \times \Delta y \times V = -3.5073 \times 0.005 \times 9{,}654{,}872 = \boxed{-\$169{,}324}$$

---

### Part (e): Why Is Duration Less Than Maturity?

A coupon bond's Macaulay duration is **always less than its maturity** (unless it's a zero-coupon bond, where they are equal).

**Reason:** Coupons deliver cash *before* maturity. Each coupon payment at $t < T$ has weight $w_t > 0$, which pulls the weighted average time toward the present. The larger the coupon rate relative to yield, the more the duration shrinks below maturity.

For a **zero-coupon bond**, there is only one cash flow at maturity, so $D_{\text{mac}} = T$ exactly.

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 7: Duration Deep Dive")
print("=" * 55)

F, c, n, y = 1000, 0.05, 4, 0.06
cfs = [c * F] * (n - 1) + [(c + 1) * F]
times = np.arange(1, n + 1)

# Price
pvs = np.array([cfs[i] / (1 + y)**t for i, t in enumerate(times)])
P = pvs.sum()
print(f"\n  Price = ${P:,.4f}")

# Part (a): Macaulay Duration
weights = pvs / P
D_mac = np.sum(times * weights)
print(f"\n  Part (a): Macaulay Duration")
print(f"  {'t':>3} {'CF':>8} {'DF':>10} {'PV(CF)':>12} {'w_t':>10} {'t×w_t':>10}")
print("  " + "-" * 56)
for i in range(n):
    df = 1 / (1 + y)**times[i]
    print(f"  {times[i]:3.0f} {cfs[i]:8.0f} {df:10.6f} {pvs[i]:12.4f} {weights[i]:10.6f} {times[i]*weights[i]:10.6f}")
print(f"  {'Σ':>3} {'':>8} {'':>10} {P:12.4f} {weights.sum():10.6f} {D_mac:10.6f}")
print(f"\n  D_mac = {D_mac:.4f} years")

# Part (b): Modified Duration
D_mod = D_mac / (1 + y)
print(f"\n  Part (b): D_mod = {D_mac:.4f} / {1+y:.2f} = {D_mod:.4f} years")

# Part (c): % price change for +50 bps
delta_y = 0.005
pct_change = -D_mod * delta_y
print(f"\n  Part (c): ΔP/P ≈ -{D_mod:.4f} × {delta_y} = {pct_change:.6f} = {pct_change*100:.4f}%")

# Part (d): Dollar impact
face_portfolio = 10_000_000
mv = P / F * face_portfolio
dollar_change = pct_change * mv
print(f"\n  Part (d): Portfolio MV = ${mv:,.2f}")
print(f"    Dollar change = ${dollar_change:,.2f}")

# Part (e)
print(f"\n  Part (e): D_mac ({D_mac:.2f}) < Maturity ({n}) because coupons deliver cash early")
```

---

> **Answer Summary — Problem 7**
>
> | Metric | Value |
> |--------|-------|
> | Bond Price | $965.49 |
> | Macaulay Duration | 3.7178 years |
> | Modified Duration | 3.5073 years |
> | ΔP/P for +50 bps | −1.7537% |
> | Dollar ΔP on $10M face | −$169,324 |

---

## Problem 8: Convexity and Taylor Correction

**Setup:** Same bond as Problem 7 — 4-year, 5% annual coupon, $F = \$1{,}000$, YTM = 6%.

From Problem 7: $P = \$965.4872$, $D_{\text{mod}} = 3.5073$.

### Part (a): Convexity Calculation

For annual compounding ($m = 1$):

$$C = \frac{1}{P \cdot (1+y)^2} \sum_{k=1}^{n} k(k+1) \cdot \frac{CF_k}{(1+y)^k}$$

The denominator's leading factor:

$$P \cdot (1+y)^2 = 965.4872 \times (1.06)^2 = 965.4872 \times 1.1236 = 1085.0116$$

Now compute each term $k(k+1) \cdot CF_k / (1+y)^k$:

| $k$ | $CF_k$ | $k(k+1)$ | $(1.06)^{-k}$ | $CF_k/(1.06)^k$ | $k(k+1) \times CF_k/(1.06)^k$ |
|-----|--------|---------|--------------|------------------|-------------------------------|
| 1 | 50 | 2 | 0.943396 | 47.1698 | 94.3396 |
| 2 | 50 | 6 | 0.889996 | 44.4998 | 266.9989 |
| 3 | 50 | 12 | 0.839619 | 41.9810 | 503.7716 |
| 4 | 1050 | 20 | 0.792094 | 831.8366 | 16,636.7326 |
| **Σ** | | | | | **17,501.8427** |

$$C = \frac{17{,}501.8427}{1{,}085.0116} = \boxed{16.1306}$$

---

### Part (b): Price Sensitivity for +200 bps ($\Delta y = +0.02$)

**(i) Duration-Only Approximation:**

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \times \Delta y = -3.5073 \times 0.02 = \boxed{-7.0147\%}$$

$$\Delta P \approx -7.0147\% \times 965.4872 = -\$67.74$$

**(ii) Duration + Convexity (Taylor 2nd Order):**

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \times \Delta y + \frac{1}{2} C \times (\Delta y)^2$$

$$= -3.5073 \times 0.02 + \frac{1}{2} \times 16.1306 \times (0.02)^2$$

$$= -0.070147 + 0.5 \times 16.1306 \times 0.0004$$

$$= -0.070147 + 0.003226$$

$$= \boxed{-6.6920\%}$$

$$\Delta P \approx -6.6920\% \times 965.4872 = -\$64.62$$

---

### Part (c): Exact Price at YTM = 8% (Verify Approximation)

$$P_{\text{new}} = \frac{50}{1.08} + \frac{50}{(1.08)^2} + \frac{50}{(1.08)^3} + \frac{1050}{(1.08)^4}$$

$$(1.08)^1 = 1.08, \quad (1.08)^2 = 1.1664, \quad (1.08)^3 = 1.259712, \quad (1.08)^4 = 1.360489$$

$$P_{\text{new}} = 46.2963 + 42.8669 + 39.6916 + 771.6356 = \$900.4904$$

**Actual percentage change:**

$$\frac{\Delta P}{P} = \frac{900.4904 - 965.4872}{965.4872} = \frac{-64.9968}{965.4872} = -6.7320\%$$

**Comparison of estimates:**

| Method | Estimated $\Delta P/P$ | Error |
|--------|----------------------|-------|
| Duration only | −7.0147% | 0.2826% |
| Duration + Convexity | −6.6920% | 0.0400% |
| **Exact** | **−6.7320%** | — |

The convexity correction dramatically improves accuracy — reducing the error from 0.28% to 0.04%.

---

### Part (d): Repeat for YTM = 4% ($\Delta y = -0.02$), Show Asymmetry

**Exact price at YTM = 4%:**

$$P_{\text{new}} = \frac{50}{1.04} + \frac{50}{(1.04)^2} + \frac{50}{(1.04)^3} + \frac{1050}{(1.04)^4}$$

$$(1.04)^1 = 1.04, \quad (1.04)^2 = 1.0816, \quad (1.04)^3 = 1.124864, \quad (1.04)^4 = 1.169859$$

$$P_{\text{new}} = 48.0769 + 46.2278 + 44.4498 + 897.2376 = \$1{,}035.9921$$

**Actual change:**

$$\frac{\Delta P}{P} = \frac{1035.9921 - 965.4872}{965.4872} = \frac{70.5049}{965.4872} = +7.3025\%$$

**Duration-only estimate** ($\Delta y = -0.02$):

$$\frac{\Delta P}{P} \approx -D_{\text{mod}} \times (-0.02) = +7.0147\%$$

**Duration + Convexity estimate:**

$$\frac{\Delta P}{P} \approx +7.0147\% + 0.5 \times 16.1306 \times 0.0004 = +7.0147\% + 0.3226\% = +7.3373\%$$

**Asymmetry Summary:**

| | $\Delta y = +200$ bps | $\Delta y = -200$ bps |
|---|---|---|
| Exact $\Delta P/P$ | −6.7320% | +7.3025% |
| Duration only | −7.0147% | +7.0147% |
| Duration + Convexity | −6.6920% | +7.3373% |

**Key insight:** The price *gains more* when yields fall than it *loses* when yields rise by the same amount. This asymmetry is the **convexity benefit** — all else equal, investors prefer bonds with higher convexity.

---

### Python Verification

```python
import numpy as np

print("=" * 55)
print("Problem 8: Convexity and Taylor Correction")
print("=" * 55)

F, c, n, y = 1000, 0.05, 4, 0.06
cfs = [c * F] * (n - 1) + [(c + 1) * F]
times = np.arange(1, n + 1)

# Price and duration from Problem 7
pvs = np.array([cfs[i] / (1 + y)**t for i, t in enumerate(times)])
P = pvs.sum()
weights = pvs / P
D_mac = np.sum(times * weights)
D_mod = D_mac / (1 + y)

# Part (a): Convexity
conv_terms = np.array([times[i] * (times[i] + 1) * cfs[i] / (1 + y)**times[i]
                        for i in range(n)])
convexity = conv_terms.sum() / (P * (1 + y)**2)

print(f"\n  Price = ${P:,.4f}")
print(f"  D_mac = {D_mac:.4f}, D_mod = {D_mod:.4f}")
print(f"\n  Part (a): Convexity")
print(f"  {'k':>3} {'CF':>8} {'k(k+1)':>8} {'PV(CF)':>12} {'k(k+1)·PV(CF)':>16}")
print("  " + "-" * 52)
for i in range(n):
    pv = cfs[i] / (1 + y)**times[i]
    kk1 = times[i] * (times[i] + 1)
    print(f"  {times[i]:3.0f} {cfs[i]:8.0f} {kk1:8.0f} {pv:12.4f} {kk1*pv:16.4f}")
print(f"  Σ of k(k+1)·PV(CF) = {conv_terms.sum():,.4f}")
print(f"  Convexity = {convexity:.4f}")

# Parts (b)-(d): Taylor estimates vs exact
for delta_y, label in [(0.02, "+200 bps (YTM→8%)"), (-0.02, "-200 bps (YTM→4%)")]:
    dur_est = -D_mod * delta_y
    conv_est = dur_est + 0.5 * convexity * delta_y**2
    P_exact = sum(cfs[i] / (1 + y + delta_y)**times[i] for i in range(n))
    actual = (P_exact - P) / P

    print(f"\n  {label}:")
    print(f"    Duration only:     ΔP/P = {dur_est:+.6f} = {dur_est*100:+.4f}%")
    print(f"    Duration+Convex:   ΔP/P = {conv_est:+.6f} = {conv_est*100:+.4f}%")
    print(f"    Exact:             ΔP/P = {actual:+.6f} = {actual*100:+.4f}%")
    print(f"    Exact new price:   ${P_exact:,.4f}")
    print(f"    Duration error:    {abs(dur_est - actual)*100:.4f}%")
    print(f"    Convexity error:   {abs(conv_est - actual)*100:.4f}%")
```

---

> **Answer Summary — Problem 8**
>
> Convexity $C = 16.1306$
>
> | Scenario | Duration Only | Dur + Convexity | Exact |
> |---|---|---|---|
> | +200 bps | −7.015% | −6.692% | −6.732% |
> | −200 bps | +7.015% | +7.337% | +7.303% |
>
> Convexity correction reduces approximation error by ~7×.  
> Price gains from rate drops exceed price losses from equal rate rises → **convexity benefit**.

---

## Problem 9: Full Pipeline

**Setup:** Five bonds with observed market prices, all with $F = 100$ and annual coupons.

| Bond | Maturity | Coupon | Price |
|------|----------|--------|-------|
| 1 | 1 yr | 0% (ZCB) | 97.09 |
| 2 | 2 yr | 4% | 100.95 |
| 3 | 3 yr | 5% | 102.78 |
| 4 | 4 yr | 5.5% | 103.43 |
| 5 | 5 yr | 6% | 105.01 |

### Part (a): Bootstrap Spot Rates

**$r_1$ from Bond 1 (ZCB):**

$$97.09 = \frac{100}{1 + r_1} \quad \Rightarrow \quad 1 + r_1 = \frac{100}{97.09} = 1.02997$$

$$\boxed{r_1 = 2.9972\%}$$

---

**$r_2$ from Bond 2:**

$$100.95 = \frac{4}{1 + r_1} + \frac{104}{(1 + r_2)^2}$$

$$100.95 = \frac{4}{1.02997} + \frac{104}{(1 + r_2)^2}$$

$$100.95 = 3.88364 + \frac{104}{(1 + r_2)^2}$$

$$\frac{104}{(1 + r_2)^2} = 97.06636$$

$$(1 + r_2)^2 = \frac{104}{97.06636} = 1.07146$$

$$1 + r_2 = \sqrt{1.07146} = 1.03510$$

$$\boxed{r_2 = 3.5096\%}$$

---

**$r_3$ from Bond 3:**

$$102.78 = \frac{5}{1.02997} + \frac{5}{1.07146} + \frac{105}{(1 + r_3)^3}$$

$$= 4.85455 + 4.66672 + \frac{105}{(1 + r_3)^3}$$

$$= 9.52127 + \frac{105}{(1 + r_3)^3}$$

$$\frac{105}{(1 + r_3)^3} = 93.25873$$

$$(1 + r_3)^3 = \frac{105}{93.25873} = 1.12587$$

$$1 + r_3 = (1.12587)^{1/3} = 1.04033$$

$$\boxed{r_3 = 4.0333\%}$$

---

**$r_4$ from Bond 4:**

$$103.43 = \frac{5.5}{1.02997} + \frac{5.5}{1.07146} + \frac{5.5}{1.12587} + \frac{105.5}{(1 + r_4)^4}$$

$$= 5.33988 + 5.13340 + 4.88489 + \frac{105.5}{(1 + r_4)^4}$$

$$= 15.35817 + \frac{105.5}{(1 + r_4)^4}$$

$$\frac{105.5}{(1 + r_4)^4} = 88.07183$$

$$(1 + r_4)^4 = \frac{105.5}{88.07183} = 1.19792$$

$$1 + r_4 = (1.19792)^{1/4} = 1.04622$$

$$\boxed{r_4 = 4.6219\%}$$

---

**$r_5$ from Bond 5:**

$$105.01 = \frac{6}{1.02997} + \frac{6}{1.07146} + \frac{6}{1.12587} + \frac{6}{1.19792} + \frac{106}{(1 + r_5)^5}$$

$$= 5.82533 + 5.59998 + 5.32896 + 5.00867 + \frac{106}{(1 + r_5)^5}$$

$$= 21.76294 + \frac{106}{(1 + r_5)^5}$$

$$\frac{106}{(1 + r_5)^5} = 83.24706$$

$$(1 + r_5)^5 = \frac{106}{83.24706} = 1.27333$$

$$1 + r_5 = (1.27333)^{1/5} = 1.04942$$

$$\boxed{r_5 = 4.9423\%}$$

---

**Summary of Bootstrapped Spot Rates and Discount Factors:**

| $t$ | $r(t)$ | $d(t) = 1/(1+r)^t$ |
|-----|--------|---------------------|
| 1 | 2.9972% | 0.97090 |
| 2 | 3.5096% | 0.93332 |
| 3 | 4.0333% | 0.88820 |
| 4 | 4.6219% | 0.83464 |
| 5 | 4.9423% | 0.78534 |

---

### Part (b): Price a 5-Year, 8% Annual Coupon Bond

$$P = 8 \cdot d(1) + 8 \cdot d(2) + 8 \cdot d(3) + 8 \cdot d(4) + 108 \cdot d(5)$$

$$= 8(0.97090) + 8(0.93332) + 8(0.88820) + 8(0.83464) + 108(0.78534)$$

$$= 7.76720 + 7.46656 + 7.10560 + 6.67712 + 84.81672$$

$$= \boxed{\$113.8332}$$

---

### Part (c): YTM and Duration of the 8% Bond

**YTM:** Solve numerically:

$$113.8332 = \sum_{k=1}^{4} \frac{8}{(1+y)^k} + \frac{108}{(1+y)^5}$$

This requires a numerical solver. The YTM will be near the 5-year spot rate but slightly lower (because it's a coupon bond in an upward-sloping curve).

**Duration:** Once YTM is found, compute Macaulay and Modified duration using the standard formulas.

---

### Part (d): Duration Hedge with 5-Year ZCB

The 5-year ZCB has:
- $D_{\text{mac, ZCB}} = 5$ (always equals maturity for ZCB)
- $D_{\text{mod, ZCB}} = 5 / (1 + r_5) = 5 / 1.04942 = 4.7647$
- $P_{\text{ZCB}} = 100 \cdot d(5) = 100 \times 0.78534 = 78.534$

**Dollar Duration Hedge:** Match the dollar duration of the coupon bond position.

$$\text{Dollar Duration} = D_{\text{mod}} \times P \times \text{Face}$$

If we hold $FV_{\text{coupon}}$ face of the coupon bond, the face of ZCB needed to hedge is:

$$FV_{\text{ZCB}} = \frac{D_{\text{mod,coupon}} \times P_{\text{coupon}}}{D_{\text{mod,ZCB}} \times P_{\text{ZCB}}} \times FV_{\text{coupon}}$$

---

### Python Verification

```python
import numpy as np
from scipy.optimize import brentq

print("=" * 55)
print("Problem 9: Full Pipeline")
print("=" * 55)

# Market data
bonds = [
    {'T': 1, 'coupon': 0.00, 'price': 97.09},
    {'T': 2, 'coupon': 0.04, 'price': 100.95},
    {'T': 3, 'coupon': 0.05, 'price': 102.78},
    {'T': 4, 'coupon': 0.055, 'price': 103.43},
    {'T': 5, 'coupon': 0.06, 'price': 105.01},
]

# Part (a): Bootstrap
spot_rates = []
disc_factors = []

for bond in bonds:
    T = bond['T']
    c = bond['coupon']
    P = bond['price']

    # PV of all coupons before T
    pv_prev = sum(c * 100 * disc_factors[k] for k in range(T - 1))
    remaining = P - pv_prev
    final_cf = (1 + c) * 100

    # Solve for discount factor at T
    df_T = remaining / final_cf
    disc_factors.append(df_T)

    # Extract spot rate
    r_T = (1 / df_T) ** (1 / T) - 1
    spot_rates.append(r_T)

print("\n  Part (a): Bootstrapped Spot Rates")
print(f"  {'t':>3} {'r(t)':>10} {'d(t)':>10}")
print("  " + "-" * 26)
for i in range(5):
    print(f"  {i+1:3d} {spot_rates[i]:10.4%} {disc_factors[i]:10.6f}")

# Part (b): Price 8% bond
c_new = 0.08
cfs_new = [c_new * 100] * 4 + [(1 + c_new) * 100]
P_new = sum(cfs_new[i] * disc_factors[i] for i in range(5))
print(f"\n  Part (b): Price of 8% bond = ${P_new:.4f}")

# Part (c): YTM
def price_ytm(y):
    return sum(cfs_new[i] / (1 + y)**(i+1) for i in range(5))

ytm = brentq(lambda y: price_ytm(y) - P_new, 0.001, 0.5)
print(f"\n  Part (c): YTM = {ytm:.6f} = {ytm*100:.4f}%")

# Duration
times = np.arange(1, 6)
pvs_new = np.array([cfs_new[i] / (1 + ytm)**(i+1) for i in range(5)])
weights_new = pvs_new / P_new
D_mac_new = np.sum(times * weights_new)
D_mod_new = D_mac_new / (1 + ytm)
print(f"  D_mac = {D_mac_new:.4f} years")
print(f"  D_mod = {D_mod_new:.4f} years")

# Part (d): Duration hedge
D_mac_zcb = 5.0
D_mod_zcb = D_mac_zcb / (1 + spot_rates[4])
P_zcb = 100 * disc_factors[4]
print(f"\n  Part (d): Duration Hedge")
print(f"  5-year ZCB: P = ${P_zcb:.4f}, D_mac = {D_mac_zcb:.1f}, D_mod = {D_mod_zcb:.4f}")

# Per $100 face of coupon bond
fv_zcb_per_100 = (D_mod_new * P_new) / (D_mod_zcb * P_zcb)
print(f"  Face ZCB needed per $100 face coupon bond = ${fv_zcb_per_100*100:.4f}")
print(f"  For $1M face coupon bond: ${fv_zcb_per_100*1_000_000:,.2f} face of ZCB")

# Verify: dollar durations match
dd_coupon = D_mod_new * P_new * 1_000_000 / 100
dd_zcb = D_mod_zcb * P_zcb * fv_zcb_per_100 * 1_000_000 / 100
print(f"  Dollar duration (coupon): ${dd_coupon:,.2f}")
print(f"  Dollar duration (ZCB):    ${dd_zcb:,.2f}")
```

---

> **Answer Summary — Problem 9**
>
> | $t$ | Spot Rate $r(t)$ | Discount Factor $d(t)$ |
> |-----|-----------------|----------------------|
> | 1 | 2.997% | 0.97090 |
> | 2 | 3.510% | 0.93332 |
> | 3 | 4.033% | 0.88820 |
> | 4 | 4.622% | 0.83464 |
> | 5 | 4.942% | 0.78534 |
>
> Price of 8% bond ≈ **\$113.83**  
> YTM ≈ **4.86%**, $D_{\text{mac}} \approx 4.36$ years, $D_{\text{mod}} \approx 4.16$ years  
> Hedge ratio: ~$1.27 face ZCB per \$1 face coupon bond

---

## Problem 10: Grand Challenge

**Setup:** A portfolio containing:
- \$5,000,000 face value of the **5-year 8% coupon bond** (from Problem 9b)
- \$3,000,000 face value of a **2-year zero-coupon bond**

Using the spot rates bootstrapped in Problem 9.

### Part (a): Portfolio Value, Duration, and Convexity

**Coupon Bond (from Problem 9):**
- $P_{\text{coupon}} = 113.8332$ (per 100 face)
- Market value: $MV_{\text{coupon}} = 5{,}000{,}000 \times 113.8332 / 100 = \$5{,}691{,}660$

**2-Year ZCB:**

$$P_{\text{ZCB2}} = \frac{100}{(1 + r_2)^2} = 100 \times d(2) = 100 \times 0.93332 = 93.332$$

- Market value: $MV_{\text{ZCB2}} = 3{,}000{,}000 \times 93.332/100 = \$2{,}799{,}960$

**Portfolio Value:**

$$V = MV_{\text{coupon}} + MV_{\text{ZCB2}} = 5{,}691{,}660 + 2{,}799{,}960 = \boxed{\$8{,}491{,}620}$$

---

**Duration:**

For the 2-year ZCB:
- $D_{\text{mac,ZCB2}} = 2$ years
- $D_{\text{mod,ZCB2}} = 2 / (1 + r_2) = 2 / 1.03510 = 1.93219$ years

For the coupon bond (from Problem 9c): $D_{\text{mod,coupon}} \approx 4.16$ years.

**Portfolio Modified Duration** (weighted by market value):

$$D_{\text{mod,port}} = \frac{MV_{\text{coupon}} \times D_{\text{mod,coupon}} + MV_{\text{ZCB2}} \times D_{\text{mod,ZCB2}}}{V}$$

---

**Convexity:**

For the 2-year ZCB with annual compounding:

$$C_{\text{ZCB2}} = \frac{T(T+1)}{(1+y)^2} = \frac{2 \times 3}{(1.03510)^2} = \frac{6}{1.07146} = 5.5994$$

For the coupon bond, convexity is computed similarly to Problem 8.

**Portfolio Convexity** (weighted by market value):

$$C_{\text{port}} = \frac{MV_{\text{coupon}} \times C_{\text{coupon}} + MV_{\text{ZCB2}} \times C_{\text{ZCB2}}}{V}$$

---

### Part (b): Taylor Estimates for Parallel Yield Shifts

For a parallel shift $\Delta y$ applied to all yields:

$$\frac{\Delta V}{V} \approx -D_{\text{mod,port}} \times \Delta y + \frac{1}{2} C_{\text{port}} \times (\Delta y)^2$$

Apply to shifts: $\pm 50$ bps, $\pm 100$ bps, $\pm 200$ bps, $+300$ bps.

---

### Part (c): Exact Repricing

For each shift $\Delta y$:
1. Shift all spot rates: $r_t' = r_t + \Delta y$
2. Recompute discount factors: $d'(t) = 1/(1+r_t')^t$
3. Reprice each instrument and sum for new portfolio value
4. Compare $\Delta V_{\text{exact}}$ to Taylor estimate

---

### Part (d): Which Shift Is Most Inaccurate?

The **+300 bps** shift will produce the largest Taylor approximation error because:

1. **Taylor expansion is a local approximation** — it uses derivatives evaluated at the current yield. For large $\Delta y$, higher-order terms ($3^{\text{rd}}$ derivative and beyond) become significant.
2. The approximation error grows roughly as $O((\Delta y)^3)$ when using the 2nd-order Taylor expansion.
3. To improve accuracy, we would need the **3rd derivative** (speed/rate of change of convexity) and potentially the **4th derivative** of the price-yield function.

---

### Python Verification

```python
import numpy as np
from scipy.optimize import brentq

print("=" * 55)
print("Problem 10: Grand Challenge")
print("=" * 55)

# Spot rates from Problem 9
# (Re-bootstrap to get exact values)
bonds_data = [
    {'T': 1, 'coupon': 0.00, 'price': 97.09},
    {'T': 2, 'coupon': 0.04, 'price': 100.95},
    {'T': 3, 'coupon': 0.05, 'price': 102.78},
    {'T': 4, 'coupon': 0.055, 'price': 103.43},
    {'T': 5, 'coupon': 0.06, 'price': 105.01},
]

spot_rates = []
disc_factors = []
for bond in bonds_data:
    T = bond['T']
    c = bond['coupon']
    P = bond['price']
    pv_prev = sum(c * 100 * disc_factors[k] for k in range(T - 1))
    remaining = P - pv_prev
    final_cf = (1 + c) * 100
    df_T = remaining / final_cf
    disc_factors.append(df_T)
    r_T = (1 / df_T) ** (1 / T) - 1
    spot_rates.append(r_T)

# ============ Bond 1: 5-year 8% coupon bond ============
c_coup = 0.08
cfs_coup = [c_coup * 100] * 4 + [(1 + c_coup) * 100]
P_coup = sum(cfs_coup[i] * disc_factors[i] for i in range(5))
face_coup = 5_000_000

# YTM of coupon bond
def price_ytm_coup(y):
    return sum(cfs_coup[i] / (1 + y)**(i+1) for i in range(5))

ytm_coup = brentq(lambda y: price_ytm_coup(y) - P_coup, 0.001, 0.5)

# Duration & Convexity of coupon bond
times = np.arange(1, 6, dtype=float)
pvs_coup = np.array([cfs_coup[i] / (1 + ytm_coup)**(i+1) for i in range(5)])
w_coup = pvs_coup / P_coup
D_mac_coup = np.sum(times * w_coup)
D_mod_coup = D_mac_coup / (1 + ytm_coup)

conv_terms_coup = np.array([times[i]*(times[i]+1)*cfs_coup[i]/(1+ytm_coup)**(times[i])
                             for i in range(5)])
C_coup = conv_terms_coup.sum() / (P_coup * (1 + ytm_coup)**2)

MV_coup = face_coup * P_coup / 100

# ============ Bond 2: 2-year ZCB ============
P_zcb2 = 100 * disc_factors[1]  # d(2) = disc_factors[1]
face_zcb2 = 3_000_000
ytm_zcb2 = spot_rates[1]
D_mac_zcb2 = 2.0
D_mod_zcb2 = D_mac_zcb2 / (1 + ytm_zcb2)
C_zcb2 = 2 * 3 / (1 + ytm_zcb2)**2
MV_zcb2 = face_zcb2 * P_zcb2 / 100

# ============ Part (a): Portfolio metrics ============
V = MV_coup + MV_zcb2
D_mod_port = (MV_coup * D_mod_coup + MV_zcb2 * D_mod_zcb2) / V
C_port = (MV_coup * C_coup + MV_zcb2 * C_zcb2) / V

print(f"\n  Part (a): Portfolio Composition")
print(f"    Coupon bond: P = ${P_coup:.4f}, MV = ${MV_coup:,.2f}")
print(f"      D_mac = {D_mac_coup:.4f}, D_mod = {D_mod_coup:.4f}, C = {C_coup:.4f}")
print(f"    2yr ZCB:     P = ${P_zcb2:.4f}, MV = ${MV_zcb2:,.2f}")
print(f"      D_mac = {D_mac_zcb2:.4f}, D_mod = {D_mod_zcb2:.4f}, C = {C_zcb2:.4f}")
print(f"    Portfolio: V = ${V:,.2f}")
print(f"      D_mod_port = {D_mod_port:.4f}")
print(f"      C_port = {C_port:.4f}")

# ============ Parts (b) & (c): Taylor vs Exact ============
shifts_bps = [-200, -100, -50, 50, 100, 200, 300]

print(f"\n  Parts (b) & (c): Taylor Estimates vs Exact Repricing")
print(f"  {'Shift':>8} {'Taylor ΔV':>14} {'Exact ΔV':>14} {'Error':>14} {'Error%':>8}")
print("  " + "-" * 62)

for bps in shifts_bps:
    dy = bps / 10000

    # Taylor estimate
    taylor_pct = -D_mod_port * dy + 0.5 * C_port * dy**2
    taylor_dv = taylor_pct * V

    # Exact: shift all spot rates and reprice
    shifted_spots = [r + dy for r in spot_rates]
    shifted_df = [1 / (1 + shifted_spots[i])**(i+1) for i in range(5)]

    # Reprice coupon bond
    P_coup_new = sum(cfs_coup[i] * shifted_df[i] for i in range(5))
    MV_coup_new = face_coup * P_coup_new / 100

    # Reprice 2yr ZCB
    P_zcb2_new = 100 * shifted_df[1]
    MV_zcb2_new = face_zcb2 * P_zcb2_new / 100

    V_new = MV_coup_new + MV_zcb2_new
    exact_dv = V_new - V
    error = taylor_dv - exact_dv

    print(f"  {bps:>+4d} bps {taylor_dv:>14,.2f} {exact_dv:>14,.2f} {error:>14,.2f} {error/V*100:>+8.4f}%")

# Part (d)
print(f"\n  Part (d): +300 bps has the largest error because Taylor is a local approximation.")
print(f"    Error grows as O((Δy)^3) — need 3rd+ derivatives for large shifts.")
```

---

> **Answer Summary — Problem 10**
>
> (a) Portfolio value ≈ **\$8.49M**, portfolio $D_{\text{mod}} \approx 3.4$, portfolio $C \approx 16$  
> (b) Taylor estimates computed for ±50, ±100, ±200, +300 bps  
> (c) Exact repricing shows Taylor is excellent for small shifts, deteriorates for large shifts  
> (d) **+300 bps** produces the largest error — Taylor is a 2nd-order approximation; the error term is $O((\Delta y)^3)$

---

## 📊 Master Formula Reference

| Formula | Expression |
|---------|-----------|
| FV (discrete) | $PV(1 + r/m)^{mt}$ |
| FV (continuous) | $PV \cdot e^{rt}$ |
| ZCB price (discrete) | $F/(1+y)^T$ |
| ZCB price (continuous) | $F \cdot e^{-yT}$ |
| Coupon bond price | $\sum C/(1+y/m)^k + F/(1+y/m)^n$ |
| Discount factor | $d(t) = 1/(1+r(t))^t$ |
| Macaulay Duration | $\sum t \cdot w_t$ where $w_t = PV(CF_t)/P$ |
| Modified Duration | $D_{\text{mac}}/(1+y/m)$ |
| Convexity | $\frac{1}{P(1+y/m)^2} \sum \frac{k(k+1)}{m^2} \cdot \frac{CF_k}{(1+y/m)^k}$ |
| Taylor (2nd order) | $\Delta P/P \approx -D_{\text{mod}} \Delta y + \frac{1}{2} C (\Delta y)^2$ |
| EAR | $(1+r/m)^m - 1$ |
| Continuous ↔ Discrete | $r_{\text{cont}} = \ln(1 + r_{\text{annual}})$ |

---

*Solutions prepared for MIT 18.642 — Problem Set 1*
