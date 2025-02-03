# Data-Mining

Replace empty cell with legit data (mean, median, mode)
Not looking for precise result, but better result
Encoding textual data: one hot encoder, label encoder

fit: Calculating parameters, store the info within the object 
transform: Calculating new data

# Multiple Linear Regression
Assumptions for linear regression:
1. Linearity: The relationship between the independent and dependent variables should be linear.
2. Homoscedasticity: The residuals (errors) should have constant variance at every level of the independent variable.
3. Multivariate normality: The residuals should be normally distributed.
4. No multicollinearity: Independent variables should not be too highly correlated with each other.
5. Independence of errors: The residuals should be independent of each other.

To ensure these assumptions are met, it is important to:
- Visualize relationships using scatter plots to check for linearity.
- Use residual plots to assess homoscedasticity.
- Conduct normality tests (e.g., Shapiro-Wilk test) on residuals.
- Calculate Variance Inflation Factor (VIF) to detect multicollinearity.
- Analyze residuals over time or across observations to confirm independence.