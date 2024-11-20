# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('study_hours_scores.csv')
print("First five rows of the dataset:")
print(data.head())
print("\nDataset information:")
print(data.info())
print("\nMissing values in the dataset:")
print(data.isnull().sum())

#Define features and target variable
X = data[['Hours']]  # Independent variable (study hours)
y = data['Scores']   # Dependent variable (test scores)

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

#Evaluate the model
#Predict test scores
y_pred = model.predict(X_test)

#Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

#=Visualize the Results
#Plot the regression line with the dataset
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Hours Studied vs Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.legend()
plt.show()

#Make Predictions for new data
# Example: Predict the score for a student who studied for 8 hours
new_hours = [[8]]  # Input study hours
predicted_score = model.predict(new_hours)
print(f"\nPredicted Score for 8 hours of study: {predicted_score[0]:.2f}")
