# simple linear regression
# Least Squares Estimation

# Page 115, question
# 100-meter race world records, build a simple linear regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data (x: years, y: recorded values)
years = np.array([1896, 1912, 1921, 1930, 1936, 1956, 1960, 1968])
values = np.array([11.80, 10.60, 10.40, 10.30, 10.20, 10.10, 10.00, 9.95])

X = years.reshape(-1, 1)
y = values
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
print(model.coef_)
print(model.intercept_)
print(y_pred)

# Plotting the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(years, values, color='blue', label='Data points')
plt.plot(years, y_pred, color='red', linewidth=2, label='Regression line')
plt.title('Simple Linear Regression')
plt.xlabel('Year')
plt.ylabel('Recorded Value')
plt.legend()
plt.grid(True)
plt.show()
