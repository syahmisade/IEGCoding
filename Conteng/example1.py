import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Generate synthetic data for a realistic scenario
np.random.seed(42)
n_samples = 200

# Simulate age (20 to 60 years) and salary ($20k to $100k)
age = np.random.randint(20, 61, n_samples)
salary = np.random.randint(20000, 100001, n_samples)

# Simulate purchase behavior: higher probability of purchase with higher age and salary
purchase_prob = 1 / (1 + np.exp(-0.05 * (age - 30) + 0.0001 * (salary - 50000)))
purchase = np.random.binomial(1, purchase_prob)

# Create DataFrame
df = pd.DataFrame({'Age': age, 'Salary': salary, 'Purchased': purchase})
print(df.head())

# Split the data
X = df[['Age', 'Salary']]
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{class_report}')

# Visualize the decision boundary
def plot_decision_boundary(X, y, model):
    # Create a mesh grid
    x_min, x_max = X['Age'].min() - 1, X['Age'].max() + 1
    y_min, y_max = X['Salary'].min() - 1000, X['Salary'].max() + 1000
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 1),
                         np.arange(y_min, y_max, 1000))
    
    # Predict the class for each point in the mesh grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X['Age'], X['Salary'], c=y, edgecolor='k', marker='o')
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.title('Decision Boundary')
    plt.show()

plot_decision_boundary(X, y, model)
