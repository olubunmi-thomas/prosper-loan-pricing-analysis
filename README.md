# Prosper Loan Pricing Analysis

## Overview

This project investigates the factors associated with the annual percentage
rate (APR) charged to borrowers on the Prosper peer-to-peer lending platform.

The analysis combines exploratory data analysis, statistical modelling,
multicollinearity diagnostics, heteroscedasticity testing, and robust
regression inference.

## Research Question

> What factors determine the interest rate charged to borrowers on the
> Prosper peer-to-peer lending platform?

## Objectives

The analysis aims to:

- Examine the distribution of BorrowerAPR.
- Investigate missing data and data quality.
- Examine borrower and loan characteristics associated with APR.
- Quantify the relationship between ProsperRating and BorrowerAPR.
- Build progressively more comprehensive OLS regression models.
- Diagnose multicollinearity using Variance Inflation Factors (VIF).
- Test for heteroscedasticity using the Breusch-Pagan test.
- Apply HC3 robust standard errors.
- Identify the most important factors associated with borrower pricing.

## Dataset

The project uses the Prosper Loan Data dataset.

The primary outcome variable is:

**BorrowerAPR** — the annual percentage rate charged to the borrower.

Important explanatory variables include:

- ProsperRating
- ProsperScore
- CreditScore
- Term
- LoanOriginalAmount
- StatedMonthlyIncome
- DebtToIncomeRatio
- EmploymentStatus
- IsBorrowerHomeowner
- CurrentCreditLines
- TotalCreditLinespast7years
- DelinquenciesLast7Years
- BankcardUtilization

## Methodology

The analysis follows these stages:

1. Data loading and inspection
2. Data quality assessment
3. Missing-value analysis
4. Exploratory data analysis
5. Progressive OLS regression modelling
6. Model comparison
7. Multicollinearity diagnostics using VIF
8. Model refinement
9. Breusch-Pagan heteroscedasticity test
10. HC3 robust regression inference
11. Final model interpretation

## Model Development

### Model 1 — ProsperRating

The first model examines the relationship between ProsperRating and
BorrowerAPR.

### Model 2 — Loan Characteristics

Loan term and original loan amount are added.

### Model 3 — Borrower Characteristics

Employment status, home ownership, income, and debt-to-income ratio
are introduced.

### Model 4 — Credit Characteristics

Additional credit variables are added, including CreditScore,
ProsperScore, CurrentCreditLines, TotalCreditLinespast7years,
DelinquenciesLast7Years, and BankcardUtilization.

## Model Results

The final model explains approximately **93.1% of the variation in
BorrowerAPR**.

| Model | R-squared | Description |
|---|---:|---|
| Model 1 | 0.930 | ProsperRating |
| Model 2 | 0.930 | + Loan characteristics |
| Model 3 | 0.930 | + Borrower characteristics |
| Model 4 | 0.931 | + Credit characteristics |

The relatively small increase in R-squared indicates that ProsperRating
captures a substantial amount of the information associated with
BorrowerAPR.

## Key Findings

### 1. ProsperRating is the dominant predictor

Using Rating 7 as the reference category, lower ProsperRating categories
are associated with substantially higher BorrowerAPR.

Estimated differences relative to Rating 7 include approximately:

| Rating | APR Difference |
|---|---:|
| 1 | +27.15 percentage points |
| 2 | +24.53 percentage points |
| 3 | +19.46 percentage points |
| 4 | +14.04 percentage points |
| 5 | +9.74 percentage points |
| 6 | +5.10 percentage points |

All ProsperRating effects are statistically significant.

### 2. Multicollinearity was identified and addressed

The initial model showed substantial multicollinearity between
CurrentCreditLines and OpenCreditLines.

OpenCreditLines was removed from the final specification.

The VIF for CurrentCreditLines decreased from approximately 15.3
to approximately 1.9.

### 3. Heteroscedasticity was detected

The Breusch-Pagan test provided strong evidence of heteroscedasticity:

- LM statistic: 6552.10
- LM p-value: < 0.001
- F statistic: 286.18
- F p-value: < 0.001

Therefore, HC3 heteroscedasticity-robust standard errors were used
for the final regression inference.

### 4. Residual autocorrelation is limited

The Durbin-Watson statistic is approximately 2.00, indicating little
evidence of first-order residual autocorrelation.

### 5. Residual normality is rejected

The Jarque-Bera test rejects the hypothesis of normally distributed
residuals.

## Final Model

The final specification includes:

- ProsperRating
- Term
- EmploymentStatus
- IsBorrowerHomeowner
- LoanOriginalAmount
- StatedMonthlyIncome
- DebtToIncomeRatio
- EmploymentStatusDuration
- CreditScore
- ProsperScore
- CurrentCreditLines
- TotalCreditLinespast7years
- DelinquenciesLast7Years
- BankcardUtilization

HC3 robust standard errors are used for statistical inference.

## Limitations

This analysis is observational and therefore identifies associations,
not causal effects.

Important limitations include:

- Missing data may introduce selection bias.
- Residuals are not normally distributed.
- Heteroscedasticity is present.
- Some credit variables may capture overlapping aspects of borrower
  credit quality.
- High R-squared does not guarantee strong predictive performance
  on unseen observations.
- The analysis focuses on BorrowerAPR rather than loan default or
  borrower profitability.
