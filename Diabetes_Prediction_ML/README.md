# Diabetes Prediction Using Machine Learning

This project focuses on predicting whether a person has diabetes or not using Machine Learning. The model is trained on diabetes data and uses Support Vector Machine (SVM), a supervised learning algorithm, for classification.

## Project Overview

Diabetes prediction is a classification-based machine learning problem where the goal is to analyze medical data and predict the possibility of diabetes.

In this project, the complete machine learning workflow is implemented including data preprocessing, data standardization, model training, and prediction using Support Vector Machine Classifier.

## Dataset

The dataset contains medical information of patients that helps the model identify diabetes patterns.

Target Classes:

- Diabetic
- Non-Diabetic

Dataset Link:

https://drive.google.com/file/d/1brJFtgj9uxD31koKJ_Un4p2bRzDZm32M/view?usp=sharing


## Technologies Used

- Python
- Machine Learning
- Support Vector Machine (SVM)
- Pandas
- NumPy
- Scikit-learn


## Workflow

### 1. Import Libraries

Required Python libraries are imported for:

- Data processing
- Data analysis
- Data standardization
- Model training
- Prediction


### 2. Diabetes Data Collection

- Loaded diabetes dataset
- Explored dataset information
- Analyzed features and target values


### 3. Data Preprocessing

Prepared the dataset before training:

- Checked dataset information
- Handled data values
- Prepared data for machine learning model


### 4. Separating Data and Labels

The dataset is divided into:

- Features (Input Data)
- Labels (Output Data)

Features contain patient information, while labels represent diabetes results.


### 5. Data Standardization

Standardized the feature values using StandardScaler.

Methods used:

- fit()
- transform()

Standardization helps to scale all input features and improve model performance.


### 6. Train Test Split

The dataset was divided into:

- Training Data
- Testing Data

Training data is used for model learning and testing data is used to evaluate model performance.


### 7. Model Training

Support Vector Machine Classifier is used for prediction.

SVM creates an optimal decision boundary to separate different classes using:

- Negative Hyperplane
- Maximum Margin Hyperplane
- Positive Hyperplane
- Support Vectors


Algorithm Used:

- Support Vector Machine Classifier (SVM)


## Prediction System

After training, the model can predict diabetes results from new medical data.

Workflow:

```
New Patient Data
        |
        ↓
Trained SVM Model
        |
        ↓
Prediction Result
```

Output:

```
Diabetic
or
Non-Diabetic
```


## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install required libraries:

```bash
pip install numpy pandas scikit-learn
```


## Usage

Run the Python file:

```bash
python diabetes_prediction.py
```

or open the Jupyter Notebook:

```bash
Diabetes_Prediction.ipynb
```


## Results

The Support Vector Machine model successfully learns from diabetes data and predicts whether a person is diabetic or non-diabetic.


## Conclusion

This project demonstrates the implementation of a complete Machine Learning classification workflow including data preprocessing, standardization, training an SVM classifier, and building a diabetes prediction system.