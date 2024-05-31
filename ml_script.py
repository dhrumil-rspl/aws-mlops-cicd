import boto3
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('datasets/dataset.csv')
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model locally
joblib.dump(model, 'model.pkl')

# Upload model to S3
s3 = boto3.client('s3')
s3.upload_file('model.pkl', 'mlops1234', 'model.pkl')
