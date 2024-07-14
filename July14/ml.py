'''
Machine Learning Algorithm
- Supervised Learning
    - Data have labels
- Unsupervised Learning
    - Data do not have labels
- Reinforcement Learning


### 1. **Linear Regression**
- **Purpose**: Predict a continuous value.
- **How it works**: Fits a line to the data points, so you can predict new values.
- **Example**: Predicting house prices based on size.

### 2. **Logistic Regression**
- **Purpose**: Classify data into two categories.
- **How it works**: Uses a logistic function to output probabilities that map to binary classes.
- **Example**: Determining if an email is spam or not.

### 3. **Decision Trees**
- **Purpose**: Both regression and classification.
- **How it works**: Splits data into branches to make decisions.
- **Example**: Predicting if someone will buy a product based on age and income.

### 4. **Random Forests**
- **Purpose**: Both regression and classification.
- **How it works**: Combines multiple decision trees to improve accuracy.
- **Example**: Predicting loan defaults by considering many factors.

### 5. **Support Vector Machines (SVM)**
- **Purpose**: Classification.
- **How it works**: Finds the best boundary that separates classes.
- **Example**: Classifying emails into different folders.

### 6. **K-Nearest Neighbors (KNN)**
- **Purpose**: Both regression and classification.
- **How it works**: Classifies data points based on the majority class of their neighbors.
- **Example**: Recommending movies based on user preferences.

### 7. **K-Means Clustering**
- **Purpose**: Unsupervised learning for grouping data.
- **How it works**: Divides data into clusters based on similarity.
- **Example**: Grouping customers by purchasing behavior.

### 8. **Naive Bayes**
- **Purpose**: Classification.
- **How it works**: Uses probability based on Bayes' theorem.
- **Example**: Text classification like spam detection.

### 9. **Neural Networks**
- **Purpose**: Both regression and classification.
- **How it works**: Mimics the human brain with layers of neurons.
- **Example**: Image and speech recognition.

### 10. **Principal Component Analysis (PCA)**
- **Purpose**: Dimensionality reduction.
- **How it works**: Transforms data to reduce the number of features while retaining variance.
- **Example**: Simplifying data for easier visualization.

### 11. **Gradient Boosting Machines (GBM)**
- **Purpose**: Both regression and classification.
- **How it works**: Builds models sequentially to correct errors from previous models.
- **Example**: Improving accuracy in predicting customer churn.

### 12. **Recurrent Neural Networks (RNN)**
- **Purpose**: Sequence prediction.
- **How it works**: Uses previous output as input for current predictions.
- **Example**: Language translation.

### 13. **Convolutional Neural Networks (CNN)**
- **Purpose**: Image and video analysis.
- **How it works**: Uses convolutional layers to detect patterns.
- **Example**: Detecting objects in images.

These algorithms form the backbone of many modern machine learning applications. They help in predicting outcomes, 
classifying data, and even recognizing patterns in complex datasets.
'''
import numpy as np

# Set a random seed
np.random.seed(42)

# Generate random numbers with the seed set
random_numbers = np.random.randint(0, 10, 5)
print(random_numbers)  # Output will be the same every time you run this
