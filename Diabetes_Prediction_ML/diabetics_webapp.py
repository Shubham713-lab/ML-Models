import numpy as np
import streamlit as st
import pickle

loaded_model = pickle.load(open("models/trained_model.sav", 'rb'))

# creating function for prediction
def diabetes_prediction(input_data):

    # changing input data into numpy array
    input_array = np.array(input_data)

    # reshape the array as we are predecting for one instane
    input_data_reshape = input_array.reshape(1, -1)

    # Standardize the input data

    prediction = loaded_model.predict(input_data_reshape)
    # print(prediction)

    if (prediction[0]==0):
        return 'The Person is Non-Diabetics.'
    else:
        return 'The Person is Diabetics.'

def main():

    #giving title
    st.title("Diabetes Prediction Web App") 

    # getting the input data from the user		
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    bmi = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of person')

    # code for prediction

    diagnosis = ''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, bmi, DiabetesPedigreeFunction, Age])
        st.success(diagnosis)


if __name__ == '__main__':
    main()

