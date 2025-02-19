# Polynomial Regression

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[, 2:3]

# Fitting Polynomial Regression to the whole dataset
dataset$Level2 = dataset$Level^2
regressor = lm(formula = Salary ~ .,
              data = dataset)

# Finding the optimal degree using p-value

# Visualizing the Polynomial Regression results
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            colour = 'blue') +
  ggtitle('Polynomial Regression') +
  xlab('Level') +
  ylab('Salary')

# Visualizing the Regression Model results (for higher resolution and smoother curve)
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor,
                                        newdata = data.frame('Level' = x_grid,
                                                             'Level2' = x_grid^2,
                                                             'Level3' = x_grid^3,
                                                             'Level4' = x_grid^4))),
            colour = 'blue') +
  ggtitle('Polynomial Regression') +
  xlab('Level') +
  ylab('Salary')