# Portfolio Management & Multi-Factor Models

---

## 🕒 Lesson 11.1: The Capital Asset Pricing Model (CAPM)

> [!NOTE]
> **Summary in 1 Sentence:**
> CAPM states that an asset's expected return is determined solely by its sensitivity to systematic market risk (Beta).

### 1. Intuition (ELIF5)
Imagine opening a business. You face two types of risk:
1. **Specific Risk:** The risk that your chef quits. You can fix this by hiring backup chefs (diversification). The market doesn't pay you extra for this risk because it's easy to avoid.
2. **Systemic Risk:** The risk of a major recession where no one goes out to eat. You cannot avoid this. The market rewards you with higher expected returns for taking this unavoidable risk.
**Beta ($eta$)** measures how sensitive your business is to the general economy.

### 2. Formulas
* **Expected Return of Asset $i$:**
  $$E[R_i] = R_f + eta_i (E[R_m] - R_f)$$
* **Beta Calculation:**
  $$eta_i = rac{	ext{Cov}(R_i, R_m)}{	ext{Var}(R_m)}$$

---

## 🕒 Lesson 11.2: Multi-Factor Risk Models

> [!NOTE]
> **Summary in 1 Sentence:**
> Multi-factor models decompose asset returns into exposures to multiple systematic risk factors plus an idiosyncratic residual.

### 1. Intuition (ELIF5)
Instead of saying a stock moves only because of the general market, we can use multiple factors to explain its return. For example, a stock might be sensitive to:
* The general stock market.
* Interest rate shifts.
* Oil prices.
* Inflation.
By identifying these "factors," we can build portfolios that are immune to specific risks (e.g., building a portfolio that doesn't care about oil price changes).

### 2. Formulas
$$R_i = lpha_i + eta_{i,1} F_1 + eta_{i,2} F_2 + \dots + eta_{i,k} F_k + \epsilon_i$$
Where $F_j$ are factor returns, $eta_{i,j}$ are factor exposures (loadings), and $\epsilon_i$ is idiosyncratic noise.
