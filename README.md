# Data-Mining

# Note
Replace empty cell with legit data (mean, median, mode)
Not looking for precise result, but better result
Encoding textual data: one hot encoder, label encoder

## Fit vs Transform
fit: Calculating parameters, store the info within the object 
transform: Calculating new data

# Simple Linear Regression
Simple linear regression can be represented by the following equation:

y = β₀ + β₁x + ε

Where:  
- y is the dependent variable  
- x is the independent variable  
- β₀ is the y-intercept  
- β₁ is the slope (coefficient)  
- ε is the error term

## Assumptions for linear regression:
1. Linearity: The relationship between the independent and dependent variables should be linear.
2. Homoscedasticity: The residuals (errors) should have constant variance at every level of the independent variable.
3. Multivariate normality: The residuals should be normally distributed.
4. No multicollinearity: Independent variables should not be too highly correlated with each other.
5. Independence of errors: The residuals should be independent of each other.

## To ensure these assumptions are met, it is important to:
- Visualize relationships using scatter plots to check for linearity.
- Use residual plots to assess homoscedasticity.
- Conduct normality tests (e.g., Shapiro-Wilk test) on residuals.
- Calculate Variance Inflation Factor (VIF) to detect multicollinearity.
- Analyze residuals over time or across observations to confirm independence.

# Multiple Linear Regression
Multiple linear regression can be represented by the following equation:

y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε

Where:  
- y is the dependent variable  
- x₁, x₂, ..., xₙ are the independent variables  
- β₀ is the y-intercept  
- β₁, β₂, ..., βₙ are the coefficients  
- ε is the error term

## Model Building Methods
1. **All-in**: Use all the predictors available in the dataset.
2. **Backward Elimination**: Start with all predictors and remove the least significant one at each step.
3. **Forward Selection**: Start with no predictors and add the most significant one at each step.
4. **Bidirectional Elimination**: Combine forward selection and backward elimination.
5. **Score Comparison**: Compare different models using a scoring metric like AIC or BIC to select the best one.

### **Backward Elimination**
1. **Step 1**: Select a significant level to stay in the model (e.g. SL = 0.05)
2. **Step 2**: Fit the full model with all possible predictors
3. **Step 3**: Consider the predictor with the highest P-value. If P > SL, remove the predictor
4. **Step 4**: Fit the model without this variable and repeat step 3
5. **Step 5**: Stop when no more predictors can be removed

### **Forward Selection**
1. **Step 1**: Select a significant level to stay in the model (e.g. SL = 0.05)
2. **Step 2**: Fit all simple regression models y~Xn and select the one with the lowest P-value
3. **Step 3**: Keep this variable and fit all possible models with one extra predictor to the one(s) you already have
4. **Step 4**: Consider the predictor with the lowest P-value. If P < SL, go to step 3, else go to FIN

### **Bidirectional Elimination**
1. **Step 1**: Select a significant level to enter and stay in the model: e.g., SLEnter = 0.05, SLStay = 0.05
2. **Step 2**: Perform the steps of Forward Selection:
   - Start with no predictors in the model.
   - Add predictors one by one based on the lowest P-value, provided it is less than SLEnter.
3. **Step 3**: After adding a new predictor, perform Backward Elimination:
   - Check all predictors in the model.
   - Remove the predictor with the highest P-value if it is greater than SLStay.
4. **Step 4**: Repeat steps 2 and 3 until no new predictors can be added and no existing predictors can be removed.
5. **Step 5**: Finalize the model when no further changes can be made.

## Rule: Dealing with Backward Elimination
1. Don't remove coefficients arbitrarily
2. Keep all categorical data in a column or remove the entire column. If P-values of all levels are insignificant, then you can remove all levels

# Polynomial Regression
Polynomial regression can be represented by the following equation:

y = β₀ + β₁x + β₂x² + β₃x³ + ... + βₙxⁿ + ε

Where:  
- y is the dependent variable  
- x is the independent variable  
- β₀ is the y-intercept  
- β₁, β₂, ..., βₙ are the coefficients of the polynomial  
- n is the degree of the polynomial  
- ε is the error term

