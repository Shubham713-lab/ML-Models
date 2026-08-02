import numpy as np
import pickle
from pathlib import Path

loaded_model = pickle.load(open('/home/shubham/python-projects/Diabetes_Prediction_ML/trained_model.sav', 'rb'))



input_data = (5,116,74,0,0,25.6,0.201,30)


# changing input data into numpy array
input_array = np.array(input_data)

# reshape the array as we are predecting for one instane
input_data_reshape = input_array.reshape(1, -1)

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if prediction[0] == 0:
    print('The Person is Non-Diabetics.')
else:
    print('The Person is Diabetics.')