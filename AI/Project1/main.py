# Imports
import numpy as np
import sklearn.preprocessing

# Input Data
input_data = np.array([2.1, -1.9, 5.5], [-15., 2.4, 3.5], [0.5, -7.9, 5.6], [5.9, 2.3, -5.8])

# Data Binarization
data_binarized = sklearn.preprocessing.Binarizer(threshold=0.5).transform(input_data)
print(f'\nBinarized Data:\n{data_binarized}')


# Not currently finished