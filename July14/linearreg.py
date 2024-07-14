import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Seed for reproducibility
np.random.seed(42)

# Generate random data
sizes = np.random.randint(1000, 3000, 100)
prices = sizes * 200 + np.random.normal(0, 50000, 100)  # Adding noise

# Create a DataFrame
data = {'Size': sizes, 'Price': prices}
df = pd.DataFrame(data)

# Plot the scattered data
plt.scatter(df['Size'], df['Price'], color='blue')
plt.xlabel('Size of House')
plt.ylabel('Price of House')
plt.title('Scattered House Size vs Price Data')
# plt.show()

# Features and target variable
X = df[['Size']]
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plotting the regression line
plt.scatter(df['Size'], df['Price'], color='blue')
plt.plot(df['Size'], model.predict(X), color='red')
plt.xlabel('Size of House')
plt.ylabel('Price of House')
plt.title('Linear Regression on Scattered Data')
plt.show()

# Predicting the price of a house with size 2000
predicted_price = model.predict([[2000]]) # type: ignore
print(f'Predicted price for a 2000 sq ft house: ${predicted_price[0]:.2f}')
