# Rock vs Mine Prediction Using Machine Learning

This project focuses on predicting whether an object detected by sonar signals is a Rock or a Mine using Machine Learning. The model is trained using sonar data and uses Logistic Regression, a supervised learning algorithm, for classification.

## Project Overview

Sonar systems send sound signals and analyze the returned signals to identify objects underwater.  
In this project, sonar signal data is used to build a Machine Learning model that can classify objects as either Rock or Mine.

The complete machine learning workflow is implemented including data collection, preprocessing, model training, and prediction.

## Dataset

The dataset contains sonar signal readings used for binary classification.

- Rock (R)
- Mine (M)

Dataset Link:

https://drive.google.com/file/d/1gPJbO-O5Ecy4NJo0eFp5PXpJZj-3PxXV/view?usp=sharing


## Technologies Used

- Python
- Machine Learning
- Logistic Regression
- Pandas
- NumPy
- Scikit-learn


## Workflow

### 1. Import Libraries

Required Python libraries are imported for:

- Data handling
- Data processing
- Model training
- Model evaluation


### 2. Sonar Data Collection

- Loaded sonar data from CSV file
- Explored dataset information
- Checked data structure and features


### 3. Data Preprocessing

Prepared the dataset before training:

- Checked missing values
- Separated features and target labels
- Converted data into suitable format for model training


### 4. Train Test Split

The dataset was divided into:

- Training Data
- Testing Data

Training data is used to train the model, and testing data is used to check model performance.


### 5. Model Training

Logistic Regression model is used for classification.

Logistic Regression is a supervised machine learning algorithm used for binary classification problems.

Algorithm Used:

- Logistic Regression


## Prediction System

After training, the model can predict new sonar data.

Input:

```
New Sonar Signal Data
```

Model Prediction:

```
Rock (R)
or
Mine (M)
```


## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install numpy pandas scikit-learn
```


## Usage

Run the Python file:

```bash
python rock_mine_prediction.py
```

or open the Jupyter Notebook:

```bash
Rock_vs_Mine_Prediction.ipynb
```


## Results

The Logistic Regression model successfully classifies sonar signals and predicts whether the detected object is a Rock or a Mine.


## Conclusion

This project demonstrates a complete supervised Machine Learning workflow including data preprocessing, training a Logistic Regression model, and making predictions on new sonar data.