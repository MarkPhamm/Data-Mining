# Polynomial Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].to_numpy()
y = dataset.iloc[:, -1].to_numpy()

# Training the Polynomial Regression model on the whole dataset
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

sc = StandardScaler()

# poly_feature = PolynomialFeatures(degree = 2, include_bias = False)
# X_poly = poly_feature.fit_transform(X)
# regressor = LinearRegression()
# regressor.fit(X_poly, y)
# regressor.summary()

for degree in range(2, 6):
    poly_feature = PolynomialFeatures(degree=degree, include_bias=False)
    X_poly = poly_feature.fit_transform(X)
    X_poly[:, 1:] = sc.fit_transform(X_poly[:, 1:])
    regressor = sm.OLS(endog = y, exog = X_poly).fit()
    print(f"Summary for degree {degree}:\n", regressor.summary())

# Finding the optimal degree using p-value

# Visualizing the Polynomial Regression results
# plt.scatter(X_poly[:,1], y, color = 'red')
# plt.plot(X_poly[:,1], regressor.predict(X_poly), color = 'blue')
# plt.title('Polynomial Regression')
# plt.xlabel('Position level')
# plt.ylabel('Salary (Scaled)')
# plt.show()

# Visualizing the Polynomial Regression results (for higher resolution and
# smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
X_grid_poly = poly_feature.transform(X_grid)
X_grid_poly[:, 1:] = sc.transform(X_grid_poly[:, 1:])
plt.scatter(X, y, color='red')
plt.plot(X_grid, regressor.predict(X_grid_poly), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary (Scaled)')
plt.show()