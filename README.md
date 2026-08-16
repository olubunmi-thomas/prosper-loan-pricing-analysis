# Prosper Loan APR Analysis

An end-to-end statistical and machine-learning analysis of Prosper
peer-to-peer lending data, focused on understanding the borrower and
loan characteristics associated with Borrower APR.

## Business question

> What borrower and loan characteristics are associated with the
> interest rate charged to borrowers on the Prosper peer-to-peer lending
> platform?

## Objectives

-   Assess data quality and missingness.
-   Explore the distribution of Borrower APR.
-   Examine APR differences across credit ratings and borrower
    characteristics.
-   Investigate time trends in loan activity and APR.
-   Quantify associations using multiple linear regression.
-   Diagnose linear-regression assumptions.
-   Use heteroscedasticity-robust standard errors where appropriate.
-   Compare interpretable linear prediction with a nonlinear
    machine-learning model.
-   Evaluate predictive performance on a chronological holdout.

## Key findings

1.  **Prosper Rating is the dominant APR signal.** APR falls strongly
    and monotonically as Prosper Rating improves.
2.  **APR varies materially over time.** Average APR rises into 2011 and
    then declines through 2014.
3.  **Simple correlations do not tell the whole story.** Loan amount has
    a moderate negative correlation with APR, but categorical
    credit-rating effects are much stronger in the regression.
4.  **The OLS model is highly explanatory but not perfectly specified.**
    The fitted model has an R² of about 0.93, while residual diagnostics
    and the Breusch--Pagan test indicate heteroscedasticity.
5.  **Statistical significance must be separated from economic
    importance.** The large sample makes very small effects
    statistically detectable.
6.  **Future-like validation matters.** The machine-learning comparison
    uses a chronological train/test split rather than mixing future
    observations into the training data.

## Dataset

The project uses the Prosper Loan Data dataset, originally published
through Udacity's Data Analyst Nanodegree materials.

The notebook expects:

``` text
prosper_loan.csv
```

in the working directory.

## Analysis workflow

``` text
Data loading
    ↓
Data quality & missingness
    ↓
Data validation
    ↓
Univariate EDA
    ↓
Time analysis
    ↓
Credit-rating analysis
    ↓
Bivariate analysis & correlations
    ↓
Statistical tests
    ↓
Feature engineering
    ↓
OLS regression
    ↓
Regression diagnostics
    ↓
Robust inference
    ↓
Chronological ML validation
    ↓
Model comparison
    ↓
Business interpretation
```

## Models

### OLS

Used primarily for interpretation. The model estimates conditional
associations between Borrower APR and:

-   Prosper Rating
-   Term
-   Log monthly income
-   Debt-to-income ratio
-   Log loan amount
-   Employment status
-   Home ownership

### Ridge regression

Used as a regularized linear prediction benchmark.

### HistGradientBoosting

Used as a nonlinear benchmark capable of learning nonlinear
relationships that a linear model may miss.

## Important modeling decisions

### Avoiding target leakage

The project deliberately avoids downstream pricing variables such as
BorrowerRate and LenderYield when predicting Borrower APR. Including
variables created as part of the pricing process would make predictive
performance misleading.

### Missing values

The statistical OLS model uses complete cases for transparency. The
machine-learning pipeline handles missing values inside the
preprocessing pipeline so that imputation parameters are learned from
training data only.

### Validation

The predictive models use a chronological 80/20 split. Earlier loans are
used for training and later loans are reserved for testing.

## Repository structure

``` text
prosper-loan-apr-analysis/
├── data/
│   └── prosper_loan.csv
├── notebooks/
│   └── prosper_loan_analysis_portfolio.ipynb
├── src/
│   └── styleplot.py
├── requirements.txt
└── README.md
```

## Recommended portfolio visuals

The strongest visuals to feature in a GitHub README or LinkedIn post
are:

1.  Borrower APR by Prosper Rating
2.  Average Borrower APR over time
3.  Correlation matrix of key numerical variables
4.  Residuals vs fitted values
5.  Q-Q plot
6.  Actual vs predicted APR on the chronological test set

## Limitations

This is an observational analysis, so regression coefficients should be
interpreted as associations rather than causal effects. The original
dataset also contains substantial missingness in several variables, and
the regression diagnostics show heteroscedasticity and non-normal
residual tails.

## Next steps

-   Tune the nonlinear model using cross-validation restricted to the
    training period.
-   Evaluate model performance by Prosper Rating and loan term.
-   Add prediction intervals or uncertainty analysis.
-   Build a lightweight dashboard for interactive exploration.
-   Move reusable preprocessing and modeling functions into `src/`.

## Data source

Prosper Loan Data:
https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv


