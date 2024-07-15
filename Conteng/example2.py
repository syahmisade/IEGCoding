import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Generate synthetic data for a realistic scenario with one feature (Age)
np.random.seed(42)
n_samples = 200

# Simulate age (20 to 60 years)
age = np.random.randint(20, 61, n_samples)

# Simulate purchase behavior: higher probability of purchase with higher age
purchase_prob = 1 / (1 + np.exp(-0.1 * (age - 40)))
purchase = np.random.binomial(1, purchase_prob)

# Create DataFrame
df = pd.DataFrame({'Age': age, 'Purchased': purchase})
print(df.head())

# Split the data
X = df[['Age']]
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

# Visualize the sigmoid curve
def plot_sigmoid_curve(X, y, model):
    # Sort the data for plotting
    sorted_indices = np.argsort(X['Age'].values)
    sorted_age = X['Age'].values[sorted_indices]
    sorted_prob = model.predict_proba(X)[:, 1][sorted_indices]
    
    # Plot the actual data points
    plt.scatter(X['Age'], y, c=y, edgecolor='k', marker='o', label='Data points')

    # Plot the sigmoid curve
    plt.plot(sorted_age, sorted_prob, color='red', label='Sigmoid curve')
    plt.xlabel('Age')
    plt.ylabel('Probability of Purchase')
    plt.title('Sigmoid Curve for Logistic Regression')
    plt.legend()
    plt.show()

plot_sigmoid_curve(X, y, model)
