import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('Diabetes_Prediction_ML/trained_model.sav', 'rb'))

input_data = (1,89,66,23,94,28.1,0.167,21)

# changing input data into numpy array
input_array = np.array(input_data)

# reshape the array as we are predecting for one instane
input_data_reshape = input_array.reshape(1, -1)

# Standardize the input data

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if (prediction[0]==0):
    print('The Person is Non-Diabetics.')
else:
    print('The Person is Diabetics.')