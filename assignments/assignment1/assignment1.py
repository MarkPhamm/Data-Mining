# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The last column 'Purchased' is a categorical variable indicating whether a purchase was made (Yes/No).
# Therefore, we are trying to solve a classification problem using machine learning.

# Importing the dataset
dataset = pd.read_csv('Customer_Data.csv')
X = dataset.iloc[:, :-1].to_numpy()  # Country, Age, Salary columns
y = dataset.iloc[:, -1].to_numpy()   # Purchased column

# Taking care of missing data
from sklearn.impute import SimpleImputer
# For Age column (index 1) - using median
imputer_age = SimpleImputer(missing_values=np.nan, strategy="median")
X[:, 1:2] = imputer_age.fit_transform(X[:, 1:2])

# For Salary column (index 2) - using mean
imputer_salary = SimpleImputer(missing_values=np.nan, strategy="mean")
X[:, 2:3] = imputer_salary.fit_transform(X[:, 2:3])

# Encoding categorical data
# Encoding the Independent Variable (Country)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = ct.fit_transform(X)
X = np.array(X)

# Encoding the Dependent Variable (Purchased)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Feature Scaling using normalization
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Print shapes to verify the split
print('Training set shape:', X_train.shape)
print('Test set shape:', X_test.shape)
