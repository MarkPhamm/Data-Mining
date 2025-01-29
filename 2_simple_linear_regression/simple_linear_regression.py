# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].to_numpy()
y = dataset.iloc[:, -1].to_numpy()

# EDA
# plt.scatter(X, y, color='red')
# plt.title('Scatter Plot of Salary vs Years of Experience')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3,
                                                    random_state = 0)

# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()  # Corrected instantiation of the LinearRegression model
regressor.fit(X_train, y_train)  # Fitting the model to the training data

# Predicting the Test set results
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
y_pred = regressor.predict(X_test)  # Store predictions in y_pred
print(math.sqrt(mean_squared_error(X_test, y_test)))
print(mean_absolute_percentage_error(y_test, y_pred))  # Compare y_test with y_pred


# Visualizing the Training set results
plt.scatter(X_train, y_train, alpha=0.5, color='red', edgecolor='black')
plt.plot(X_train, regressor.predict(X_train), color='blue', linewidth=2, label='Predicted Salary')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()



# Visualizing the Test set results
plt.scatter(X_test, y_test, alpha=0.5, color='red', edgecolor='black')
plt.plot(X_train, regressor.predict(X_train), color='black', linewidth=2, label='Predicted Salary for training set')
plt.plot(X_test, regressor.predict(X_test), color='blue', linewidth=2, label='Predicted Salary for test')
plt.title('Salary vs Experience (Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()


# Making a single prediction
print(regressor.predict(np.array(12).reshape(1, -1)))  # Reshapes 12 into [[12]] for prediction

# Getting the final linear regression equation with the values of the
# coefficients
print(regressor.coef_)
print(regressor.intercept_)