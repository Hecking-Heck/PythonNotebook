# Supervised Learning: Classification

#Imports
import sklearn

# Datasets
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

# Set the data as variables
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Print the label names
print(f"Label Names:\n{label_names}")

# Print the labels
print(f"Labels:\n{labels}")

# Print the feature names
print(f"Feature Names:\n{feature_names}")

# Print the features
print(f"Features:\n{features}")

# Orgranizing data into sets
from sklearn.model_selection import train_test_split

# Splitting data into a training set and a test set
# 40 / 60 split
train, test, train_labels, test_labels = train_test_split(features, labels, test_size = 0.40, random_state=42)

# Using the naice bayes algorithm GaussianNB
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

model = gnb.fit(train, train_labels)

# Evaluating the model and its accuracy
preds = gnb.predict(test)
print(f"\nPredictions:\n{preds}")

from sklearn.metrics import accuracy_score
print(f"\nAccuracy:\n{accuracy_score(test_labels, preds)}")