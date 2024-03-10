# Imports
import numpy as np
import sklearn.preprocessing

# Input Data
input_data = np.array([[2.1, -1.9, 5.5],
                      [-1.5, 2.4, 3.5],
                      [0.5, -7.9, 5.6],
                      [5.9, 2.3, -5.8]])

# Data Preprocessing
print(f"\n\nDATA PREPROCESSING")

# Data Binarization
data_binarized = sklearn.preprocessing.Binarizer(threshold=0.5).transform(input_data)
print(f'Binarized Data:\n{data_binarized}')

# Mean Removal
print(f"\nMean = {input_data.mean(axis=0)}")
print(f"Std deviation = {input_data.std(axis=0)}")

# Scaling
data_scaled = sklearn.preprocessing.scale(input_data)
print(f"\nMean = {data_scaled.mean(axis=0)}")
print(f"Std deviation = {data_scaled.std(axis=0)}")

# Min max scaling
data_scaler_minmax = sklearn.preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print(f"\nMin max scaled data:\n{data_scaled_minmax}")

# Normalization

# L1 Normalization
data_normalized_11 = sklearn.preprocessing.normalize(input_data, norm = "l1")
print(f"\nL1 normalized data:\n{data_normalized_11}")

# L2 Normalization
data_normalized_12 = sklearn.preprocessing.normalize(input_data, norm="l2")
print(f"\nL2 normalized data:\n{data_normalized_12}")


# Labelling the Data
print(f"\n\nDATA LABELLING\n")
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Creating the label encoder
encoder = sklearn.preprocessing.LabelEncoder()
encoder.fit(input_labels)

# Encoding a set of Labels
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)

# Print the labels
print(f"Labels = {test_labels}")

# Print the encoded labels
print(f"Encoded Labels = {list(encoded_values)}")

# Decoding a set of values
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print(f"Encoded Values = {encoded_values}")
print(f"Decoded Values = {decoded_list}")
