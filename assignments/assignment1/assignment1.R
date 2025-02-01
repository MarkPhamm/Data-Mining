# Data Preprocessing Tools

# Importing the libraries
library(dplyr)
library(tidyr)

# The last column 'Purchased' is a categorical variable indicating whether a purchase was made (Yes/No).
# Therefore, we are trying to solve a classification problem using machine learning.

# Importing the dataset
dataset <- read.csv('Customer_Data.csv')
X <- dataset[, -ncol(dataset)]  # Country, Age, Salary columns
y <- dataset[, ncol(dataset)]    # Purchased column

# Taking care of missing data
# For Age column - using median
X$Age[is.na(X$Age)] <- median(X$Age, na.rm = TRUE)

# For Salary column - using mean
X$Salary[is.na(X$Salary)] <- mean(X$Salary, na.rm = TRUE)

# Encoding categorical data
# Encoding the Independent Variable (Country)
X <- dummy.data.frame(X, names = "Country", sep = "_")

# Encoding the Dependent Variable (Purchased)
y <- as.numeric(factor(y, levels = c("No", "Yes")))

# Splitting the dataset into the Training set and Test set
set.seed(0)
train_indices <- sample(1:nrow(X), size = floor(2/3 * nrow(X)))
X_train <- X[train_indices, ]
X_test <- X[-train_indices, ]
y_train <- y[train_indices]
y_test <- y[-train_indices]

# Feature Scaling using normalization
X_train <- scale(X_train)
X_test <- scale(X_test)

# Print shapes to verify the split
cat('Training set shape:', dim(X_train), '\n')
cat('Test set shape:', dim(X_test), '\n')
